import sqlite3
from pathlib import Path
import datetime

DATA_DIR = Path(__file__).parent / 'data'
DB_PATH = DATA_DIR / 'assistant.db'

DATA_DIR.mkdir(exist_ok=True)

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()