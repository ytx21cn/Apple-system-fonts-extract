from os import mkdir
from shutil import rmtree


def safe_mkdir(path: str):
    path = str(path)
    try:
        mkdir(path)
    except FileExistsError:
        pass


def safe_remove(path: str):
    path = str(path)
    rmtree(path, ignore_errors=True)
