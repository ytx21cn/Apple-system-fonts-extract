from sys import argv, stderr

from path_utils import safe_remove
from timing_utils import time_func


@time_func
def main():
    """
    Remove the files generated from "make".
    The files and directories to remove are given in the command line argument.

    :return 0 on success
        1 if command line arguments are invalid
    """

    # check command line arguments
    if len(argv) < 2:
        print('Usage: python3 %s <path to remove> {paths to remove ...}'
              % __file__, file=stderr)
        return 1

    paths_to_remove = argv[1:]
    for path in paths_to_remove:
        safe_remove(path)

    return 0


if __name__ == '__main__':
    exit(main())
