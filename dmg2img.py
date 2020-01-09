import glob
from os.path import basename, splitext

from unpack import dmg2img
from path_utils import safe_mkdir
from paths import source_files_path, converted_files_path


def main():
    """
    Convert dmg files to img files
    """

    safe_mkdir(converted_files_path)

    dmg_files = glob.glob('%s/*.dmg' % source_files_path)
    for file in dmg_files:
        font_name = splitext(basename(file))[0]
        converted_file = '%s/%s.img' % (converted_files_path, font_name)
        dmg2img(file, converted_file)


if __name__ == '__main__':
    main()
