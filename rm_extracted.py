from paths import safe_remove, converted_files_path, img_extracted_path, pkg_extracted_path


def main():
    for path in [converted_files_path, img_extracted_path, pkg_extracted_path]:
        safe_remove(path)


if __name__ == '__main__':
    main()
