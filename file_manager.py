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
    p = Path(path)
    if p.exists():
        if p.is_file():
            p.unlink()
            return True
    elif p.is_dir():
        shutil.rmtree(p)
        return True
    return False


def sort_files_by_extension(folder='.', target_folder=None):
    folder = Path(folder)
    target_folder = Path(target_folder) if target_folder else folder
    moved = []