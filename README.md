# 🔐 CLAP v1.0

**Credential Leak Analysis Program**

A fast, minimal, and visually clean desktop tool to check whether a
password appears in massive real-world leaked credential datasets.

------------------------------------------------------------------------

## 🚀 Features

-   🔍 **Password Leak Detection**\
    Checks your password against a 10M+ leaked password database.

-   ⚡ **Fast Local Scanning**\
    Downloads the wordlist once and caches it for offline use.

-   🧠 **Live Console Mode** *(optional)*\
    Watch the scan process in real-time (slower but cool).

-   🔐 **Secure Password Generator**\
    Instantly generate strong random passwords.

-   👁 **Show/Hide Password Toggle**

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
pip install customtkinter requests
```

### 3. Run the app

``` bash
python main.py
```

------------------------------------------------------------------------

## 📥 First Run Behavior

On first use, CLAP will download a large password dataset (\~100MB+):

-   Source: SecLists (top 10 million passwords)
-   Stored locally as: top_10m_passwords.txt

After that, all scans are **offline and fast**.

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
-   Large dataset → enabling console mode slows performance\
-   Passwords are **never sent anywhere except initial dataset
    download**

------------------------------------------------------------------------

## 🧠 Future Improvements

-   Hash-based lookup (faster than linear scan)\
-   Partial match / fuzzy detection\
-   API integration (HaveIBeenPwned-style)\
-   UI animations & themes\
-   Export scan reports

------------------------------------------------------------------------

## 🛠️ Built With

-   Python\
-   CustomTkinter\
-   Requests

------------------------------------------------------------------------

## 📜 License

MIT License

------------------------------------------------------------------------

