# notes.py
from db import get_conn
from utils import now_iso

# --------------
def add_note(title, content, tags=''):
    conn = get_conn()
    cur = conn.cursor()
    t = now_iso()
    cur.execute('INSERT INTO notes (title, content, tags, created_at, updated_at) VALUES (?, ?, ?, ?, ?)',
    (title, content, tags, t, t))
    conn.commit()
    conn.close()

# -----
def list_notes():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT id, title, tags, created_at, updated_at FROM notes ORDER BY created_at DESC')
    rows = cur.fetchall()
    conn.close()
    return rows

def get_note(note_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM notes WHERE id=?', (note_id,))
    r = cur.fetchone()
    conn.close()
    return r

# -----
def search_notes(query):
    conn = get_conn()
    cur = conn.cursor()
    q = f"%{query}%"
    cur.execute('SELECT id, title, tags, created_at FROM notes WHERE title LIKE ? OR content LIKE ? OR tags LIKE ? ORDER BY created_at DESC', (q, q, q))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_note(note_id):
    conn = get_conn()
    cur = conn.cursor()