import subprocess as sp
from os.path import abspath

import rm_extracted


def dmg2img(file, convertedFile=None):
    if convertedFile:
        convertedFile = str(convertedFile)

    try:
        sp.call(['dmg2img', file, convertedFile])
    except:
        print('[ERROR] unable to convert file: %s\n'
              'Please make sure that the dmg2img package is installed,'
              'and that the file exists.' % abspath(file))
        rm_extracted.main()
        exit(1)


def unpack_xar(file):
    try:
        sp.call(['xar', '-xf', file])
    except:
        print('[ERROR] Unable to extract file: %s\n'
              'Please make sure that the file exists, '
              'and install xar from https://bit.ly/archive-xar.' % abspath(file))
        rm_extracted.main()
        exit(1)


def unpack_7z(file, output_dir ='.'):
    try:
        sp.call(['7z', 'x', file, '-y', '-o%s' % output_dir])
    except:
        print('[ERROR] unable to extract file: %s\nPlease install the p7zip-full package.' % abspath(file))
        rm_extracted.main()
        exit(1)

