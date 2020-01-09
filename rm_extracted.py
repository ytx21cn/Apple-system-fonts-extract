from paths import safe_remove, convertedFilesPath, imgExtractedPath, pkgExtractedPath


def main():
    for path in [convertedFilesPath, imgExtractedPath, pkgExtractedPath]:
        safe_remove(path)


if __name__ == '__main__':
    main()
