import glob
import subprocess as sp
from os import chdir
from os.path import dirname, basename, abspath

from paths import safe_mkdir, img_extracted_path, pkg_extracted_path
from unpack import unpack_xar


def main():
    """
    Extract *.pkg files
    pkg files are in xar format
    """

    base_dir = abspath(dirname(__file__))

    safe_mkdir(pkg_extracted_path)

    pkg_files = glob.glob('%s/**/*.pkg' % img_extracted_path, recursive=True)
    for file in pkg_files:
        font_name = basename(dirname(file))
        font_dir = abspath('%s/%s' % (pkg_extracted_path, font_name))
        safe_mkdir(font_dir)

        sp.call(['cp', '-r', file, font_dir])
        file_to_extract = '%s/%s' % (font_dir, basename(file))
        chdir(font_dir)
        unpack_xar(file_to_extract)
        chdir(base_dir)


if __name__ == '__main__':
    main()
