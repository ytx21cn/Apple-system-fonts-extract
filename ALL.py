from glob import glob
from os.path import basename, splitext, join
from tempfile import TemporaryDirectory
from sys import argv, stderr

from unpack_utils import dmg2img, unpack_7z
from move_file_utils import move_to_dir
from timing_utils import time_func


@time_func
def main():
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

    :return 0 on success
        1 if invalid command line arguments are specified
        -1 if "dmg2img" or "p7zip-full" or both are not installed
    """

    # command line argument check
    # set dmg and otf directories
    if len(argv) < 3:
        print('Usage: python3 %s <dmg directory> <fonts directory>' % __file__,
              '<dmg directory>: the directory with Apple\'s .dmg files',
              '<fonts directory>: the directory to output font files',
              sep='\n', file=stderr)
        return 1
    dmg_dir = argv[1]
    fonts_dir = argv[2]

    # do the trial run
    # to see if "dmg2img" and "p7zip" packages are both installed
    # if either or both of them are not installed, print error messages
    dmg2img_installed = dmg2img()
    p7zip_installed = unpack_7z()
    if not (dmg2img_installed and p7zip_installed):
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
            move_to_dir(src_file_list=src_font_files, dst_dir=target_dir)


if __name__ == '__main__':
    exit(main())
