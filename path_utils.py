from sys import stderr
from os import makedirs
from os.path import abspath, isfile, isdir
from shutil import rmtree

from err_utils import get_err_msg


def check_file_exists(file_path: str, err_msg: str = None) -> bool:
    """
    Check if the file specified does exist.
    Print an error message if the file does not exist.
    :param file_path: the path of the file
    :param err_msg: the custom error message to use
    :return: True if file exists, False otherwise
    """

    try:
        file_path = '' if (file_path is None) else abspath(str(file_path))
        if isfile(file_path):
            return True
        elif isdir(file_path):
            raise IsADirectoryError('"%s" is a directory')
        else:
            err_msg = 'File "%s" does not exist' % file_path \
                if (err_msg is None) else str(err_msg)
            raise FileNotFoundError(err_msg)

    except OSError as err:
        print(get_err_msg(err), file=stderr)
        return False


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
