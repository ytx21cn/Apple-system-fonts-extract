import glob

from os.path import basename, splitext, abspath

from paths import safe_mkdir, source_files_path, converted_files_path
from unpack import dmg2img


def main():

    safe_mkdir(converted_files_path)

    dmgFiles = glob.glob('%s/*.dmg' % source_files_path)
    for file in dmgFiles:
        fontName = splitext(basename(file))[0]
        convertedFile = '%s/%s.img' % (converted_files_path, fontName)
        dmg2img(file, convertedFile)


if __name__ == '__main__':
    main()
