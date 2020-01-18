import glob
from sys import stderr
from os.path import basename, dirname, splitext, abspath, join
from tempfile import TemporaryDirectory
from shutil import move

from unpack import dmg2img, unpack_7z
from paths import project_root, dmg_path, otf_path
from path_utils import safe_mkdir
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

    dmg_files = glob.glob('%s/**/*.dmg' % dmg_path, recursive=True)
    for dmg_file in dmg_files:
        with TemporaryDirectory(dir=dirname(project_root)) as temp_dir:
            # First, convert each dmg to img
            font_name = splitext(basename(dmg_file))[0]
            img_file = dmg2img(dmg_file, target=temp_dir)
            img_file = abspath(str(img_file))

            # Then, for each img:

            # 1. unpack img, then we can see a single pkg file
            img_extracted_dir = \
                time_func(unpack_7z, img_file,
                          start_msg='Unpacking "%s"...' % img_file,
                          end_msg='Unpacked %s' % img_file)
            pkg_file = glob.glob('%s/**/*.pkg' % img_extracted_dir, recursive=True)[0]
            pkg_file = abspath(str(pkg_file))
            print('\nExtracted .pkg file: "%s"' % pkg_file,
                  file=stderr)

            # 2. extract the pkg file, then we can see a single 'Payload~' file
            pkg_extracted_dir = \
                time_func(unpack_7z, pkg_file,
                          start_msg='Unpacking "%s"' % pkg_file,
                          end_msg='"%s" extracted' % pkg_file)
            payload_file = glob.glob('%s/**/Payload~' % pkg_extracted_dir, recursive=True)[0]
            payload_file = abspath(str(payload_file))
            print('\nExtracted "Payload~" file: "%s"' % payload_file,
                  file=stderr)

            # 3. extract the 'Payload~' file, then we can see the font files in otf format
            src_fonts_dir = \
                time_func(unpack_7z, payload_file,
                          start_msg='Unpacking "%s"' % payload_file,
                          end_msg='"%s" extracted' % payload_file)
            src_fonts_dir = abspath(str(src_fonts_dir))
            src_font_files = glob.glob('%s/**/*.otf' % src_fonts_dir, recursive=True)
            num_font_files = len(src_font_files)
            print("\nExtracted %d font files to: %s"
                  % (num_font_files, src_fonts_dir),
                  file=stderr)

            # 4. move the font files from the temporary directory to the otf directory
            target_dir = abspath(join(otf_path, font_name))
            safe_mkdir(target_dir)

            print('\n[Moving files]', file=stderr)
            for src_font_file in src_font_files:
                # overwrite the target if it already exists
                dst_font_file = join(target_dir, basename(src_font_file))
                move(src=src_font_file, dst=dst_font_file)
            print('Moved %d font files into "%s"'
                  % (len(src_font_files), target_dir),
                  file=stderr)


if __name__ == '__main__':
    time_func(main)
