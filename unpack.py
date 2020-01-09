import subprocess as sp
from os.path import abspath

import rm_extracted


# file extraction

def dmg2img(file: str, converted_file: str = None):
    """
    Convert dmg to img.
    This function uses the 'dmg2img' command from the 'dmg2img' package.
    """

    file = abspath(str(file))
    if converted_file:
        converted_file = abspath(str(converted_file))

    try:
        sp.call(['dmg2img', file, converted_file])
    except:
        print('[ERROR] unable to convert file: %s\n'
              'Please make sure that the dmg2img package is installed,'
              'and that the file exists.' % abspath(file))
        rm_extracted.main()
        exit(1)


def unpack_7z(file: str, output_dir: str = '.'):
    """
    Unpack 7z files.
    This function uses the '7z' command in 'p7zip-full' package.
    """

    file = abspath(str(file))
    output_dir = abspath(str(output_dir))
    try:
        sp.call(['7z', 'x', file, '-y', '-o%s' % output_dir])
    except:
        print('[ERROR] unable to extract file: %s\nPlease install the p7zip-full package.' % abspath(file))
        rm_extracted.main()
        exit(1)
