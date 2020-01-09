import glob

from unpack import unpack_7z
from path_utils import safe_mkdir
from paths import converted_files_path, img_extracted_path


def main():
    safe_mkdir(img_extracted_path)

    # extract each img file, and put the extracted content in img_extracted_path
    img_files = glob.glob('%s/*.img' % converted_files_path)
    for file in img_files:
        unpack_7z(file, output_dir=img_extracted_path)


if __name__ == '__main__':
    main()
