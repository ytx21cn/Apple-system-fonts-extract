from sys import argv, stderr

from path_utils import safe_remove
from timing_utils import time_func


@time_func
def main(paths_to_remove: list):
    """
    Remove the files generated from "make".
    The files and directories to remove are given in the command line argument.
    """

    for path in paths_to_remove:
        safe_remove(path)


if __name__ == '__main__':
    # check command line arguments
    if len(argv) < 2:
        print('Usage: python3 %s <path to remove> {paths to remove ...}'
              % __file__, file=stderr)
        exit(1)

    exit(main(argv[1:]))
