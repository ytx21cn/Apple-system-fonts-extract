import dmg2img
import extract_fonts_from_payloads
import extract_img
import extract_pkg
import rm_extracted


def main():
    dmg2img.main()
    extract_img.main()
    extract_pkg.main()
    extract_fonts_from_payloads.main()
    rm_extracted.main()


if __name__ == '__main__':
    main()
