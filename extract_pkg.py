import glob
from os import chdir
from os.path import dirname, basename, abspath
from shutil import copyfile

from paths import safe_mkdir, img_extracted_path, pkg_extracted_path
from unpack import unpack_xar


def main():
    """
    Extract *.pkg files
    pkg files are in xar format
    """

    safe_mkdir(pkg_extracted_path)

    base_dir = abspath(dirname(__file__))
    pkg_files = glob.glob('%s/**/*.pkg' % img_extracted_path, recursive=True)
    for file in pkg_files:
        font_name = basename(dirname(file))
        font_dir = abspath('%s/%s' % (pkg_extracted_path, font_name))
        safe_mkdir(font_dir)

        # copy each pkg file to destination directory
        # and extract it there
        dest_file = '%s/%s' % (font_dir, basename(file))
        copyfile(src=file, dst=dest_file)
        chdir(font_dir)
        unpack_xar(dest_file)
        chdir(base_dir)


if __name__ == '__main__':
    main()
