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


sourceFilesPath = abspath('./dmg')
convertedFilesPath = abspath('./img')

imgExtractedPath = abspath('./img_extracted')
pkgExtractedPath = abspath('./pkg_extracted')

fontPath = abspath('./otf')


