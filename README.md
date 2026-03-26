# HackFacebookpass2

> **⚠️ WARNING:** This tool is for **educational purposes only**.  
> Unauthorized access to any computer system or account is **illegal**.  
> Only use against accounts you own or have explicit written permission to test.

Originally coded by **MR.K7C8NG** (InDoNeSiA CYBER ErRoR SyStEm).  
Upgraded to **Python 3** from the original obfuscated Python 2 build.

---

## Features

| Option | Description |
|--------|-------------|
| 1. masuk | Login with Facebook email + password (REST API) |
| 2. Login dengan token | Login using a Facebook access token |
| 0. keluar | Exit |

### After login you can:
- View account information (name, ID)
- List friends / get IDs
- Accept friend requests
- Delete all friends
- Other tools:
  - Create a Facebook post
  - Generate a password wordlist from personal data
  - Account checker (reads `user|pass` combo file)
  - List your groups and save to `out/Grupid.txt`
  - Activate / deactivate Profile Guard

---

## Requirements

- **Python 3.7+**
- **pip** (Python 3 package manager)
- **requests** library
- **mechanize** library

---

## Installation

### 1. Install Python 3 and pip

**Termux (Android):**
```bash
pkg update && pkg upgrade
pkg install python
```

**Debian / Ubuntu:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**macOS (Homebrew):**
```bash
brew install python3
```

### 2. Clone the repository

```bash
git clone https://github.com/lunnar211/HackFacebookpass2.git
cd HackFacebookpass2
```

### 3. Install Python dependencies

```bash
pip3 install requests mechanize
```

Or using the requirements file (if present):
```bash
pip3 install -r requirements.txt
```

---

## Usage

```bash
python3 SETAN2.py
```

You will see the main menu:

```
║--➤ 1. masuk
║--➤ 2. Login menggunakan token
║--➤ 0. keluar
║
╚═D R
```

Enter a number and press **Enter**.

### Login with email/password

1. Select **1**
2. Enter your Facebook email / ID
3. Enter your password (hidden input)
4. If login succeeds, you will enter the feature menu

### Login with token

1. Select **2**
2. Paste your Facebook access token when prompted
3. If the token is valid, you will enter the feature menu

### Account Checker

1. Prepare a text file with credentials (one per line):
   ```
   user@example.com|password123
   user2@example.com|secret456
   ```
2. After logging in, go to **Other → Account Checkers**
3. Enter the file path and separator character

Results are saved to `live.txt`.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: No module named 'requests'` | Run `pip3 install requests` |
| `ModuleNotFoundError: No module named 'mechanize'` | Run `pip3 install mechanize` |
| `python3: command not found` | Install Python 3 (see Installation section) |
| Login fails immediately | Facebook may have deprecated the old mobile API endpoint. |
| `[!] No connection` | Check your internet connection. |

---

## Legal Disclaimer

This software is provided for **educational and research purposes only**.  
The author(s) are **not responsible** for any misuse or damage caused by this program.  
By using this software, you agree that:

- You will only use it against accounts you own or have explicit permission to test.
- You understand that unauthorized account access violates laws in most countries (e.g., CFAA in the USA, Computer Misuse Act in the UK, UU ITE in Indonesia).
- Facebook's Terms of Service prohibit automated access to their platform without permission.

---

## License

MIT – see [LICENSE](LICENSE) for details.
