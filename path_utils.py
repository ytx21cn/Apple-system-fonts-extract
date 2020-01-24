from sys import stderr
from os import makedirs
from os.path import abspath, isfile, isdir
from shutil import rmtree

from err_utils import get_err_msg


def safe_mkdir(dir_path: str) -> str or None:
    """
    Safely create a directory.
    Supports multi-level directory creation.
    :param dir_path: the path to create a directory.
    :return the absolute path of the directory,
        or None if failed to create directory.
    """

    dir_path = abspath(str(dir_path))

    try:
        print('\n[Creating directory...]', file=stderr)
        if isfile(dir_path):
            raise FileExistsError('"%s" is an existing file')
        elif isdir(dir_path):
            print('Directory "%s" already exists, so not created'
                  % dir_path, file=stderr)
            return dir_path
        else:
            makedirs(dir_path)
            print('Created directory: "%s"' % dir_path, file=stderr)
            return dir_path

    except OSError as err:
        print(get_err_msg(err), 'Failed to create directory: "%s"'
              % dir_path, sep='\n', file=stderr)
        return None


def safe_remove(path: str) -> str or None:
    """
    Safely remove a file / directory tree.
    :param path: the path to remove.
    :return the path removed, or None if failed to remove.
    """

    path = abspath(str(path))

    try:
        print('\n[Removing item...]', file=stderr)
        rmtree(path)
        print('Removed item: "%s"' % path, file=stderr)
        return path

    except OSError as err:
        print(get_err_msg(err), 'Failed to removed item: "%s"' % path,
              sep='\n', file=stderr)
        return None
