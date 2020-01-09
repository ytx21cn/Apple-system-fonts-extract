from path_utils import safe_remove
from paths import otf_path


def main():
    safe_remove(otf_path)


if __name__ == '__main__':
    main()
