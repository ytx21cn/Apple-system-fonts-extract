from os import lstat
from shutil import get_terminal_size
from os.path import join, relpath, abspath, dirname
from sys import argv, stderr
from glob import glob
from datetime import datetime

from timing_utils import time_func


@time_func
def main():
    """
    This function lists the font files and their modified time.
    :return: 0 on success
        1 with invalid arguments
    """

    # check command line arguments
    if len(argv) < 2:
        print('Usage: python3 %s <fonts directory>' % __file__, file=stderr)
        return 1

    # get font files
    fonts_dir = argv[1]
    font_files = glob(join(fonts_dir, '**/*.otf'), recursive=True)
    font_files.sort()

    base_dir = dirname(__file__)

    # print header
    time_now = datetime.utcnow()
    time_now = time_now.__str__().replace('.%d' % time_now.microsecond, '')
    print('{:{:d}s} {:s}'
          .format('[Modified time]', len(time_now), '[File name]'),
          sep=' ')
    terminal_size = get_terminal_size()
    print('-' * terminal_size.columns)

    # list font files and modification times
    print('\nListing font files in "%s"' % abspath(fonts_dir), file=stderr)
    for font_file in font_files:
        modified_time = lstat(font_file).st_mtime
        modified_time = datetime.utcfromtimestamp(modified_time)
        font_file = relpath(font_file, start=base_dir)
        print('%s %s' % (modified_time, font_file))


if __name__ == '__main__':
    exit(main())
