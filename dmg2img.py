import glob

from os.path import basename, splitext, abspath

from paths import safe_mkdir, sourceFilesPath, convertedFilesPath
from unpack import dmg2img


def main():

    safe_mkdir(convertedFilesPath)

    dmgFiles = glob.glob('%s/*.dmg' % sourceFilesPath)
    for file in dmgFiles:
        fontName = splitext(basename(file))[0]
        convertedFile = '%s/%s.img' % (convertedFilesPath, fontName)
        dmg2img(file, convertedFile)


if __name__ == '__main__':
    main()
