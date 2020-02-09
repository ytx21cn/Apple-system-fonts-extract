PYTHON := python3

dmg_dir := dmg/
otf_dir := otf/

font_list := font_list.txt
release_zip := Apple_fonts.zip

extract_fonts := $(PYTHON) MAIN.py $(dmg_dir) $(otf_dir)
list_fonts := $(PYTHON) LS_FONTS.py $(otf_dir)
clear_fonts := $(PYTHON) CLEAN.py $(font_list) $(otf_dir)

create_release_zip := $(PYTHON) CREATE_ZIP.py $(otf_dir) $(release_zip)
rm_release_zip := $(PYTHON) CLEAN.py $(release_zip)

suppress_stderr := 2>/dev/null
fonts_changed := $(shell $(list_fonts) $(suppress_stderr) | diff -q - $(font_list) $(suppress_stderr); echo $$?)

.PHONY: fonts
fonts:
ifneq ($(fonts_changed), 0)
	$(extract_fonts)
	@echo
	$(list_fonts) > $(font_list)
endif

.PHONY: release
release: $(release_zip)

$(release_zip): fonts
	$(create_release_zip)

.PHONY: rm_release
rm_release:
	$(rm_release_zip)

.PHONY: clean
clean:
	$(clear_fonts)
