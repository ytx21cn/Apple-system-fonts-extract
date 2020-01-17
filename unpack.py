import subprocess as sp
from sys import stderr
from os.path import basename, splitext, dirname, abspath, isdir


# file extraction

def dmg2img(dmg_file: str, converted: str = None):
    """
    Convert dmg to img.
    Note: This function uses the 'dmg2img' command from the 'dmg2img' package.

    :param dmg_file: the dmg file to be converted
    :param converted: the output path / output img file
    :return: the actual path of the converted file
    """

    dmg_file = abspath(str(dmg_file))
    img_filename = '%s.img' % splitext(basename(dmg_file))[0]
    if converted:
        converted = abspath(str(converted))
        if isdir(converted):
            converted = '%s/%s' % (converted, img_filename)
    else:
        converted = '%s/%s' % (dirname(dmg_file), img_filename)
        converted = abspath(converted)

    try:
        sp.call(['dmg2img', dmg_file, converted])
    except:
        print('[ERROR] unable to convert dmg file: %s\n'
              'Please make sure that the dmg2img package is installed,'
              'and that the dmg file does exist.' % abspath(dmg_file),
              file=stderr)
        exit(1)

    return converted


def unpack_7z(archive: str, output_dir: str = None):
    """
    Unpack 7z archive.
    Note: This function uses the '7z' command in 'p7zip-full' package.

    :param archive: the path to the archive to be extracted
    :param output_dir: the directory to output the extracted content
    :return: the actual output directory
    """

    archive = abspath(str(archive))
    if output_dir:
        output_dir = abspath(str(output_dir))
    else:
        output_dir = abspath(dirname(archive))

    try:
        sp.call(['7z', 'x', archive, '-y', '-o"%s"' % output_dir])
    except:
        print('[ERROR] unable to extract file: %s\n'
              'Please ensure that the p7zip-full package is installed,'
              'and that the file to extract does exist.' % abspath(archive),
              file=stderr)
        exit(1)

    return output_dir
