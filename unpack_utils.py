import subprocess as sp
from sys import stderr
from os.path import basename, splitext, dirname, abspath, join

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
    # if output_path is specified, then use it
    # the output_path can either be a directory or a filename
    if output_path:
        output_path = str(output_path)
        # if extension of output_path is .img
        # then treat it as the output file
        if splitext(output_path)[1] == output_ext:
            output_dir = dirname(output_path)
        # otherwise, treat output_path as the output directory
        else:
            output_dir = output_path
            output_path = join(output_dir, img_filename)
    # if output_path is not specified
    # then use the directory of the .dmg file as output directory
    else:
        output_dir = dirname(dmg_file)
        output_path = join(output_dir, img_filename)

    output_path = abspath(output_path)

    # convert .dmg to .img
    try:
        print('\n[Converting from .dmg to .img...]',
              'Input file: "%s"' % dmg_file,
              'Output file: "%s"' % output_path,
              sep='\n', file=stderr)
        if safe_mkdir(output_dir) is None:
            raise OSError
        sp.check_call(['dmg2img', dmg_file, output_path], stdout=stderr)
        print('\n[Conversion completed]',
              'Output file: "%s"' % output_path,
              sep='\n', file=stderr)
        return output_path

    except (OSError, sp.SubprocessError) as err:
        print(get_err_msg(err),
              'Failed to convert "%s" to "%s".' % (dmg_file, output_path),
              'Please ensure that the "dmg2img" package is installed, '
              'both the input and output paths are valid, '
              'and you have proper permission.',
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

    # unpack archive
    try:
        print('\n[Unpacking archive...]',
              'Unpack from: "%s"' % archive,
              'Output directory: "%s"' % output_dir,
              sep='\n', file=stderr)
        if safe_mkdir(output_dir) is None:
            raise OSError
        sp.check_call(['7z', 'x', archive, '-y', '-o%s' % output_dir],
                      stdout=stderr)
        print('\n[Unpacking completed]',
              'Output directory: "%s"' % output_dir,
              sep='\n', file=stderr)
        return output_dir

    except (OSError, sp.SubprocessError) as err:
        print(get_err_msg(err),
              'Failed to extract file: "%s".' % archive,
              'Please ensure that the "p7zip-full" package is installed, '
              'both the archive and the output directory are valid, '
              'and you have proper permission.',
              sep='\n', file=stderr)
        return None
