from os import mkdir
from os.path import abspath
from shutil import rmtree


def safe_mkdir(path):
    try:
        mkdir(path)
    except:
        pass


def safe_remove(path):
    try:
        rmtree(path, ignore_errors=True)
    except:
        pass


source_files_path = abspath('./dmg')
converted_files_path = abspath('./img')

img_extracted_path = abspath('./img_extracted')
pkg_extracted_path = abspath('./pkg_extracted')

font_path = abspath('./otf')


