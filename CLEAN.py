from sys import argv, stderr

from path_utils import safe_remove
from timing_utils import time_func


@time_func
def main():
    """
    Remove the generated otf files.
    The otf directory is given in the command line argument.

    :return 0 on success
        1 if command line arguments are invalid
    """

    if len(argv) < 2:
        print('Usage: python3 %s <directory to remove>' % __file__,
              file=stderr)
        return 1

    otf_path = argv[1]
    safe_remove(otf_path)
    return 0


if __name__ == '__main__':
    exit(main())
