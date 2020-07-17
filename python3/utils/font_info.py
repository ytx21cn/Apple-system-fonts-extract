from os.path import abspath
from sys import stderr

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
    This class stores the basic information of a font file.
    """

    def __init__(self, font_path: str):
        try:
            # initialize font
            font_path = abspath(str(font_path))
            font = TTFont(font_path)
            self.font_path = font_path

            # save "name" table
            self.__name_table = font.get('name')

            # save essential information from the "name" table
            # for the name ID codes, visit https://docs.microsoft.com/en-us/typography/opentype/spec/name#name-ids
            self.copyright = self.__name_table.getDebugName(0)
            self.family_name = self.__name_table.getDebugName(16) or self.__name_table.getDebugName(1)
            self.subfamily_name = self.__name_table.getDebugName(17) or self.__name_table.getDebugName(2)
            self.postscript_name = self.__name_table.getDebugName(6)

            # save "OS/2" table information
            # for the OS/2 table, visit: https://docs.microsoft.com/en-us/typography/opentype/spec/os2
            self.__os2_table = font.get('OS/2')
            self.font_weight = self.__os2_table.usWeightClass
            self.font_width = self.__os2_table.usWidthClass

        except OSError:
            print('[ERROR]\nfont file "%s" does not exist' % font_path, file=stderr)
            exit(-1)

        except TTLibError:
            print('[ERROR]\nfile "%s" is NOT a valid font file' % font_path, file=stderr)
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
            'Width: %s' % self.font_width,
        ])
