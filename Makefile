PYTHON := python3

dmg_dir := dmg/
otf_dir := otf/

font_list := font_list.txt
release_zip := Apple_fonts.zip

extract_fonts := $(PYTHON) MAIN.py $(dmg_dir) $(otf_dir)
clear_fonts := $(PYTHON) CLEAN.py $(font_list) $(otf_dir)

create_release_zip := $(PYTHON) CREATE_RELEASE_ZIP.py $(otf_dir) $(release_zip)
rm_release_zip := $(PYTHON) CLEAN.py $(release_zip)

main_target := fonts

.PHONY: $(main_target)
$(main_target):
	$(extract_fonts)

.PHONY: release
release: $(release_zip)

$(release_zip): $(main_target)
	$(create_release_zip)

.PHONY: rm_release
rm_release:
	$(rm_release_zip)

.PHONY: clean
clean: rm_release
	$(clear_fonts)
