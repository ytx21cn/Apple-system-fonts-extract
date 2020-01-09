import glob, subprocess as sp
from os.path import abspath

from paths import safe_mkdir, convertedFilesPath, imgExtractedPath
from unpack import unpack_7z

def main():
    safe_mkdir(imgExtractedPath)

    # extract each img file, and put the extracted content in imgExtractedPath
    imgFiles = glob.glob('%s/*.img' % convertedFilesPath)
    for file in imgFiles:
        unpack_7z(file, imgExtractedPath)

if __name__ == '__main__':
    main()
