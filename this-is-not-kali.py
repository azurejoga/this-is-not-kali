#!/usr/bin/env python3
import subprocess
import os
import json
import argparse
import time

BASE_DIR = "/home/this-not-kali"
INSTALLED_LOG = os.path.join(BASE_DIR, "installed.log")
SKIPPED_LOG = os.path.join(BASE_DIR, "skipped.log")
DEFAULT_TOOL_LIST = os.path.join(BASE_DIR, "my-tools.json")
DEB_DIR = os.path.join(BASE_DIR, "deb_packages")

os.makedirs(BASE_DIR, exist_ok=True)
for path in [INSTALLED_LOG, SKIPPED_LOG, DEFAULT_TOOL_LIST]:
    open(path, 'a').close()

def wait_for_apt_lock():
    while True:
        result = subprocess.run("sudo fuser /var/lib/dpkg/lock", shell=True, stdout=subprocess.DEVNULL)
        if result.returncode != 0:
            break
        print("[!] Waiting for APT lock to be released...")
        time.sleep(2)

def run_command(command):
    return subprocess.run(command, shell=True, check=True, capture_output=True, text=True).stdout

def get_kali_tools(metapackage="kali-linux-everything"):
    print(f"[*] Fetching tools from {metapackage}...")
    output = run_command(f"apt-cache depends {metapackage}")
    tools = []
    for line in output.splitlines():
        line = line.strip()
        if line.startswith("Depends:"):
            tool = line.replace("Depends:", "").strip()
            if tool and tool not in tools:
                tools.append(tool)
    return tools

def add_kali_repo():
    if os.path.exists("/etc/apt/sources.list.d/kali.list"):
        print("[=] Kali repository already present. Skipping addition.")
        return
    print("[*] Adding Kali repository and key...")
    subprocess.run('sudo curl https://archive.kali.org/archive-keyring.gpg -o /usr/share/keyrings/kali-archive-keyring.gpg', shell=True)
    subprocess.run(
        'echo "deb [signed-by=/usr/share/keyrings/kali-archive-keyring.gpg] http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list.d/kali.list',
        shell=True
    )
    subprocess.run('sudo apt update', shell=True)

def remove_kali_repo():
    print("[*] Removing Kali repository...")
    subprocess.run("sudo rm -f /etc/apt/sources.list.d/kali.list", shell=True)
    subprocess.run("sudo apt update", shell=True)

def install_tool(tool):
    wait_for_apt_lock()
    print(f"[+] Installing {tool}...")
    subprocess.run(f"sudo apt install -y {tool}", shell=True)

def save_log(tool, log_path):
    with open(log_path, 'a') as f:
        f.write(tool + '\n')

