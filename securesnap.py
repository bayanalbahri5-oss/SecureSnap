# securesnap.py
import os

def check_firewall():
    status = os.popen("defaults read /Library/Preferences/com.apple.alf globalstate").read().strip()
    return "Enabled" if status == "1" else "Disabled"

def main():
    print("=== SecureSnap Security Check ===")
    print(f"Firewall: {check_firewall()}")
    # Here you can add more checks: FileVault, Updates, etc.

if __name__ == "__main__":
    main()
