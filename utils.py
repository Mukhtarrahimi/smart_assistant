# utils.py
import os
import time
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).parent / 'data'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def now_iso():
    return datetime.now().isoformat(sep=' ', timespec='seconds')

def confirm(prompt='Are you sure? (y/n): '):
    ans = input(prompt).strip().lower()
    return ans in ('y', 'yes')

def human_dt(dt_str):
    try:
        return datetime.fromisoformat(dt_str).strftime('%Y-%m-%d %H:%M')
    except Exception:
        return dt_str