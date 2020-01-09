import subprocess as sp
import os
from os.path import abspath
from shutil import rmtree

import rm_extracted


# file / directory utils

def safe_mkdir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


def safe_remove(path):
    rmtree(path, ignore_errors=True)


# file extraction utils

def dmg2img(file, converted_file=None):
    if converted_file:
        converted_file = str(converted_file)

    try:
        sp.call(['dmg2img', file, converted_file])
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


def unpack_7z(file, output_dir='.'):
    output_dir = str(output_dir)
    try:
        sp.call(['7z', 'x', file, '-y', '-o%s' % output_dir])
    except:
        print('[ERROR] unable to extract file: %s\nPlease install the p7zip-full package.' % abspath(file))
        rm_extracted.main()
        exit(1)
