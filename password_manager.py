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