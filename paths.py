import subprocess as sp
from os.path import abspath

def makedirs(path):
    sp.call(['mkdir', '-p', path])

def remove(path):
    sp.call(['rm', '-r', path])

sourceFilesPath = abspath('./dmg')
convertedFilesPath = abspath('./img')

imgExtractedPath = abspath('./img_extracted')
pkgExtractedPath = abspath('./pkg_extracted')

fontPath = abspath('./otf')


