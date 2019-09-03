import glob, subprocess as sp
from os.path import basename, splitext, abspath
from os import makedirs

from paths import makedirs, sourceFilesPath, convertedFilesPath
from unpack import dmg2img

def main():

    makedirs(convertedFilesPath)

    dmgFiles = glob.glob('%s/*.dmg' % sourceFilesPath)
    for file in dmgFiles:
        fontName = splitext(basename(file))[0]
        convertedFile = '%s/%s.img' % (convertedFilesPath, fontName)
        dmg2img(file, convertedFile)

if __name__ == '__main__':
    main()
