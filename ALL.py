import glob
from sys import stderr
from os.path import basename, dirname, splitext, abspath, join
from tempfile import TemporaryDirectory
from shutil import move
from time import time

from unpack import dmg2img, unpack_7z
from paths import project_root, dmg_path, otf_path
from path_utils import safe_mkdir


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

    dmg_files = glob.glob('%s/**/*.dmg' % dmg_path, recursive=True)
    for dmg_file in dmg_files:
        with TemporaryDirectory(dir=dirname(project_root)) as temp_dir:
            # First, convert each dmg to img
            font_name = splitext(basename(dmg_file))[0]
            img_file = dmg2img(dmg_file, target=temp_dir)

            # Then, for each img:

            # 1. unpack img, then we can see a single pkg file
            img_extracted_dir = unpack_7z(img_file)
            pkg_file = glob.glob('%s/**/*.pkg' % img_extracted_dir, recursive=True)[0]

            # 2. extract the pkg file, then we can see a single 'Payload~' file
            pkg_extracted_dir = unpack_7z(pkg_file)
            payload_file = glob.glob('%s/**/Payload~' % pkg_extracted_dir, recursive=True)[0]

            # 3. extract the 'Payload~' file, then we can see the font files in otf format
            src_fonts_dir = unpack_7z(payload_file)
            src_font_files = glob.glob('%s/**/*.otf' % src_fonts_dir, recursive=True)

            # 4. move the font files from the temporary directory to the otf directory
            target_dir = abspath(join(otf_path, font_name))
            safe_mkdir(target_dir)

            print('\n[Moving files]', file=stderr)
            move_start_time = time()
            for src_font_file in src_font_files:
                # overwrite the target if it already exists
                dst_font_file = join(target_dir, basename(src_font_file))
                move(src=src_font_file, dst=dst_font_file)
            move_total_time = time() - move_start_time
            print('Moved %s font files into "%s" in %.3f seconds' % (len(src_font_files), target_dir, move_total_time), file=stderr)


if __name__ == '__main__':
    main()
