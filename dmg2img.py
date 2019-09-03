import glob, subprocess as sp
from os.path import basename, splitext, abspath
from os import makedirs

from paths import makedirs, sourceFilesPath, convertedFilesPath

def main():

    makedirs(convertedFilesPath)

    dmgFiles = glob.glob('%s/*.dmg' % sourceFilesPath)
    for file in dmgFiles:
        fontName = splitext(basename(file))[0]
        convertedFile = '%s/%s.img' % (convertedFilesPath, fontName)
        try:
            sp.call(['dmg2img', file, convertedFile])
        except BaseException:
            print('[ERROR] unable to convert file: %s\nPlease make sure that the dmg2img package is installed, and the file exists.' % abspath(file))
            exit(1)

if __name__ == '__main__':
    main()
