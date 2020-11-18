from typing import Union
import shutil
from os.path import abspath, basename, join

from utils.paths import safe_mkdir


def move_to_dir(src_file_list: list, dest_dir: str = '.') -> Union[str, None]:
    """
    Move a list of files to a specified directory.
    Existing files will be overwritten without warning.
    :param src_file_list: the list of files to move.
    :param dest_dir: the destination directory to move files into.
    :return: the destination directory's absolute path,
        or None if failed to create that path.
    """

    dest_dir = abspath(dest_dir)

    num_success = 0
    num_failure = 0
    num_total = len(src_file_list)

    print(f'[Moving files...]\n'
          f'Moving {num_total} files to directory "{dest_dir}"',
          sep='\n')

    # create directory if not existent
    if safe_mkdir(dest_dir) is None:
        return None
    # move files
    for src_file in src_file_list:
        # overwrite the destination file if it already exists
        dest_file = join(dest_dir, basename(src_file))
        try:
            shutil.move(src=src_file, dst=dest_file)
            num_success += 1
        except OSError:
            num_failure += 1

    print(f'[Moving files completed]',
          f'Success: {num_success} / {num_total}',
          f'Success: {num_failure} / {num_total}',
          sep='\n')

    return dest_dir
