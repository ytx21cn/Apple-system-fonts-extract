from glob import glob
from os.path import isfile, isdir, basename, dirname, splitext,\
    abspath, join
from tempfile import TemporaryDirectory
from sys import argv, stderr

from utils.unpack import dmg2img, unpack_7z
from utils.move_files import move_to_dir
from utils.timing import time_func


def check_dirs(dmg_dir: str, fonts_dir: str) -> bool:
    """
    Check if input and output directories are valid.
    :param dmg_dir: the directory containing Apple's .dmg files.
    :param fonts_dir: the directory to output fonts.
    :return: True if both arguments are valid directories;
        False otherwise.
    """

    dmg_dir = abspath(str(dmg_dir))
    fonts_dir = abspath(str(fonts_dir))

    if not isdir(dmg_dir):
        print(f'Error: "{dmg_dir}" is not a valid input directory',
              file=stderr)
        return False
    if (not isdir(dirname(fonts_dir))) or isfile(fonts_dir):
        print(f'Error: "{fonts_dir}" is not a valid output directory', file=stderr)
        return False

    return True


@time_func
def main(dmg_dir: str, fonts_dir: str):
    """
    This program extracts the Apple fonts (*.otf) from the dmg disk images.
    Apple fonts:
    1. SF Pro
    2. SF Compact
    3. SF Mono
    4. New York
    Download link: https://developer.apple.com/fonts/

    The dmg directory (for Apple's source images)
    and the otf directory (for output fonts)
    are specified by command-line arguments.

    Two packages are required for the extraction:
    1. dmg2img - convert Apple .dmg files to .img files
    2. p7zip-full - extract font files from the converted .img files

    :return None on success
        -1 if target directories are invalid, or if "dmg2img" or "p7zip-full" or both are not installed
    """

    # set dmg and otf directories
    # check if input and output directories are valid
    dmg_dir = abspath(str(dmg_dir))
    fonts_dir = abspath(str(fonts_dir))
    io_dirs_valid = check_dirs(dmg_dir, fonts_dir)

    # do the trial run
    # check if "dmg2img" and "p7zip" packages are both installed
    # if either or both of them are not installed, print error messages
    dmg2img_installed = dmg2img()
    p7zip_installed = unpack_7z()

    if not (io_dirs_valid and dmg2img_installed and p7zip_installed):
        return -1

    # if trial run succeeded, start the conversion process
    dmg_files = glob(join(dmg_dir, '**/*.dmg'), recursive=True)
    for dmg_file in dmg_files:
        with TemporaryDirectory() as temp_dir:
            # first, convert each dmg to img
            font_name = splitext(basename(dmg_file))[0]
            img_file = dmg2img(dmg_file, output_path=temp_dir)

            # then, for each .img file:

            # 1. unpack .img
            # then we can see a single .pkg file
            img_extracted_dir = unpack_7z(img_file)
            pkg_file = glob(join(img_extracted_dir, '**/*.pkg'),
                            recursive=True)[0]

            # 2. extract the .pkg file
            # then we can see a single "Payload~" file
            pkg_extracted_dir = unpack_7z(pkg_file)
            payload_file = glob(join(pkg_extracted_dir, '**/Payload~'),
                                recursive=True)[0]

            # 3. extract the "Payload~" file
            # then we can see the font files in .otf format
            src_fonts_dir = unpack_7z(payload_file)
            src_font_files = glob(join(src_fonts_dir, '**/*.otf'),
                                  recursive=True)

            # 4. move the font files from the temporary directory
            # to the target directory
            target_dir = join(fonts_dir, font_name)
            move_to_dir(src_file_list=src_font_files, dest_dir=target_dir)


if __name__ == '__main__':
    # check command line arguments
    if len(argv) < 3:
        print('Usage: python3 %s <dmg directory> <fonts directory>'
              % __file__,
              '<dmg directory>: the directory with Apple\'s .dmg files',
              '<fonts directory>: the directory to output font files',
              sep='\n', file=stderr)
        exit(1)

    exit(main(*argv[1:3]))
