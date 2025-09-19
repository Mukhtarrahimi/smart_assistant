from pathlib import Path
import shutil
from utils import now_iso

BASE = Path.cwd()



def list_files(folder='.'):
    p = Path(folder)
    return [x for x in p.iterdir()]