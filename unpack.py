import subprocess as sp
from os.path import abspath

import clean_up

def dmg2img(file, convertedFile=None):
    try:
        sp.call(['dmg2img', file, convertedFile])
    except BaseException:
        print('[ERROR] unable to convert file: %s\nPlease make sure that the dmg2img package is installed, and the file exists.' % abspath(file))
        clean_up.main()
        exit(1)

def unpackXar(file):
    try:
        sp.call(['xar', '-xf', file])
    except BaseException:
        print('[ERROR] Unable to extract file: %s\nPlease make sure that the file exists, and install xar from http://bit.ly/archive-xar.' % abspath(file))
        clean_up.main()
        exit(1)

def unpack7z(file, outputDir = '.'):
    try:
        sp.call(['7z', 'x', file, '-y', '-o%s' % outputDir])
    except BaseException:
        print('[ERROR] unable to extract file: %s\nPlease install the p7zip-full package.' % abspath(file))
        clean_up.main()
        exit(1)

