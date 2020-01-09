import glob, subprocess as sp
from os import chdir
from os.path import dirname, basename, abspath

from paths import safe_mkdir, img_extracted_path, pkg_extracted_path
from unpack import unpackXar

def main():
    baseDir = abspath('.')

    safe_mkdir(pkg_extracted_path)

    pkgFiles = glob.glob('%s/**/*.pkg' % img_extracted_path, recursive=True)
    for file in pkgFiles:
        # pkg files are in xar format
        # extract the pkg for each font in a separate directory

        fontName = basename(dirname(file))
        fontDir = abspath('%s/%s' % (pkg_extracted_path, fontName))
        safe_mkdir(fontDir)

        sp.call(['cp', '-r', file, fontDir])
        fileToExtract = '%s/%s' % (fontDir, basename(file))
        chdir(fontDir)
        unpackXar(fileToExtract)
        chdir(baseDir)

        pass

if __name__ == '__main__':
    main()
