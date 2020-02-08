PYTHON := python3

dmg_dir := dmg/
otf_dir := otf/

font_list := font_list.txt

extract_fonts := $(PYTHON) ALL.py $(dmg_dir) $(otf_dir)
list_fonts := $(PYTHON) LS_FONTS.py $(otf_dir)
clear_fonts := $(PYTHON) CLEAN.py $(font_list) $(otf_dir)

.PHONY: all
all:
	$(extract_fonts)
	@echo
	$(list_fonts) > $(font_list)

.PHONY: clean
clean:
	$(clear_fonts)
