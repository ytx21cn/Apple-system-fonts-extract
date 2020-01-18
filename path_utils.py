from os import makedirs, renames
from tempfile import mkstemp
from shutil import rmtree


def safe_mkdir(dir_path: str):
    dir_path = str(dir_path)
    makedirs(dir_path, exist_ok=True)


def safe_create_file(file_path: str):
    file_path = str(file_path)
    temp_file_name = mkstemp(dir='.')[1]
    renames(temp_file_name, file_path)


def safe_remove(path: str):
    path = str(path)
    rmtree(path, ignore_errors=True)
