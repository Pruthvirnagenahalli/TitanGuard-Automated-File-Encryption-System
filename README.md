Automatic File Protection System
Overview

The Automatic File Protection System is a Python-based security application that automatically encrypts files as soon as they are created in a protected directory. The system ensures that sensitive files are never stored in plaintext form and can only be accessed by authorized users using password-based authentication.

This project demonstrates practical implementation of cybersecurity concepts such as file system monitoring, encryption, access control, and security logging

**Key Features**

1)Real-time folder monitoring

2)Automatic file encryption on creation

3)Password-based secure file access

4)Temporary decryption for authorized users

5)Automatic re-encryption after file access

6)ecurity event logging

7)Protection against unauthorized file access


**Technologies Used**

1)Python 3

2)Watchdog (File system monitoring)

3)Cryptography (Fernet encryption)

4)Windows File Attributes

5)Command Line Interface (CLI)


**How the System Works**

The watcher module continuously monitors a protected folder.

When a new file is created, it is immediately encrypted.

The original plaintext file is removed.

Encrypted files remain unreadable if accessed directly.

Authorized users can open files using the secure opener.

Files are automatically re-encrypted after use.

All security events are recorded in a log file.


**Installation and Setup**

Clone the repository:

git clone <repository-url>


Navigate to the project directory:

cd AutoFileProtector


Create and activate virtual environment:

python -m venv venv
venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


**Usage**

Start the file watcher:

python watcher.py

Create files inside the protected folder.

Use the secure file opener:

python opener.py

Provide the encrypted file path and correct password when prompted.


**Security Notes**

Encrypted files cannot be read without the correct password.

Renaming encrypted files does not reveal original content.

Encryption keys and logs are excluded from version control.

The protected folder contents are hidden from unauthorized access.


**Future Enhancements**

Graphical User Interface (GUI)

Multi-user authentication

Intrusion detection and alerts

Encrypted and protected security logs

Cross-platform support

**Author**

**Pruthvi R,
Information Science Student**
