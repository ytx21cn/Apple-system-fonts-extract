from sys import argv, stderr
from utils.font_info import FontInfo


def main(font_path: str):
    """Show the information of a font file."""
    font_path = str(font_path)
    font = FontInfo(font_path)
    print(font)


if __name__ == '__main__':
    # check arguments
    if len(argv) < 2:
        print('Usage: python3 %s <font path>' % __file__, file=stderr)
        exit(1)
    main(argv[1])
