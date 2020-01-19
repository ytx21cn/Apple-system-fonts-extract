from os import makedirs
from os.path import dirname, abspath, isfile, isdir
from shutil import rmtree


def safe_mkdir(dir_path: str):
    """
    Safely create a directory. Supports multi-level directory creation.
    :param dir_path: the path to create a directory.
    """
    dir_path = abspath(str(dir_path))
    if isfile(dir_path):
        pass
    else:
        makedirs(dir_path, exist_ok=True)


def safe_create_file(file_path: str, overwrite: bool = False):
    """
    Safely create a file. Supports multi-level directory creation.
    :param file_path: the path to create a directory.
    :param overwrite: whether to overwrite if a file of that name exists
        (do nothing if a directory of that name exists)
    """
    file_path = abspath(str(file_path))
    if isdir(file_path):
        pass
    elif isfile(file_path) and (not overwrite):
        pass
    else:
        safe_mkdir(dirname(file_path))
        file = open(file_path, 'w')
        file.close()


def safe_remove(path: str):
    """
    Safely remove a file / directory tree.
    :param path: the path to remove.
    """
    path = abspath(str(path))
    rmtree(path, ignore_errors=True)
