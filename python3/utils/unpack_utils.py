import subprocess as sp
from sys import stderr
from os.path import basename, splitext, dirname, abspath, join

from utils.err_utils import get_err_msg
from utils.path_utils import check_file_exists, safe_mkdir
from utils.timing_utils import time_func


# file extraction utilities


@time_func
def dmg2img(dmg_file: str or None = None, output_path: str = None)\
        -> str or bool or None:
    """
    Convert dmg to img.
    Note: This function uses the "dmg2img" command in the "dmg2img" package.
    Make sure that you have "dmg2img" package installed.
    To perform a trial run, call this function without parameters.

    :param dmg_file: the .dmg file to be converted.
    :param output_path: the output directory / output .img file.
        If the output directory does not exist originally,
        then it will be created to contain the output file.
    :return:
        [Trial run] True if "dmg2img" command executes successfully,
            False otherwise;
        [Actual conversion] the absolute path of the output file,
            or None if failed to convert.
    """

    output_ext = '.img'
    convert_exec = 'dmg2img'

    # this part is for trial run: check if "dmg2img" is installed
    if dmg_file is None:
        try:
            sp.check_call(convert_exec, stdout=sp.DEVNULL)
            return True
        except OSError as err:
            print(get_err_msg(err),
                  'Please install the "dmg2img" package.',
                  sep='\n', file=stderr)
            return None

    dmg_file = abspath(str(dmg_file))

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
        if (not check_file_exists(dmg_file)) or \
                (safe_mkdir(output_dir) is None):
            raise OSError

        sp.check_call([convert_exec, dmg_file, output_path],
                      stdout=stderr)

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


@time_func
def unpack_7z(archive: str or None = None, output_dir: str = None)\
        -> str or None:
    """
    Unpack 7z archive.
    Note: This function uses the "7z" command in "p7zip-full" package.
    Make sure that you have "p7zip-full" package installed.
    To perform a trial run, call this function without parameters.

    :param archive: the path to the archive to be extracted.
    :param output_dir: the directory to output the extracted content.
    :return:
        [Trial run] True if "dmg2img" command executes successfully,
            False otherwise;
        [Actual conversion] the absolute path of the output directory,
            or None if failed to extract.
    """

    unpack_exec = '7z'

    # this part is for trial run: check if "p7zip-full" is installed
    if archive is None:
        try:
            sp.check_call(unpack_exec, stdout=sp.DEVNULL)
            return True
        except OSError as err:
            print(get_err_msg(err),
                  'Please install the "p7zip-full" package.',
                  sep='\n', file=stderr)
            return None

    # to begin unpacking the archive, first set proper paths
    archive = abspath(str(archive))
    output_dir = str(output_dir) if output_dir else dirname(archive)
    output_dir = abspath(output_dir)

    # unpack archive
    try:
        print('\n[Unpacking archive...]',
              'Unpack from: "%s"' % archive,
              'Output directory: "%s"' % output_dir,
              sep='\n', file=stderr)
        if (not check_file_exists(archive)) or \
                (safe_mkdir(output_dir) is None):
            raise OSError
        sp.check_call([unpack_exec, 'x', archive, '-y',
                       '-o%s' % output_dir], stdout=stderr)
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
