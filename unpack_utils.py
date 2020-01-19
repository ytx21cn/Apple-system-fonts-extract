import subprocess as sp
from sys import stderr
from os.path import basename, splitext, dirname, abspath, isdir, join


# file extraction

def dmg2img(dmg_file: str, output: str = None):
    """
    Convert dmg to img.
    Note: This function uses the "dmg2img" command in the "dmg2img" package.
    Make sure that you have "dmg2img" package installed.

    :param dmg_file: the .dmg file to be converted
    :param output: the output path / output .img file
    :return: the absolute path of the output file
    """

    # set proper paths
    dmg_file = str(dmg_file)
    img_filename = '%s.img' % splitext(basename(dmg_file))[0]
    if output:
        output = str(output)
        if isdir(output):
            output = join(output, img_filename)
    else:
        output = join(dirname(dmg_file), img_filename)

    try:
        sp.call(['dmg2img', dmg_file, output])
    except OSError:
        print('[ERROR] unable to convert dmg file: "%s"\n'
              'Please make sure that the dmg2img package is installed,'
              'and that the .dmg file does exist.' % abspath(dmg_file),
              file=stderr)
        exit(1)

    return abspath(output)


def unpack_7z(archive: str, output_dir: str = None):
    """
    Unpack 7z archive.
    Note: This function uses the "7z" command in "p7zip-full" package.
    Make sure that you have "p7zip-full" package installed.

    :param archive: the path to the archive to be extracted
    :param output_dir: the directory to output the extracted content
    :return: the absolute path of the actual output directory
    """

    # set proper paths
    archive = str(archive)
    if output_dir:
        output_dir = str(output_dir)
    else:
        output_dir = dirname(archive)

    # unpack archive
    try:
        sp.call(['7z', 'x', archive, '-y', '-o%s' % output_dir])
    except OSError:
        print('[ERROR] unable to extract file: "%s"\n'
              'Please ensure that the p7zip-full package is installed,'
              'and that the file to extract does exist.' % abspath(archive),
              file=stderr)
        exit(1)

    return abspath(output_dir)
