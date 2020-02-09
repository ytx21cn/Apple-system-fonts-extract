import subprocess as sp

from sys import argv, stderr
from os.path import isdir, abspath

from timing_utils import time_func
from err_utils import get_err_msg


@time_func
def main(fonts_dir: str, zip_file: str):
    """
    Create a zip file from the font files, to create a release archive.
    """
    fonts_dir = str(fonts_dir)
    zip_file = abspath(str(zip_file))

    try:
        if not isdir(fonts_dir):
            raise NotADirectoryError('"%s" is not a directory'
                                     % abspath(fonts_dir))

        sp.check_call(['zip', '-r', zip_file, fonts_dir])
        print('\nCreated font archive: "%s"' % zip_file, file=stderr)

    except (OSError, sp.SubprocessError) as err:
        print(get_err_msg(err, break_line=True),
              'Failed to create font archive: "%s"' % zip_file,
              sep='\n', file=stderr)


if __name__ == '__main__':
    # check command line arguments
    if len(argv) < 3:
        print('Usage: python3 %s <fonts directory> <zip file>'
              % __file__, file=stderr)
        exit(1)

    exit(main(*argv[1:3]))
