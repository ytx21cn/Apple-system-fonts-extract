import rm_extracted
from paths import safe_remove, fontPath


def main():
    safe_remove(fontPath)
    rm_extracted.main()


if __name__ == '__main__':
    main()
