import os
import subprocess
import time
import platform

# Checking if ProtonVPN CLI is installed
def check_protonvpn():
    result = subprocess.run(["protonvpn-cli", "--version"], capture_output=True, text=True, shell=True)
    if result.returncode == 0:
        print(f"OS: {platform.system()}")
        print("Proton-VPN CLI is installed.")
        print(f"Version: {result.stdout.strip()}")
        return True
    else:
        print("Proton-VPN CLI is not installed.")
        return False

# Changing IP in windows
def change_ip_windows(ip_per):
    os.system("protonvpn-cli d")
    time.sleep(ip_per)
    os.system("protonvpn-cli c -f")

# Changing IP in linux
def change_ip_linux(ip_per):
    os.system("protonvpn-cli disconnect")
    time.sleep(ip_per)
    os.system("protonvpn-cli connect --fastest")

# Changing IP in macOS
def change_ip_mac(ip_per):
    os.system("protonvpn-cli disconnect")
    time.sleep(ip_per)
    os.system("protonvpn-cli connect --fastest")

# Kicking unsupported OS
def unsupported_os():
    print("Your OS is not supported for this script")
    print("Proton-VPN CLI officially supports Windows, Linux, and macOS")
    print("If you are using a different OS, manually check ProtonVPN's documentation")

#Changing IPs
def main():
    if not check_protonvpn():
        return

    ip_per = int(input("Enter how often you want the IP to change (in seconds): "))
    num_changes = int(input("Enter how many times you want the IP to change: "))

    os_name = platform.system()

    for i in range(num_changes):
        print(f"Changing IP... ({i+1}/{num_changes})")
        
        if os_name == "Windows":
            change_ip_windows(ip_per)
        elif os_name == "Linux":
            change_ip_linux(ip_per)
        elif os_name == "Darwin":
            change_ip_mac(ip_per)
        else:
            unsupported_os()
            return

        print(f"IP change complete {i+1}/{num_changes}")

if __name__ == "__main__":
    main()
