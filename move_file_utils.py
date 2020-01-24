from shutil import move
from sys import stderr
from os.path import abspath, basename, join

from path_utils import safe_mkdir


def move_to_dir(src_file_list: list, dst_dir: str = '.') -> str or None:
    """
    Move a list of files to a specified directory
    :param src_file_list: the list of files to move
    :param dst_dir: the destination directory to move files into
    :return: the destination directory's absolute path,
        or None if failed to create that path
    """

    dst_dir = abspath(str(dst_dir))
    try:
        assert safe_mkdir(dst_dir) is not None,\
            'Failed to create directory "%s"' % dst_dir
    except AssertionError as err:
        print('\n[%s]' % type(err), err, sep='\n', file=stderr)
        return None

    num_success = 0
    num_failure = 0
    num_total = len(src_file_list)

    print('\n[Moving files...]',
          'Moving %d files to "%s"' % (num_total, dst_dir),
          sep='\n', file=stderr)

    for src_file in src_file_list:
        # overwrite the destination file if it already exists
        dst_file = join(dst_dir, basename(src_file))
        try:
            move(src=src_file, dst=dst_file)
            num_success += 1
        except OSError:
            num_failure += 1

    print('\n[Moving files completed]'
          'Success: %d / %d' % (num_success, num_total),
          'Failure: %d / %d' % (num_failure, num_total),
          sep='\n', file=stderr)

    return dst_dir
