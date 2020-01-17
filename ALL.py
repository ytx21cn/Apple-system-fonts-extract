import glob
from sys import stderr
from os.path import basename, splitext, abspath
from tempfile import TemporaryDirectory
from shutil import copy

from unpack import dmg2img, unpack_7z
from paths import dmg_path, otf_path
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
    """
    dmg_files = glob.glob('%s/**/*.dmg' % dmg_path, recursive=True)
    for dmg_file in dmg_files:
        with TemporaryDirectory() as temp_dir:
            # First, convert each dmg to img
            font_name = splitext(basename(dmg_file))[0]
            img_file = dmg2img(dmg_file, converted=temp_dir)

            # Then, for each img:

            # 1. unpack img, then we can see a single pkg file
            img_extracted_dir = unpack_7z(img_file)
            pkg_file = glob.glob('%s/**/*.pkg' % img_extracted_dir, recursive=True)[0]

            # 2. extract the pkg file, then we can see a single 'Payload~' file
            pkg_extracted_dir = unpack_7z(pkg_file)
            payload_file = glob.glob('%s/**/Payload~' % pkg_extracted_dir, recursive=True)[0]

            # 3. extract the 'Payload~' file, then we can see the font files in otf format
            fonts_dir = unpack_7z(payload_file)
            font_files = glob.glob('%s/**/*.otf' % fonts_dir, recursive=True)

            # 4. copy the font files to the otf directory
            target_dir = abspath('%s/%s' % (otf_path, font_name))
            safe_mkdir(target_dir)
            for font_file in font_files:
                copy(src=font_file, dst=target_dir)
            print('\nCopied %s font files to "%s"' % (len(font_files), target_dir), file=stderr)


if __name__ == '__main__':
    main()
