import subprocess as sp
from sys import stderr
from os import renames
from os.path import basename, splitext, dirname, abspath,\
    isdir, isfile, join

from path_utils import safe_create_file, safe_mkdir


# file extraction

def dmg2img(dmg_file: str, output: str = None) -> str or None:
    """
    Convert dmg to img.
    Note: This function uses the "dmg2img" command in the "dmg2img" package.
    Make sure that you have "dmg2img" package installed.

    :param dmg_file: the .dmg file to be converted.
    :param output: the output path / output .img file.
    :return: the absolute path of the output file,
        or None if failed to convert.
    """

    output_ext = '.img'

    # first check existence of the .dmg file to be converted
    try:
        assert dmg_file is not None, 'dmg_file is None'
        dmg_file = abspath(str(dmg_file))
        if not isfile(dmg_file):
            raise FileNotFoundError('File "%s" does not exist' % dmg_file)
        img_filename = splitext(basename(dmg_file))[0] + output_ext
    except (AssertionError, FileNotFoundError) as err:
        print('\n[%s]' % type(err).__name__, err, sep='\n', file=stderr)
        return None

    # set proper paths
    # handle different cases for output
    # if output is specified, then use it for the output file
    if output:
        output = str(output)
        # if output is an existing file, then overwrite it
        # also set the extension to .img
        if isfile(output):
            safe_create_file(output, overwrite=True)
            if not output.endswith(output_ext):
                output_with_proper_ext = splitext(output)[0] + output_ext
                renames(output, output_with_proper_ext)
                output = output_with_proper_ext
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
    # otherwise, use the filename of the .dmg
    # and change extension to .img
    else:
        output = join(dirname(dmg_file), img_filename)

    output = abspath(output)

    # convert .dmg to .img
    try:
        print('\n[Converting from .dmg to .img...]',
              'Input file: "%s"' % dmg_file,
              'Output file: "%s"' % output,
              sep='\n', file=stderr)
        sp.check_call(['dmg2img', dmg_file, output])
        print('\n[Conversion completed]',
              'Output file: "%s"' % output,
              sep='\n', file=stderr)
        return output

    except (OSError, sp.SubprocessError) as err:
        print('\n[%s]' % type(err).__name__, err,
              'Failed to convert "%s" to "%s".' % (dmg_file, output),
              'Please ensure that the "dmg2img" package is installed,'
              'and both the input and output paths are valid.',
              sep='\n', file=stderr)
        return None


def unpack_7z(archive: str, output_dir: str = None) -> str or None:
    """
    Unpack 7z archive.
    Note: This function uses the "7z" command in "p7zip-full" package.
    Make sure that you have "p7zip-full" package installed.

    :param archive: the path to the archive to be extracted.
    :param output_dir: the directory to output the extracted content.
    :return: the absolute path of the actual output directory,
        or None if failed to extract.
    """

    # first check existence of archive to be extracted
    try:
        assert archive is not None, 'archive is None'
        archive = abspath(str(archive))
        if not isfile(archive):
            raise FileNotFoundError('Archive "%s" does not exist')
    except (AssertionError, FileNotFoundError) as err:
        print('\n[%s]' % type(err).__name__, err, sep='\n', file=stderr)
        return None

    # set proper paths
    output_dir = str(output_dir) if output_dir else dirname(archive)
    output_dir = abspath(output_dir)
    safe_mkdir(output_dir)

    # unpack archive
    try:
        print('\n[Unpacking archive...]',
              'Unpack from: "%s"' % archive,
              'Output directory: "%s"' % output_dir,
              sep='\n', file=stderr)
        sp.check_call(['7z', 'x', archive, '-y', '-o%s' % output_dir])
        print('\n[Unpacking completed]',
              'Output directory: "%s"' % output_dir,
              sep='\n', file=stderr)
        return output_dir

    except (OSError, sp.SubprocessError) as err:
        print('\n[%s]' % type(err).__name__, err,
              'Failed to extract file: "%s".' % archive,
              'Please ensure that the "p7zip-full" package is installed,'
              'and both file to extract and the output directory are valid.',
              sep='\n', file=stderr)
        return None
