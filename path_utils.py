from sys import stderr
from os import makedirs
from os.path import dirname, abspath, isfile, isdir
from shutil import rmtree


def safe_mkdir(dir_path: str):
    """
    Safely create a directory. Supports multi-level directory creation.
    :param dir_path: the path to create a directory.
    :return the path to directory, or None if failed to create directory
    """
    dir_path = abspath(dir_path)
    try:
        print('\n[Creating directory...]', file=stderr)
        makedirs(dir_path, exist_ok=True)
        print('Created directory: "%s"' % dir_path, file=stderr)
        return dir_path
    except OSError as err:
        print('\n[OSError]\n%s' % err, file=stderr)
        print('Failed to create directory: "%s"' % dir_path, file=stderr)
        return None


def safe_create_file(file_path: str, overwrite: bool = False):
    """
    Safely create a file. Supports multi-level directory creation.
    :param file_path: the path to create a directory.
    :param overwrite: whether to overwrite if a file of that name exists
        (do nothing if a directory of that name exists)
    """
    file_path = abspath(str(file_path))
    if isdir(file_path):
        raise IsADirectoryError
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
