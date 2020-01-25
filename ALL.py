import glob
from os.path import basename, splitext, join
from tempfile import TemporaryDirectory

from paths import dmg_path, otf_path
from unpack_utils import dmg2img, unpack_7z
from move_file_utils import move_to_dir
from timing_utils import time_func


def main():
    """
    This program extracts the Apple fonts (*.otf) from the dmg disk images.
    Apple fonts:
    1. SF Pro
    2. SF Compact
    3. SF Mono
    4. New York
    Download link: https://developer.apple.com/fonts/

    Two packages are required for the extraction:
    1. dmg2img - convert Apple .dmg files to .img files
    2. p7zip-full - extract font files from the converted .img files
    """

    # first, do the trial run
    # to see if "dmg2img" and "p7zip" are both installed
    dmg2img_installed = dmg2img()
    p7zip_installed = unpack_7z()
    if not (dmg2img_installed and p7zip_installed):
        return -1

    dmg_files = glob.glob(join(dmg_path, '**/*.dmg'), recursive=True)
    for dmg_file in dmg_files:
        with TemporaryDirectory() as temp_dir:

            # First, convert each dmg to img
            font_name = splitext(basename(dmg_file))[0]
            img_file = dmg2img(dmg_file, output_path=temp_dir)

            # Then, for each .img file:

            # 1. unpack .img
            # then we can see a single .pkg file
            img_extracted_dir = unpack_7z(img_file)
            pkg_file = glob.glob(join(img_extracted_dir, '**/*.pkg'),
                                 recursive=True)[0]

            # 2. extract the .pkg file
            # then we can see a single "Payload~" file
            pkg_extracted_dir = unpack_7z(pkg_file)
            payload_file = glob.glob(join(pkg_extracted_dir, '**/Payload~'),
                                     recursive=True)[0]

            # 3. extract the "Payload~" file
            # then we can see the font files in .otf format
            src_fonts_dir = unpack_7z(payload_file)
            src_font_files = glob.glob(join(src_fonts_dir, '**/*.otf'),
                                       recursive=True)

            # 4. move the font files from the temporary directory
            # to the target directory
            target_dir = join(otf_path, font_name)
            move_to_dir(src_file_list=src_font_files, dst_dir=target_dir)


if __name__ == '__main__':
    exit(time_func(main))
