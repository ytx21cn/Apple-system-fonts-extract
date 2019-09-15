import subprocess as sp
from paths import imgExtractedPath, pkgExtractedPath

def main():
    sp.call(['rm', '-r', imgExtractedPath, pkgExtractedPath])

if __name__ == '__main__':
    main()
