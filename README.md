# 🎯 This is not Kali! - Kali Linux tool selective installer

> A powerful and flexible script to selectively install Kali Linux tools in ** Debian -based systems that are not Kali **.

---

## 🧭 Overview

** this is not kali! ** It is a python -based command line tool that allows:

* Install individually or all tools of any Kali Metapacote (such as `Kali-Linux-Everything`)
* Interactively choose the tools to be installed
* Export and import tools of installed tools
* Download Packages `.deb` For offline installations
* Generate a complete offline installer script
* Remove the Kali repository after use to preserve system integrity

This script is designed for penetration testers, CTF enthusiasts or researchers who want to take advantage of the power of Kali Linux tools without changing their current environment Debian/Ubuntu.---

## 🚀 features

| RESOURCE | Description |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| ✅ Interactive installation | Choose tools one by one during installation |
| ✅ Complete installation mode | Automatically installs all available tools |
| 🔍 Keyword Search | Search specific tools and choose to install them |
| 📦 Export tools | Save the list of tools installed in `.json` |
| ♻ Restore tools | Reinstall tools previously selected from log |
| ❌ Uninstall tools | Remove all previously installed tools |
| 🧪 Repository Management | Add/Remove Kali Repository with Key Management |
| 💾 Export offline packages | Download all `.deb` packages and archive them |
| 📜 Generate offline installer | Create an autonomous shell script for offline configuration |
| 🧠 Command Line Support | Use command line flags instead of the menu interface |
---

## 🛠 Installation

### 1. Clone the repository:

   git clone https://github.com/azurejoga/this-not-kali.git

   cd this-is-not-kali

### 2. * (Optional) * Create and enable a virtual environment:

   Python3 -m Venv Venv

   SOURCE VENV/BIN/activate

### 3. Run the script:

   Python3 this-is-not-kali.py



---

## 🧑‍💻 Use

### 📋 Interactive Mode (Menu)

Run the script without arguments to start the interactive menu:

Python3 this-is-not-kali.py


You will see a numbered menu:


1. Install in interactive mode (asking by tool)
2. Install all tools without asking
3. Search and install by keyword
4. Export list of installed tools
5. Restore Installed.log tools
6. Uninstall Installed.log tools
7. Remove Kali repository
8. Import and show file tool list
9. Export Packages .DEB For Offline Installation
10. Generate Offline Installation Script
0.


---

### ⚙ Command Line Mode

#### General format:

Python3 this-is-not-kali.py [Options]


#### Options:

| Argument | Description |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| `---all` | Install all specified metapote tools |
| `-Search <Word>` | Search tools corresponding to the keyword and installs interactively |
| `--Export <File>` | Export the list of tools installed to a JSON file |
| `-Restore <File>` | Restores and Reinstall Log or JSON File Tools specified |
| `-uninstall <file>` | Uninstall tools listed in the specified file |
| `--metapackage <name>` | Specifies a different Kali metapacote (default: `kali-linux-eurything`) |

#### Example:


# Install all standard metapacote tools
python3 this-is-not-kali.py--all

# Search for WiFi -related tools
Python3 this-is-not-kali.py -search wifi

# Uninstall all previously installed tools
python3 this-is-not-kali.py -uninstall installled.log


---

## 📡 Offline features

### Export Packages .Deb


Python3 this-is-not-kali.py
# Choose option 9 from the menu


This will download the `.deb` packages to the` Deb_Packages/`directory and compress them as` offline_tools.tar.gz`.

### Generate offline installer


Python3 this-is-not-kali.py
# Choose option 10 from the menu


This will create a `install_offline script.SH` can install all `.deb` files in offline environments.

---

## 📁 Log and configuration files

| File | Purpose |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| `Installed.log` | Successful Tools installed |
| `skipped.log` | Tools ignored during interactive mode |
| `my-tools.json` | List of Exported Tools (for repayment or sharing) |
| `Deb_Packages/` | Folder containing `.deb` packages for offline use |
| `offline_tools.tar.gz` | Compressed File for Offline Installation |

---

## ⚠ Warning

This script ** adds and temporarily removes the Kali Linux repository. Use it responsibly to avoid unwanted behavior in the system. It is recommended to remove the Kali repository after installing the desired tools.

---

## 🧪 Tested in

* Debian 12
* Ubuntu 22.04 lts
* Linux Mint

---

## 🤝 Contributing

Pull Requests are welcome! Feel free to open bugs for bugs, improvements or suggestions for resource.

* [LinkedIn – Juan Mathews Rebello Santos](https://linkedin.com/in/juan-mathews-rebello-santos-/)

