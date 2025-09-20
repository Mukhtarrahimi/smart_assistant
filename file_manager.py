from pathlib import Path
import shutil
from utils import now_iso

BASE = Path.cwd()



def list_files(folder='.'):
    p = Path(folder)
    return [x for x in p.iterdir()]

def copy_file(src, dest):
    src = Path(src)
    dest = Path(dest)
    shutil.copy2(src, dest)
    return dest

def move_file(src, dest):
    src = Path(src)
    dest = Path(dest)
    shutil.move(str(src), str(dest))
    return dest

def delete_file(path):
    pass