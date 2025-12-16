import os
import sys
import subprocess
from cryptography.fernet import Fernet
from datetime import datetime

BASE_DIR = r"C:\AutoFileProtector"
KEY_FILE = os.path.join(BASE_DIR, "secret.key")
LOG_FILE = os.path.join(BASE_DIR, "security_log.txt")
PASSWORD = "admin123"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")

def load_key():
    return open(KEY_FILE, "rb").read()

def decrypt(enc_path):
    key = load_key()
    fernet = Fernet(key)

    with open(enc_path, "rb") as f:
        encrypted = f.read()

    decrypted = fernet.decrypt(encrypted)
    original = enc_path.replace(".enc", "")

    with open(original, "wb") as f:
        f.write(decrypted)

    os.remove(enc_path)
    return original

def encrypt(path):
    key = load_key()
    fernet = Fernet(key)

    with open(path, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)
    enc_path = path + ".enc"

    with open(enc_path, "wb") as f:
        f.write(encrypted)

    os.remove(path)
    subprocess.call(f'attrib +H +S +R "{enc_path}"', shell=True)

if __name__ == "__main__":

    if len(sys.argv) > 1:
        enc_path = sys.argv[1]
    else:
        enc_path = input("Enter path of .enc file: ").strip()

    password = input("Enter Password: ")

    if password != PASSWORD:
        log("Wrong password attempt")
        print("❌ Wrong password")
        sys.exit()

    log(f"Authorized access: {os.path.basename(enc_path)}")

    original = decrypt(enc_path)
    subprocess.call(f'notepad "{original}"', shell=True)

    input("Press ENTER after closing the file...")

    encrypt(original)
    log(f"File re-encrypted: {os.path.basename(enc_path)}")
    print("🔒 File locked again successfully")
