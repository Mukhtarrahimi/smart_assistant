# notes.py
from db import get_conn
from utils import now_iso

def add_note(title, content, tags=''):
    conn = get_conn()
    cur = conn.cursor()