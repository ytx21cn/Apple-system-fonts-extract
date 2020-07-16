# Get the information of a font file

from sys import argv, stderr
from os.path import abspath

try:
    from fontTools.ttLib import TTFont, TTLibError
except (ImportError, ModuleNotFoundError):
    pkg_name = 'fonttools'
    print('ERROR: package "%s" not installed' % pkg_name,
          'You may install it by typing:',
          'sudo pip3 install %s' % pkg_name,
          sep='\n', file=stderr)


class FontInfo:
    """
    This class stores the name information of a font file.
    """

    def __init__(self, font_path: str):
        try:
            # initialize font
            font_path = abspath(str(font_path))
            self.font_path = font_path
            font = TTFont(self.font_path)

            # save "name" table information into a dictionary
            name_table = font.get('name').names
            self.name_table_dict = {}
            name_table_dict = self.name_table_dict
            for record in name_table:
                assert record.__class__.__name__ == 'NameRecord'
                name_id = record.nameID
                name_table_dict[name_id] = record

            # save essential information from the "name" table
            # for the name ID codes, visit https://docs.microsoft.com/en-us/typography/opentype/spec/name#name-ids
            self.copyright = name_table_dict.get(0)
            self.family_name = name_table_dict.get(16) \
                or name_table_dict.get(1)
            self.subfamily_name = name_table_dict.get(17) \
                or name_table_dict.get(2)
            self.postscript_name = name_table_dict.get(6)

            # save "OS/2" table information
            # for the OS/2 table, visit: https://docs.microsoft.com/en-us/typography/opentype/spec/os2
            os2_table = font.get('OS/2')
            self.font_weight = os2_table.usWeightClass
            self.font_width = os2_table.usWidthClass

        except OSError:
            print('[ERROR] font file "%s" does not exist' % font_path,
                  file=stderr)
            exit(-1)

        except TTLibError:
            print('[ERROR] file "%s" is NOT a valid font file' % font_path, file=stderr)
            exit(-1)

    def __str__(self):
        return '\n'.join([
            '[Font Information]',
            'Path: "%s"' % self.font_path,
            'Copyright: %s' % self.copyright,
            'Family name: %s' % self.family_name,
            'Subfamily name: %s' % self.subfamily_name,
            'PostScript name: %s' % self.postscript_name,
            'Weight: %s' % self.font_weight,
            'Width: %s' % self.font_width
        ])


def main(font_path: str):
    font_path = str(font_path)
    font = FontInfo(font_path)
    print(font)


if __name__ == '__main__':
    # check arguments
    if len(argv) < 2:
        print('Usage: python3 %s <font path>' % __file__, file=stderr)
        exit(1)
    main(argv[1])
