from paths import converted_files_path, img_extracted_path, pkg_extracted_path
from path_utils import safe_remove


def main():
    for path in [converted_files_path, img_extracted_path, pkg_extracted_path]:
        safe_remove(path)


if __name__ == '__main__':
    main()
