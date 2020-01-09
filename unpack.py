import subprocess as sp
from os.path import abspath

import rm_extracted


# file extraction

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


def unpack_xar(file: str, output_dir: str = '.'):
    file = abspath(str(file))
    output_dir = abspath(str(output_dir))
    try:
        sp.call(['xar', '-xf', file], cwd=output_dir)
    except:
        print('[ERROR] Unable to extract file: %s\n'
              'Please make sure that the file exists, '
              'and install xar from https://bit.ly/archive-xar.' % file)
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
