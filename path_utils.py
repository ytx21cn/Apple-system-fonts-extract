from os import makedirs
from shutil import rmtree


def safe_mkdir(path: str):
    path = str(path)
    makedirs(path, exist_ok=True)


def safe_remove(path: str):
    path = str(path)
    rmtree(path, ignore_errors=True)
