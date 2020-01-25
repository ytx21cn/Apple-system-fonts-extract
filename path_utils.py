from sys import stderr
from os import makedirs, renames
from os.path import abspath, normpath, isfile, isdir, splitext
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

    file_path = '' if (file_path is None) else abspath(str(file_path))

    try:
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


def change_ext(file_path: str, ext: str, rename_file: bool = False)\
        -> str or None:
    """
    Change the extension of specified file_path.
    :param file_path: the original file path.
    :param ext: the new extension.
    :param rename_file: Whether to rename that file if the file exists.
    :return: the absolute path of the file with new extension,
        or None if extension is illegal or failed to rename.
    """

    # set proper file path and extension
    file_path = normpath(str(file_path))
    if ext is None:
        ext = ''
    else:
        ext = str(ext)
        try:
            assert ext.find('/') == -1, 'Illegal extension "%s", '\
                'extension should not contain "/"' % ext
        except AssertionError as err:
            print(get_err_msg(err), file=stderr)
            return None
        if not ext.startswith('.'):
            ext = '.' + ext

    # set new extension
    new_file_path = splitext(file_path)[0] + ext
    if rename_file:
        try:
            renames(file_path, new_file_path)
        except OSError:
            print(get_err_msg(), file=stderr)
            return None
    file_path = abspath(normpath(new_file_path))
    return file_path


def safe_mkdir(dir_path: str) -> str or None:
    """
    Safely create a directory.
    Supports multi-level directory creation.
    :param dir_path: the path to create a directory.
    :return the absolute path of the directory,
        or None if failed to create directory.
    """

    dir_path = abspath(normpath(str(dir_path)))

    try:
        print('\n[Creating directory...]', file=stderr)
        if isdir(dir_path):
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

    path = abspath(normpath(str(path)))

    try:
        print('\n[Removing item...]', file=stderr)
        rmtree(path)
        print('Removed item: "%s"' % path, file=stderr)
        return path

    except OSError as err:
        print(get_err_msg(err), 'Failed to removed item: "%s"' % path,
              sep='\n', file=stderr)
        return None
