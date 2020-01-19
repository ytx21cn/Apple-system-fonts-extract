import subprocess as sp
from sys import stderr
from os.path import basename, splitext, dirname, abspath,\
    isdir, isfile, join

from path_utils import safe_create_file, safe_mkdir


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

    output_ext = '.img'

    # set proper paths
    dmg_file = abspath(str(dmg_file))
    img_filename = '%s%s' % (splitext(basename(dmg_file))[0], output_ext)
    # handle different cases for output
    # if output is specified
    if output:
        output = str(output)
        # if output is an existing file, then overwrite it
        if isfile(output):
            pass
        # if output is an existing directory,
        # then create the output file in that directory
        elif isdir(output):
            output = join(output, img_filename)
        # otherwise, need to create the directory to hold the output file
        else:
            # if output path ends with '.img'
            # then treat it as the target output file
            if output.endswith(output_ext):
                safe_create_file(output)
            # otherwise, treat it as the output directory
            else:
                output_dir = output
                output = join(output_dir, img_filename)
                safe_create_file(output)
    else:
        output = join(dirname(dmg_file), img_filename)
    output = abspath(output)

    # convert .dmg to .img
    try:
        print('\n[Converting from .dmg to .img...]', file=stderr)
        print('Input file: "%s"\nOutput file: "%s"' % (dmg_file, output),
              file=stderr)
        sp.call(['dmg2img', dmg_file, output])
        print('\n[Conversion completed]', file=stderr)
        print('Output file: "%s"' % output, file=stderr)
    except OSError:
        print('[ERROR] unable to convert dmg file: "%s"\n'
              'Please make sure that the dmg2img package is installed,'
              'and that the .dmg file does exist.' % abspath(dmg_file),
              file=stderr)
        exit(1)

    return output


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
    archive = abspath(str(archive))
    if output_dir:
        output_dir = str(output_dir)
    else:
        output_dir = dirname(archive)
    output_dir = abspath(output_dir)
    safe_mkdir(output_dir)

    # unpack archive
    try:
        print('\n[Unpacking archive...]', file=stderr)
        print('Unpack from: "%s"\nOutput directory: "%s"'
              % (archive, output_dir), file=stderr)
        sp.call(['7z', 'x', archive, '-y', '-o%s' % output_dir])
        print('\n[Unpacking completed]', file=stderr)
        print('Output directory: "%s"' % output_dir, file=stderr)
    except OSError:
        print('[ERROR] unable to extract file: "%s"\n'
              'Please ensure that the p7zip-full package is installed,'
              'and that the file to extract does exist.' % abspath(archive),
              file=stderr)
        exit(1)

    return output_dir
