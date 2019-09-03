import glob, subprocess as sp
from os import chdir
from os.path import dirname, basename, abspath

from paths import makedirs, imgExtractedPath, pkgExtractedPath
from unpack import unpackXar

def main():
    baseDir = abspath('.')

    makedirs(pkgExtractedPath)

    pkgFiles = glob.glob('%s/**/*.pkg' % imgExtractedPath, recursive=True)
    for file in pkgFiles:
        # pkg files are in xar format
        # extract the pkg for each font in a separate directory

        fontName = basename(dirname(file))
        fontDir = abspath('%s/%s' % (pkgExtractedPath, fontName))
        makedirs(fontDir)

        sp.call(['cp', '-r', file, fontDir])
        fileToExtract = '%s/%s' % (fontDir, basename(file))
        chdir(fontDir)
        unpackXar(fileToExtract)
        chdir(baseDir)

        pass

if __name__ == '__main__':
    main()
