import subprocess as sp
from sys import stderr
from os import renames
from os.path import basename, splitext, dirname, abspath,\
    isdir, isfile, join

from err_utils import get_err_msg
from path_utils import check_file_exists, safe_mkdir


# file extraction

def dmg2img(dmg_file: str, output_path: str = None) -> str or None:
    """
    Convert dmg to img.
    Note: This function uses the "dmg2img" command in the "dmg2img" package.
    Make sure that you have "dmg2img" package installed.

    :param dmg_file: the .dmg file to be converted.
    :param output_path: the output directory / output .img file.
    :return: the absolute path of the output file,
        or None if failed to convert.
    """

    output_ext = '.img'

    # first check existence of the .dmg file to be converted
    dmg_file = '' if (dmg_file is None) else abspath(str(dmg_file))
    if not check_file_exists(dmg_file):
        return None

    # use the filename of the original .dmg file
    # to set the filename of the .img file
    img_filename = splitext(basename(dmg_file))[0] + output_ext

    # set proper output path
    # handle different cases for output path
    # if output is specified, then use it for the output file
    if output_path:
        output_path = str(output_path)
        # if output is an existing file, then overwrite it
        # also set the extension to .img
        if isfile(output_path):
            if not output_path.endswith(output_ext):
                output_with_proper_ext = splitext(output_path)[0] + output_ext
                try:
                    renames(output_path, output_with_proper_ext)
                    output_path = output_with_proper_ext
                except OSError as err:
                    print(get_err_msg(err), file=stderr)
                    return None
        # if output is an existing directory,
        # then create the output file in that directory
        elif isdir(output_path):
            output_dir = output_path
            output_path = join(output_dir, img_filename)
        # otherwise, need to create the directory to hold the output file
        else:
            # if output path ends with '.img'
            # then treat it as the target output file
            if output_path.endswith(output_ext):
                output_dir = dirname(output_path)
            # otherwise, treat it as the output directory
            else:
                output_dir = output_path
                output_path = join(output_dir, img_filename)
            try:
                assert safe_mkdir(output_dir) is not None,\
                    'Failed to create directory "%s"' % output_dir
            except AssertionError as err:
                print(get_err_msg(err), file=stderr)
                return None
    # otherwise, use the filename of the .dmg
    # and change extension to .img
    else:
        output_path = join(dirname(dmg_file), img_filename)

    output_path = abspath(output_path)

    # convert .dmg to .img
    try:
        print('\n[Converting from .dmg to .img...]',
              'Input file: "%s"' % dmg_file,
              'Output file: "%s"' % output_path,
              sep='\n', file=stderr)
        sp.check_call(['dmg2img', dmg_file, output_path], stdout=stderr)
        print('\n[Conversion completed]',
              'Output file: "%s"' % output_path,
              sep='\n', file=stderr)
        return output_path

    except (OSError, sp.SubprocessError) as err:
        print(get_err_msg(err),
              'Failed to convert "%s" to "%s".' % (dmg_file, output_path),
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
    archive = '' if (archive is None) else abspath(str(archive))
    if not check_file_exists(archive):
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
        sp.check_call(['7z', 'x', archive, '-y', '-o%s' % output_dir],
                      stdout=stderr)
        print('\n[Unpacking completed]',
              'Output directory: "%s"' % output_dir,
              sep='\n', file=stderr)
        return output_dir

    except (OSError, sp.SubprocessError) as err:
        print(get_err_msg(err),
              'Failed to extract file: "%s".' % archive,
              'Please ensure that the "p7zip-full" package is installed,'
              'and both file to extract and the output directory are valid.',
              sep='\n', file=stderr)
        return None
