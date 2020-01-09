import glob
from os.path import basename, dirname
from tempfile import TemporaryDirectory
from shutil import copy

from unpack import dmg2img, unpack_7z
from paths import dmg_path, otf_path
from path_utils import safe_mkdir


def main():
    dmg_files = glob.glob('%s/**/*.dmg' % dmg_path, recursive=True)
    for dmg_file in dmg_files:
        with TemporaryDirectory() as temp_dir:
            # First, convert each dmg to img
            img_file = dmg2img(dmg_file, converted=temp_dir)

            # Then, for each img:

            # 1. unpack img, then we can see a single pkg file
            # we can also get the font name
            img_extracted_dir = unpack_7z(img_file, output_dir=temp_dir)
            pkg_file = glob.glob('%s/**/*.pkg' % img_extracted_dir, recursive=True)[0]
            font_name = basename(dirname(pkg_file))

            # 2. extract the pkg file, then we can see a single 'Payload~' file
            pkg_extracted_dir = unpack_7z(pkg_file)
            payload_file = glob.glob('%s/**/Payload~*' % pkg_extracted_dir, recursive=True)[0]

            # 3. extract the 'Payload~' file, then we can see the font files in otf format
            fonts_dir = unpack_7z(payload_file)
            font_files = glob.glob('%s/**/*.otf' % fonts_dir, recursive=True)

            # 4. copy the font files to the otf directory
            target_dir = '%s/%s' % (otf_path, font_name)
            safe_mkdir(target_dir)
            for font_file in font_files:
                copy(src=font_file, dst=target_dir)








if __name__ == '__main__':
    main()
