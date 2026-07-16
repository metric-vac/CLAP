# 🔐 CLAP v2.0

**Credential Leak Analysis Program**

A fast, minimal and visually clean CLI tool to check whether a
password appears in massive real-world leaked credential datasets.

------------------------------------------------------------------------

## 🚀 Features

-   🔍 **Password Leak Detection**\
    Checks your password against a 10M+ leaked password database.

-   ⚡ **Extremely Fast Local Scanning**\
    Downloads the wordlist once and caches it for offline use.

-   🔐 **Secure Password Generator**\
    Instantly generate strong random passwords.

-   🧹 **Cache Wipe System**\
    Delete the downloaded database anytime.

------------------------------------------------------------------------

## 📦 Installation

### 1. Clone the repo

``` bash
git clone https://github.com/metric-vac/CLAP
cd CLAP
```

### 2. Install dependencies

``` bash
pip install requests
```

### 3. Run the app

``` bash
python main.py
```

------------------------------------------------------------------------

## 📥 How To Use
CLAP works like any other CLI tool by using flags. Flags are:
- [-p] or [--pass] to check your password againts the 10 million common passwords
- [-d] or [--down] to download the 10 million password wordlist and cache it for offline use
- [-c] or [--clear] to delete the cached password list
- [-g] or [--gen] to generate a secure password

------------------------------------------------------------------------

## PERFORMANCE

CLAP v2.0 Metrics(NOTICE: This were all recorded using passwords that were not in the wordlist, so performance may vary by the password inputed)

-  Uses about 0.1GB(100MB) of RAM to scan through the wordlist
-  Takes approximatly 1.5 seconds to go through the whole wordlist

------------------------------------------------------------------------

## ⚙️ How It Works

1.  Takes user input password\
2.  Loads cached password dataset\
3.  Performs a linear scan comparison\
4.  Outputs:
    -   ❌ **COMPROMISED** → Found in leaks\
    -   ✅ **SAFE** → Not found

------------------------------------------------------------------------

## ⚠️ Important Notes

-   This tool only checks against **known leaked passwords**\
-   "SAFE" does **NOT** mean unbreakable\
-   Large dataset → The wordlist used is optimized for faster scans\
-   Passwords are **never sent anywhere. it is only used to check againts the wordlist**

------------------------------------------------------------------------

## 🧠 Future Improvements

-   Hash-based lookup (faster than linear scan)\
-   Partial match / fuzzy detection\
-   API integration (HaveIBeenPwned-style)\
-   Performance Upgrades(optimized wordlists and fine tuning)
-   Export scan reports

------------------------------------------------------------------------

## 🛠️ Built With

-   Python\
-   Requests

------------------------------------------------------------------------

## 📜 License

MIT License

------------------------------------------------------------------------

