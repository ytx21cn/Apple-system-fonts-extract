PYTHON := python3

dmg_dir := dmg/
otf_dir := otf/

extract_fonts := $(PYTHON) python3/MAIN.py $(dmg_dir) $(otf_dir)
clear_fonts := -rm -rfv $(otf_dir)

release_zip := Apple_fonts.zip

create_release_zip := zip -v -r $(release_zip) $(otf_dir)
rm_release_zip := -rm -rfv $(release_zip)

.PHONY: all
all:
	$(extract_fonts)
	$(create_release_zip)

.PHONY: clean
clean:
	$(clear_fonts)
	$(rm_release_zip)
