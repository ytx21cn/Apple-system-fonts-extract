import glob, subprocess as sp
from os.path import abspath

from paths import safe_mkdir, converted_files_path, img_extracted_path
from unpack import unpack_7z

def main():
    safe_mkdir(img_extracted_path)

    # extract each img file, and put the extracted content in img_extracted_path
    imgFiles = glob.glob('%s/*.img' % converted_files_path)
    for file in imgFiles:
        unpack_7z(file, output_dir=img_extracted_path)

if __name__ == '__main__':
    main()
