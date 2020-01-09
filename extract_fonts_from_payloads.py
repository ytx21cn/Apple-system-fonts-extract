import glob, subprocess as sp
from os.path import basename, dirname, splitext, abspath

from paths import safe_mkdir, safe_remove, pkgExtractedPath, fontPath
from unpack import unpack_7z

def unpackPayload(payloadFile, outputDir='.'):
    copyTarget = '%s.7z.gz' % payloadFile
    sp.call(['cp', payloadFile, copyTarget])
    sp.call(['gunzip', copyTarget])
    unpack_7z('%s.7z' % payloadFile, outputDir)
    safe_remove('%s.7z' % payloadFile)

def main():
    payloadFiles = glob.glob('%s/**/Payload' % pkgExtractedPath, recursive=True)

    safe_mkdir(fontPath)

    for payloadFile in payloadFiles:
        fontName = splitext(basename(dirname(payloadFile)))[0]
        print('\n[Now copying font] %s' % fontName)

        payloadDir = abspath(dirname(payloadFile))
        tempPath = '%s/temp' % payloadDir

        unpackPayload(payloadFile, tempPath)
        fontTargetPath = '%s/%s' % (fontPath, fontName)
        safe_mkdir(fontTargetPath)

        otfFilesPath = '%s/**/*.otf' % tempPath
        otfFiles = glob.glob(otfFilesPath, recursive=True)
        for otfFile in otfFiles:
            sp.call(['cp', '-r', otfFile, fontTargetPath])


if __name__ == '__main__':
    main()
