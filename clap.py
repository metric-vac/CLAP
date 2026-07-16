import requests
import os
import sys
import string
import random

# --- Settings ---
CACHE_FILE = "top_10m_passwords.txt"
URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/xato-net-10-million-passwords.txt"

def download_wordlist():
    """Downloads the wordlist if it doesn't exist."""
    if not os.path.exists(CACHE_FILE):
        print(f"Downloading wordlist to {CACHE_FILE}...")
        try:
            r = requests.get(URL, timeout=30)
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                f.write(r.text)
            print("Download complete.")
        except Exception as e:
            print(f"Failed to download wordlist: {e}")
            return False
    else:
        print("Wordlist already exists")
    return True

def check_password(target):
    """Checks if a password exists in the local wordlist."""
    if not os.path.exists(CACHE_FILE):
        download_wordlist()
        print("Wordlist not found. Downloading...")

    print("Analyzing password...")
    try:
        with open(CACHE_FILE, "r", encoding="utf-8", errors="ignore") as f:
            # Using a generator for memory efficiency instead of reading all lines at once
            for line in f:
                if line.strip() == target:
                    print("RESULT: COMPROMISED! Password found in database. Generate a secure password using -g or --gen")
                    return
        print("RESULT: SAFE. No match found in database.")
    except Exception as e:
        print(f"Error reading cache file: {e}")

def generate_password(length):
    """Generates a random 16-character password."""
    pool = string.ascii_uppercase + string.ascii_lowercase + string.digits
    try:
        return "".join(random.choice(pool) for _ in range(length))
    except ValueError:
        print("Length provided was invalid, use numbers between 4-100")

def clear_cache():
    """Removes the local wordlist file."""
    if os.path.exists(CACHE_FILE):
        os.remove(CACHE_FILE)
        print("Cache deleted.")
    else:
        print("Cache file does not exist.")

def main():

    try:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":

            print("Welcome to CLAP(Credential Leak Analysis Program) by metric_vac")
            print("HOW TO USE\n---------- ----------")
            print("[-p] or [--pass] to check your password [ clap.py -c 'your password' ]")
            print("[-d] or [--down] to download and cache a password wordlist [ clap.py -d ]")
            print("[-c] or [--clear] to clear the cache [ clap.py -c ]")
            print("[-g] or [--gen] to generate a secure password [ clap.py -g 16 <- length of the password ]")
            print("---------- ----------")
    except IndexError:
        print("CLAP - Credential Leak Analysis Peogram by metric_vac")
        print("Use -h or --help to see the commands")
        return


    if sys.argv[1] == "-p" or sys.argv[1] == "--pass":

        try:
            check_password(sys.argv[2])
        except IndexError:
            print("Error: Password wasnt given. Enter in your password after -p or --pass")

    elif sys.argv[1] == "-d" or sys.argv[1] == "--down":
        download_wordlist()

    elif sys.argv[1] == "-c" or sys.argv[1] == "--clear":
        clear_cache()

    elif sys.argv[1] == "-g" or sys.argv[1] == "--gen":
        try:
            if int(sys.argv[2]) < 4 or int(sys.argv[2]) > 100:
                print("Error: cant choose length under 4 or over 100")
                return

            print(f"Password Generated: {generate_password(int(sys.argv[2]))}")
            return
        except IndexError:
            print(f"Length wasnt given. Defaulting to 16\nGenerated Password: {generate_password(16)}")
            return








if __name__ == "__main__":
    main()
