# 🎯 THIS IS NOT KALI! – Selective Kali Linux Tool Installer

> A powerful and flexible script to selectively install Kali Linux tools on **non-Kali Debian-based systems**.

---

## 🧭 Overview

**THIS IS NOT KALI!** is a Python-based command-line tool that allows you to:
- Install individual or all tools from any Kali metapackage (like `kali-linux-everything`)
- Interactively choose tools to install
- Export and import installed tool lists
- Download `.deb` packages for offline installations
- Generate a complete offline installer script
- Remove the Kali repository after use to preserve system integrity

This script is designed for penetration testers, CTF enthusiasts, or researchers who want to leverage the power of Kali Linux tools without switching from their current Debian/Ubuntu environment.

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| ✅ Interactive Tool Installation | Choose tools one-by-one during install |
| ✅ Full Install Mode | Automatically install all available tools |
| 🔍 Keyword Search | Search for specific tools and choose to install them |
| 📦 Export Installed Tools | Save the list of installed tools in `.json` format |
| ♻ Restore Tools | Reinstall previously selected tools from log |
| ❌ Uninstall Tools | Cleanly remove all tools previously installed |
| 🧪 Kali Repo Handling | Add/remove Kali Linux repository with key management |
| 💾 Offline Package Export | Download all `.deb` packages and archive them |
| 📜 Offline Installer Generator | Create a self-contained shell script for offline setup |
| 🧠 Command-Line Support | Use command-line flags instead of menu interface |

---

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/azurejoga/this-is-not-kali.git
   cd this-is-not-kali
````

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Run the script:

   ```bash
   python3 this-is-not-kali.py
   ```

---

## 🧑‍💻 Usage

### 📋 Interactive Menu Mode

Simply run the script without arguments to launch the interactive menu:

```bash
python3 this-is-not-kali.py
```

You will see a numbered menu to:

```
1. Install in interactive mode (ask per tool)
2. Install all tools without asking
3. Search and install by keyword
4. Export installed tools list
5. Restore tools from installed.log
6. Uninstall tools from installed.log
7. Remove Kali repository
8. Import and show tool list from file
9. Export .deb packages for offline installation
10. Generate offline installation script
0. Exit
```

---

### ⚙ Command-Line Mode

#### General format:

```bash
python3 this-is-not-kali.py [-options]
```

#### Options:

| Argument               | Description                                                             |
| ---------------------- | ----------------------------------------------------------------------- |
| `--all`                | Install all Kali tools from the specified metapackage                   |
| `--search <keyword>`   | Search for tools matching the keyword and install interactively         |
| `--export <file>`      | Export the list of installed tools to a JSON file                       |
| `--restore <file>`     | Restore and reinstall tools from the specified log or JSON file         |
| `--uninstall <file>`   | Uninstall tools listed in the specified file                            |
| `--metapackage <name>` | Specify a different Kali metapackage (default: `kali-linux-everything`) |

#### Example:

```bash
# Install all tools from default metapackage
python3 this-is-not-kali.py --all

# Search for tools related to 'wifi'
python3 this-is-not-kali.py --search wifi

# Export installed tools list
python3 this-is-not-kali.py --export my_tools.json

# Restore tools from log file
python3 this-is-not-kali.py --restore installed.log

# Uninstall all previously installed tools
python3 this-is-not-kali.py --uninstall installed.log
```

---

## 📡 Offline Features

### Export .deb Packages

```bash
python3 this-is-not-kali.py
# Choose option 9 from the menu
```

This downloads `.deb` packages into `deb_packages/` and compresses them as `offline_tools.tar.gz`.

### Generate Offline Installer

```bash
python3 this-is-not-kali.py
# Choose option 10 from the menu
```

This creates a `install_offline.sh` script which can install all `.deb` files in offline environments.

---

## 📁 Log & Configuration Files

| File                   | Purpose                                           |
| ---------------------- | ------------------------------------------------- |
| `installed.log`        | Tools successfully installed                      |
| `skipped.log`          | Tools skipped during interactive mode             |
| `my-tools.json`        | Exported tool list (for re-import or sharing)     |
| `deb_packages/`        | Folder containing `.deb` packages for offline use |
| `offline_tools.tar.gz` | Compressed archive for offline installation       |

---

## ⚠ Disclaimer

This script **adds and removes** the Kali Linux repository temporarily. Use it responsibly to avoid unwanted system behavior. It is recommended to remove the Kali repo after installing your desired tools.

---

## 🧪 Tested On

* Debian 12
* Ubuntu 22.04 LTS
* Linux Mint

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open issues for bugs, enhancements, or feature suggestions.

* [linkedin](https://linkedin.com/in/juan-mathews-rebello-santos-/)

---