def is_installed(tool):
    result = subprocess.run(f"dpkg -s {tool}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def interactive_mode(tools):
    for tool in tools:
        if is_installed(tool):
            print(f"[=] {tool} already installed. Skipping.")
            continue
        choice = input(f"Do you want to install {tool}? [y/n]: ").strip().lower()
        if choice == "y":
            install_tool(tool)
            save_log(tool, INSTALLED_LOG)
        else:
            print(f"[-] Skipping {tool}.")
            save_log(tool, SKIPPED_LOG)

def install_all(tools):
    for tool in tools:
        if is_installed(tool):
            print(f"[=] {tool} already installed. Skipping.")
            continue
        install_tool(tool)
        save_log(tool, INSTALLED_LOG)

def search_tools(tools, keyword):
    return [tool for tool in tools if keyword.lower() in tool.lower()]

def export_selection(filename=DEFAULT_TOOL_LIST):
    with open(INSTALLED_LOG) as f:
        installed = [line.strip() for line in f if line.strip()]
    with open(filename, 'w') as f:
        json.dump(installed, f, indent=2)
    print(f"[+] Exported tool list to {filename}")

def restore_from_file(filename=INSTALLED_LOG):
    with open(filename) as f:
        tools = [line.strip() for line in f if line.strip()]
    install_all(tools)

def uninstall_tools(filename=INSTALLED_LOG):
    with open(filename) as f:
        tools = [line.strip() for line in f if line.strip()]
    for tool in tools:
        print(f"[-] Removing {tool}...")
        subprocess.run(f"sudo apt remove -y {tool}", shell=True)

def import_and_show_tools(filename=DEFAULT_TOOL_LIST):
    try:
        with open(filename) as f:
            tools = json.load(f)
        print(f"[+] Imported tools from {filename}:")
        for tool in tools:
            print(f" - {tool}")
    except Exception as e:
        print(f"[!] Failed to import tools: {e}")

def export_offline_packages(log_file=INSTALLED_LOG, output_tar="offline_tools.tar.gz"):
    print(f"[*] Exporting .deb packages listed in {log_file}...")
    os.makedirs(DEB_DIR, exist_ok=True)

    with open(log_file) as f:
        tools = [line.strip() for line in f if line.strip()]

    for tool in tools:
        print(f"[+] Downloading .deb files for {tool}...")
        wait_for_apt_lock()
        result = subprocess.run(f"apt download {tool}", shell=True, cwd=DEB_DIR)
        if result.returncode != 0:
            print(f"[!] Warning: Download failed for {tool}")

    tar_path = os.path.join(BASE_DIR, output_tar)
    subprocess.run(f"tar -czvf {tar_path} -C {BASE_DIR} deb_packages", shell=True)
    print(f"[✔] Packages exported to: {tar_path}")

def generate_offline_installer_script():
    script_path = os.path.join(BASE_DIR, "install_offline.sh")
    with open(script_path, 'w') as f:
        f.write("""#!/bin/bash
set -e
echo "[*] Extracting archive if needed..."
if [ -f offline_tools.tar.gz ]; then
    tar -xvzf offline_tools.tar.gz
fi

if [ -d deb_packages ]; then
    cd deb_packages
    echo "[*] Installing offline tools..."
    sudo dpkg -i *.deb || sudo apt --fix-broken install -y
    echo "[✔] Offline installation completed."
else
    echo "[!] deb_packages folder not found."
    exit 1
fi
""")
    os.chmod(script_path, 0o755)
    print(f"[+] Offline installer script created: {script_path}")

def show_menu():
    print("\n🎯 THIS IS NOT KALI! - Selective Kali Linux Tool Installer, made by azurejoga: https://github.com/azurejoga/ and https://linkedin.com/in/juan-mathews-rebello-santos-/")
    print("1. Install in interactive mode (ask per tool)")
    print("2. Install all tools without asking")
    print("3. Search and install by keyword")
    print("4. Export installed tools list")
    print("5. Restore tools from installed.log")
    print("6. Uninstall tools from installed.log")
    print("7. Remove Kali repository")
    print("8. Import and show tool list from file")
    print("9. Export .deb packages for offline installation")
    print("10. Generate offline installation script")
    print("0. Exit\n")
    return input("Choose an option: ").strip()

def parse_args():
    parser = argparse.ArgumentParser(description="Selective Kali Linux Tool Installer")
    parser.add_argument("--install", nargs="*", help="Install tools by name")
    parser.add_argument("--search", help="Search tools by keyword")
    parser.add_argument("--export", help="Export installed tool list to file")
    parser.add_argument("--restore", help="Restore tools from a file")
    parser.add_argument("--uninstall", help="Uninstall tools listed in a file")
    parser.add_argument("--offline", help="Export .deb packages for offline installation")
    parser.add_argument("--generate-script", action="store_true", help="Generate offline installation script")
    return parser.parse_args()

def main():
    add_kali_repo()
    args = parse_args()

    if args.install:
        tools = get_kali_tools()
        install_all([tool for tool in args.install if tool in tools])
    elif args.search:
        tools = get_kali_tools()
        matched = search_tools(tools, args.search)
        interactive_mode(matched)
    elif args.export:
        export_selection(args.export)
    elif args.restore:
        restore_from_file(args.restore)
    elif args.uninstall:
        uninstall_tools(args.uninstall)
    elif args.offline:
        subprocess.run("sudo chmod o+rx /root /home/this-not-kali", shell=True)
        export_offline_packages()
    elif args.generate_script:
        generate_offline_installer_script()
    else:
        while True:
            option = show_menu()
            if option == "0":
                print("Bye!")
                break

            tools = get_kali_tools()

            if option == "1":
                interactive_mode(tools)
            elif option == "2":
                install_all(tools)
            elif option == "3":
                keyword = input("Enter keyword to search: ").strip()
                matched = search_tools(tools, keyword)
                interactive_mode(matched)
            elif option == "4":
                export_selection()
            elif option == "5":
                restore_from_file()
            elif option == "6":
                uninstall_tools()
            elif option == "7":
                remove_kali_repo()
            elif option == "8":
                import_and_show_tools()
            elif option == "9":
                subprocess.run("sudo chmod o+rx /root /home/this-not-kali", shell=True)
                export_offline_packages()
            elif option == "10":
                generate_offline_installer_script()
            else:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
