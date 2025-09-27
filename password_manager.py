# libraray-----

import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
from pathlib import Path
from db import get_conn
from utils import now_iso

DATA_DIR = Path(__file__).parent / 'data'
SALT_PATH = DATA_DIR / 'master_salt.bin'

# functions-----
def _ensure_salt():
    DATA_DIR.mkdir(exist_ok=True)
    if not SALT_PATH.exists():
        SALT_PATH.write_bytes(os.urandom(16))

def derive_key_from_password(password: str) -> bytes:
    _ensure_salt()
    salt = SALT_PATH.read_bytes()
    kdf = PBKDF2HMAC(
algorithm=hashes.SHA256(),
length=32,
salt=salt,
iterations=390000,
backend=default_backend()
)
    
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key


def add_password(master_password, name, username, plaintext_password, notes=''):
    key = derive_key_from_password(master_password)
    f = Fernet(key)
    token = f.encrypt(plaintext_password.encode())
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO passwords (name, username, encrypted_password, notes, created_at) VALUES (?, ?, ?, ?, ?)',
    (name, username, token.decode(), notes, now_iso()))
    conn.commit()
    conn.close()


# ---
def list_passwords():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT id, name, username, created_at FROM passwords')
    rows = cur.fetchall()
    conn.close()
    return rows

def get_password(master_password, entry_id):
    key = derive_key_from_password(master_password)
    f = Fernet(key)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT encrypted_password FROM passwords WHERE id=?', (entry_id,))
    r = cur.fetchone()
    conn.close()
    if not r:
        return None
    token = r['encrypted_password'].encode()
    try:
        return f.decrypt(token).decode()
    except Exception:
        raise ValueError('Master password incorrect or data corrupted')
    
def delete_password(entry_id):
    pass