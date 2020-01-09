import rm_extracted
from paths import safe_remove, font_path


def main():
    safe_remove(font_path)
    rm_extracted.main()


if __name__ == '__main__':
    main()
