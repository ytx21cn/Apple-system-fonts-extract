import glob, subprocess as sp
from os.path import abspath

from paths import makedirs, convertedFilesPath, imgExtractedPath
from unpack_7z import unpack7z

def main():
    makedirs(imgExtractedPath)

    # extract each img file, and put the extracted content in imgExtractedPath
    imgFiles = glob.glob('%s/*.img' % convertedFilesPath)
    for file in imgFiles:
        try:
            unpack7z(file, imgExtractedPath)
        except BaseException:
            print('[ERROR] unable to extract file: %s\nPlease install the p7zip-full package.' % abspath(file))
            exit(1)

if __name__ == '__main__':
    main()
