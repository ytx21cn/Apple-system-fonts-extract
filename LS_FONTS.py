import glob

from os import lstat
from os.path import join, relpath, abspath, dirname
from sys import argv, stderr
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
    font_files = glob.glob(join(fonts_dir, '**/*.otf'),
                           recursive=True)
    font_files.sort()

    # print header
    separator = ' ' * 4
    ref_time = datetime.utcfromtimestamp(0).__str__()
    print(f'{"[Modified time]":{len(ref_time)}}', '[Filename]', sep=separator)
    print('-' * 80)

    # list font files and modification times
    print('\nListing font files in "%s"' % abspath(fonts_dir), file=stderr)
    base_dir = dirname(__file__)
    for font_file in font_files:
        modified_time = lstat(font_file).st_mtime
        modified_time = datetime.utcfromtimestamp(modified_time)
        font_file = relpath(font_file, start=base_dir)
        print('%s%s%s' % (modified_time, separator, font_file))


if __name__ == '__main__':
    exit(main())
