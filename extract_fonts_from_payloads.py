import glob
import subprocess as sp
from os.path import basename, dirname, splitext, abspath
from shutil import copyfile

from paths import safe_mkdir, safe_remove, pkgExtractedPath, fontPath
from unpack import unpack_7z


def unpack_payload(payload_file, output_dir='.'):
    source = '%s.7z' % payload_file
    copy_target = '%s.gz' % source

    copyfile(src=payload_file, dst=copy_target)
    sp.call(['gunzip', copy_target])
    unpack_7z(source, output_dir)
    safe_remove(source)


def main():
    payloadFiles = glob.glob('%s/**/Payload' % pkgExtractedPath, recursive=True)

    safe_mkdir(fontPath)

    for payloadFile in payloadFiles:
        fontName = splitext(basename(dirname(payloadFile)))[0]
        print('\n[Now copying font] %s' % fontName)

        payloadDir = abspath(dirname(payloadFile))
        tempPath = '%s/temp' % payloadDir

        unpack_payload(payloadFile, tempPath)
        fontTargetPath = '%s/%s' % (fontPath, fontName)
        safe_mkdir(fontTargetPath)

        otfFilesPath = '%s/**/*.otf' % tempPath
        otfFiles = glob.glob(otfFilesPath, recursive=True)
        for otfFile in otfFiles:
            sp.call(['cp', '-r', otfFile, fontTargetPath])


if __name__ == '__main__':
    main()
