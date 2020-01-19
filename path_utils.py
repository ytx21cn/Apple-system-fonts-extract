from sys import stderr
from os import makedirs
from os.path import dirname, abspath, isfile, isdir
from shutil import rmtree


def safe_mkdir(dir_path: str):
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
        makedirs(dir_path, exist_ok=True)
        print('Created directory: "%s"' % dir_path, file=stderr)
        return dir_path

    except OSError as err:
        print('\n[OSError]\n%s' % err, file=stderr)
        print('Failed to create directory: "%s"' % dir_path, file=stderr)
        return None


def safe_create_file(file_path: str, overwrite: bool = False):
    """
    Safely create a file.
    Supports multi-level directory creation.
    :param file_path: the path to create a directory.
    :param overwrite: whether to overwrite if a file of that name exists
        (do nothing if a directory of that name exists)
    :return the absolute path of the file,
        or None if failed to create the file.
    """

    file_path = abspath(str(file_path))

    try:
        print('\n[Creating file...]', file=stderr)
        if isdir(file_path):
            raise IsADirectoryError
        elif isfile(file_path) and (not overwrite):
            print('File "%s" already exists, and is not overwritten'
                  % file_path, file=stderr)
            return file_path
        else:
            safe_mkdir(dirname(file_path))
            file = open(file_path, 'w')
            file.close()
            print('Created file "%s"' % file_path, file=stderr)
            return file_path

    except OSError as err:
        print('\n[OSError]\n%s' % err, file=stderr)
        print('Failed to create file: "%s"' % file_path, file=stderr)
        return None


def safe_remove(path: str):
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

    except OSError:
        print('[OSError]', file=stderr)
        print('Failed to removed item: "%s"' % path, file=stderr)
        return None
