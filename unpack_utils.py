import subprocess as sp
from sys import stderr
from os.path import basename, splitext, dirname, abspath, isdir, join


# file extraction

def dmg2img(dmg_file: str, target: str = None):
    """
    Convert dmg to img.
    Note: This function uses the "dmg2img" command in the "dmg2img" package.
    Make sure that you have "dmg2img" package installed.

    :param dmg_file: the dmg file to be converted
    :param target: the output path / output img file
    :return: the actual path of the target file
    """

    header = '\n[DMG to IMG]'

    dmg_file = abspath(str(dmg_file))
    img_filename = '%s.img' % splitext(basename(dmg_file))[0]
    if target:
        target = abspath(str(target))
        if isdir(target):
            target = join(target, img_filename)
    else:
        target = abspath(join(dirname(dmg_file), img_filename))

    print(header, file=stderr)
    print('Converting "%s" to "%s"...' % (dmg_file, target), file=stderr)
    try:
        sp.call(['dmg2img', dmg_file, target])
        print(header, file=stderr)
        print('Converted "%s" to "%s"' % (dmg_file, target), file=stderr)
    except OSError:
        print('[ERROR] unable to convert dmg file: %s\n'
              'Please make sure that the dmg2img package is installed,'
              'and that the dmg file does exist.' % abspath(dmg_file),
              file=stderr)
        exit(1)

    return target


def unpack_7z(archive: str, output_dir: str = None):
    """
    Unpack 7z archive.
    Note: This function uses the "7z" command in "p7zip-full" package.
    Make sure that you have "p7zip-full" package installed.

    :param archive: the path to the archive to be extracted
    :param output_dir: the directory to output the extracted content
    :return: the actual output directory
    """

    header = '\n[Unpack 7z archive]'

    archive = abspath(str(archive))
    if output_dir:
        output_dir = abspath(str(output_dir))
    else:
        output_dir = abspath(dirname(archive))

    print(header, file=stderr)
    print('Unpacking "%s" to "%s"...' % (archive, output_dir), file=stderr)
    try:
        sp.call(['7z', 'x', archive, '-y', '-o%s' % output_dir])
        print(header, file=stderr)
        print('Unpacked "%s" to "%s"' % (archive, output_dir), file=stderr)
    except OSError:
        print('[ERROR] unable to extract file: %s\n'
              'Please ensure that the p7zip-full package is installed,'
              'and that the file to extract does exist.' % abspath(archive),
              file=stderr)
        exit(1)

    return output_dir
