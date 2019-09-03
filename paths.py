import subprocess as sp

def makedirs(path):
    sp.call(['mkdir', '-p', path])

def remove(path):
    sp.call(['rm', '-r', path])

sourceFilesPath = './dmg'
convertedFilesPath = './img'

imgExtractedPath = './img_extracted'
pkgExtractedPath = './pkg_extracted'

fontPath = './otf'


