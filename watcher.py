import os
import time
import subprocess
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from cryptography.fernet import Fernet

WATCH_FOLDER = r"C:\AutoFileProtector\ProtectedFolder"
BASE_DIR = r"C:\AutoFileProtector"
KEY_FILE = os.path.join(BASE_DIR, "secret.key")
LOG_FILE = os.path.join(BASE_DIR, "security_log.txt")

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")

def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        log("Encryption key generated")

def load_key():
    return open(KEY_FILE, "rb").read()

def encrypt_file(path):
    time.sleep(1)

    if not os.path.exists(path):
        return
    if path.endswith(".enc"):
        return

    key = load_key()
    fernet = Fernet(key)

    with open(path, "rb") as f:
        data = f.read()

    if not data:
        return

    encrypted = fernet.encrypt(data)
    enc_path = path + ".enc"

    with open(enc_path, "wb") as f:
        f.write(encrypted)

    os.remove(path)

    subprocess.call(f'attrib +H +S +R "{enc_path}"', shell=True)
    log(f"File encrypted & hidden: {os.path.basename(enc_path)}")
    print("🔐 Encrypted:", os.path.basename(enc_path))

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            encrypt_file(event.src_path)

if __name__ == "__main__":
    print("✅ File Protection Running...")
    log("Watcher started")

    generate_key()

    observer = Observer()
    observer.schedule(Handler(), WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
        log("Watcher stopped")

    observer.join()

