import glob
import subprocess as sp
from os.path import abspath, basename, dirname, splitext
from shutil import copyfile
from tempfile import TemporaryDirectory

from unpack import unpack_7z
from path_utils import safe_mkdir, safe_remove
from paths import pkg_extracted_path, font_path


def unpack_payload(payload_file: str, output_dir: str = '.'):
    payload_file = abspath(str(payload_file))
    output_dir = abspath(str(output_dir))
    unpack_7z(payload_file, output_dir=output_dir)


def main():
    payload_files = glob.glob('%s/**/Payload~' % pkg_extracted_path, recursive=True)

    safe_mkdir(font_path)

    for payload_file in payload_files:
        font_name = splitext(basename(dirname(payload_file)))[0]
        font_target_path = '%s/%s' % (font_path, font_name)
        safe_mkdir(font_target_path)

        print('\n[Now extracting font "%s"]' % font_name)

        with TemporaryDirectory() as temp_path:
            unpack_payload(payload_file, temp_path)
            otf_files = glob.glob('%s/**/*.otf' % temp_path, recursive=True)
            for otf_file in otf_files:
                copyfile(src=otf_file, dst='%s/%s.otf' % (font_target_path, basename(otf_file)))


if __name__ == '__main__':
    main()
