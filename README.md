<div align="center">

# 🔐 HackFacebookpass2

<img src="https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20macOS%20%7C%20Windows-green?style=for-the-badge"/>
<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>
<img src="https://img.shields.io/github/stars/lunnar211/HackFacebookpass2?style=for-the-badge&logo=github"/>
<img src="https://img.shields.io/github/forks/lunnar211/HackFacebookpass2?style=for-the-badge&logo=github"/>

<br/>

[![Website](https://img.shields.io/badge/🌐%20Website-lunnar211.github.io-0A66C2?style=for-the-badge&logoColor=white)](https://lunnar211.github.io)
[![GitHub](https://img.shields.io/badge/GitHub-lunnar211-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lunnar211)
[![Profile Views](https://komarev.com/ghpvc/?username=lunnar211&label=Profile+Views&color=0e75b6&style=for-the-badge)](https://github.com/lunnar211)

<br/>

> ### ⚠️ EDUCATIONAL & AUTHORIZED USE ONLY
> Unauthorized access to any computer system or account is **illegal**.  
> Only use this tool against accounts you **own** or have **explicit written permission** to test.

<br/>

**Originally coded by MR.K7C8NG — InDoNeSiA CYBER ErRoR SyStEm**  
🔄 Upgraded to **Python 3** from the original Python 2 build  
👨‍💻 Maintained by **[Dipesh Karki](https://lunnar211.github.io)** — Python Programmer & BCA Student

</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🌐 Supported Platforms](#-supported-platforms)
- [📦 Requirements](#-requirements)
- [⚙️ Installation](#️-installation)
- [🚀 Usage](#-usage)
- [🔧 Troubleshooting](#-troubleshooting)
- [⚖️ Legal Disclaimer](#️-legal-disclaimer)
- [📄 License](#-license)

---

## ✨ Features

### 🔑 Login Methods

| Option | Description |
|--------|-------------|
| **1. masuk** | Login with email + password via REST API |
| **2. Login dengan token** | Login using a valid access token |
| **0. keluar** | Exit the program |

### 🛠️ Post-Login Tools

| Feature | Description |
|---------|-------------|
| 👤 **Account Info** | View your name, user ID, and profile details |
| 👥 **Friends Manager** | List friends, get IDs, accept/delete friend requests |
| 📝 **Create Post** | Publish a post directly from the terminal |
| 🔑 **Wordlist Generator** | Build a custom password list from personal data |
| ✅ **Account Checker** | Bulk-check `user\|pass` combo files — results saved to `live.txt` |
| 🏘️ **Group Lister** | Enumerate all your groups and save IDs to `out/Grupid.txt` |
| 🛡️ **Profile Guard** | Toggle Facebook Profile Guard on or off |

---

## 🌐 Supported Platforms

The tool currently fully supports **Facebook**. The table below shows the current implementation status and planned future support for other major platforms:

| Platform | Type | Status |
|----------|------|--------|
| ![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=flat&logo=facebook&logoColor=white) | Social Network | ✅ Fully Implemented |
| ![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=flat&logo=instagram&logoColor=white) | Social Network | 🔜 Planned |
| ![Twitter/X](https://img.shields.io/badge/Twitter%2FX-000000?style=flat&logo=x&logoColor=white) | Microblogging | 🔜 Planned |
| ![TikTok](https://img.shields.io/badge/TikTok-000000?style=flat&logo=tiktok&logoColor=white) | Video Platform | 🔜 Planned |
| ![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white) | Professional Network | 🔜 Planned |
| ![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=flat&logo=youtube&logoColor=white) | Video Platform | 🔜 Planned |
| ![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=flat&logo=telegram&logoColor=white) | Messaging | 🔜 Planned |

> 🔒 All usage **must** be authorized. Refer to each platform's Terms of Service before any testing.

---

## 📦 Requirements

| Requirement | Minimum Version |
|-------------|----------------|
| 🐍 Python | 3.7+ |
| 📦 pip | Latest |
| 🌐 requests | Any stable |
| 🔧 mechanize | Any stable |

---

## ⚙️ Installation

### Step 1 — Install Python 3 and pip

<details>
<summary>📱 <strong>Termux (Android)</strong></summary>

```bash
pkg update && pkg upgrade
pkg install python
```
</details>

<details>
<summary>🐧 <strong>Debian / Ubuntu / Kali Linux</strong></summary>

```bash
sudo apt update
sudo apt install python3 python3-pip
```
</details>

<details>
<summary>🍎 <strong>macOS (Homebrew)</strong></summary>

```bash
brew install python3
```
</details>

<details>
<summary>🪟 <strong>Windows</strong></summary>

Download and install Python 3 from [python.org](https://www.python.org/downloads/), making sure to check **"Add Python to PATH"** during setup.
</details>

---

### Step 2 — Clone the Repository

```bash
git clone https://github.com/lunnar211/HackFacebookpass2.git
cd HackFacebookpass2
```

### Step 3 — Install Dependencies

```bash
pip3 install requests mechanize
```

Or, if a `requirements.txt` is present:

```bash
pip3 install -r requirements.txt
```

---

## 🚀 Usage

```bash
python3 SETAN2.py
```

You will see the interactive main menu:

```
╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ 
 ║ ├─┤├┬┘├┴┐───╠╣ ╠╩╗
═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝  versi2

║--➤ 1. masuk
║--➤ 2. Login menggunakan token
║--➤ 0. keluar
║
╚═D R
```

> Enter a number and press **Enter** to select an option.

---

### 🔐 Login with Email / Password

1. Select option **`1`**
2. Enter your Facebook **email address** or **ID**
3. Enter your **password** (input is hidden for security)
4. On success, you will enter the feature menu

---

### 🪙 Login with Access Token

1. Select option **`2`**
2. Paste your **Facebook access token** when prompted
3. If the token is valid, you will enter the feature menu

> 💡 You can obtain your access token via Facebook developer tools or Graph API explorer.

---

### ✅ Account Checker

1. Prepare a combo file (one credential per line):
   ```
   user@example.com|password123
   user2@example.com|secret456
   ```
2. After logging in, navigate to **Other → Account Checkers**
3. Enter the file path and the separator character (`|` by default)

📁 Results (valid accounts) are saved to **`live.txt`**

---

## 🔧 Troubleshooting

| ❌ Problem | ✅ Solution |
|-----------|------------|
| `ModuleNotFoundError: No module named 'requests'` | Run `pip3 install requests` |
| `ModuleNotFoundError: No module named 'mechanize'` | Run `pip3 install mechanize` |
| `python3: command not found` | Install Python 3 (see [Installation](#️-installation)) |
| Login fails immediately | The old Facebook mobile API endpoint may be deprecated |
| `[!] No connection` | Check your internet connection and try again |
| Script crashes on import | Make sure you are using **Python 3.7+**, not Python 2 |

---

## ⚖️ Legal Disclaimer

```
THIS SOFTWARE IS PROVIDED FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY.
```

The author(s) are **not responsible** for any misuse, damage, or legal consequences resulting from the use of this program.

By downloading or using this software, **you agree** that:

- ✅ You will only use it on accounts **you own** or have **explicit written permission** to test.
- ✅ You understand that unauthorized account access violates laws in most countries:
  - 🇺🇸 **USA** — Computer Fraud and Abuse Act (CFAA)
  - 🇬🇧 **UK** — Computer Misuse Act 1990
  - 🇮🇩 **Indonesia** — UU ITE No. 11/2008
  - 🇪🇺 **EU** — Directive on Attacks Against Information Systems
- ✅ You acknowledge that Facebook's **Terms of Service** prohibits unauthorized automated access.

---

## 🤝 Contributing

Contributions, bug reports, and suggestions are welcome!

1. 🍴 Fork the repository
2. 🌿 Create a new branch (`git checkout -b feature/your-feature`)
3. 💾 Commit your changes (`git commit -m 'Add some feature'`)
4. 📤 Push to the branch (`git push origin feature/your-feature`)
5. 🔃 Open a **Pull Request**

---

## ⭐ Support the Project

If you find this tool useful for your authorized security research, consider giving it a **⭐ star** on GitHub — it helps others discover the project!

[![GitHub stars](https://img.shields.io/github/stars/lunnar211/HackFacebookpass2?style=social)](https://github.com/lunnar211/HackFacebookpass2/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/lunnar211/HackFacebookpass2?style=social)](https://github.com/lunnar211/HackFacebookpass2/network/members)

---

## 📄 License

**MIT License** — see [LICENSE](LICENSE) for full details.

---

<div align="center">

### 👨‍💻 About the Maintainer

**Dipesh Karki** — Python Programmer & BCA Student

🌐 **Website:** [lunnar211.github.io](https://lunnar211.github.io)  
📧 **Email:** [karkimadan48@gmail.com](mailto:karkimadan48@gmail.com)  
✍️ **Blog:** [learnearnwithonline.blogspot.com](https://learnearnwithonline.blogspot.com)

<br/>

[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://fb.com/diepsh.karki.1800)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/dipesh.karki__)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/c/technicaldipesh_hacks)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lunnar211)

<br/>

Made with ❤️ by **MR.K7C8NG** — *InDoNeSiA CYBER ErRoR SyStEm*  
Maintained & upgraded by **[Dipesh Karki](https://lunnar211.github.io)**

</div>
