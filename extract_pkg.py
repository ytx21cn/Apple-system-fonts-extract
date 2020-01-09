import glob
from os.path import dirname, basename, abspath
from shutil import copyfile

from unpack import unpack_7z
from path_utils import safe_mkdir
from paths import img_extracted_path, pkg_extracted_path


def main():
    """
    Extract *.pkg files
    pkg files are in xar format
    """

    safe_mkdir(pkg_extracted_path)

    pkg_files = glob.glob('%s/**/*.pkg' % img_extracted_path, recursive=True)
    for file in pkg_files:
        font_name = basename(dirname(file))
        font_dir = abspath('%s/%s' % (pkg_extracted_path, font_name))
        safe_mkdir(font_dir)

        # copy each pkg file to destination directory
        # and extract it there
        dst_file = '%s/%s' % (font_dir, basename(file))
        copyfile(src=file, dst=dst_file)
        unpack_7z(dst_file, output_dir=font_dir)


if __name__ == '__main__':
    main()
