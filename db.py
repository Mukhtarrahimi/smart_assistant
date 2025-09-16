import sqlite3
from pathlib import Path
import datetime

DATA_DIR = Path(__file__).parent / 'data'
DB_PATH = DATA_DIR / 'assistant.db'