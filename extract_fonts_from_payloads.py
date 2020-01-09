import glob
import subprocess as sp
from os.path import basename, dirname, splitext
from shutil import copyfile
from tempfile import TemporaryDirectory

from paths import safe_mkdir, safe_remove, pkgExtractedPath, fontPath
from unpack import unpack_7z


def unpack_payload(payload_file, output_dir='.'):
    source = '%s.7z' % payload_file
    copy_target = '%s.gz' % source

    copyfile(src=payload_file, dst=copy_target)
    sp.call(['gunzip', '-f', copy_target])
    unpack_7z(source, output_dir)
    safe_remove(source)


def main():
    payload_files = glob.glob('%s/**/Payload' % pkgExtractedPath, recursive=True)

    safe_mkdir(fontPath)

    for payload_file in payload_files:
        font_name = splitext(basename(dirname(payload_file)))[0]
        font_target_path = '%s/%s' % (fontPath, font_name)
        safe_mkdir(font_target_path)

        print('\n[Now extracting font "%s"]' % font_name)

        with TemporaryDirectory() as temp_path:
            unpack_payload(payload_file, temp_path)
            otf_files = glob.glob('%s/**/*.otf' % temp_path, recursive=True)
            for otf_file in otf_files:
                copyfile(src=otf_file, dst='%s/%s.otf' % (font_target_path, basename(otf_file)))


if __name__ == '__main__':
    main()
