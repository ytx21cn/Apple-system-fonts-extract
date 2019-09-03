import glob, subprocess as sp
from os.path import abspath

from paths import makedirs, convertedFilesPath, imgExtractedPath
from unpack import unpack7z

def main():
    makedirs(imgExtractedPath)

    # extract each img file, and put the extracted content in imgExtractedPath
    imgFiles = glob.glob('%s/*.img' % convertedFilesPath)
    for file in imgFiles:
        unpack7z(file, imgExtractedPath)

if __name__ == '__main__':
    main()
