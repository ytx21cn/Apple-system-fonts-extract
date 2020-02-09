PYTHON := python3

dmg_dir := dmg/
otf_dir := otf/

font_list := font_list.txt

extract_fonts := $(PYTHON) MAIN.py $(dmg_dir) $(otf_dir)
list_fonts := $(PYTHON) LS_FONTS.py $(otf_dir)
clear_fonts := $(PYTHON) CLEAN.py $(font_list) $(otf_dir)

suppress_stderr := 2>/dev/null
fonts_changed := $(shell $(list_fonts) $(suppress_stderr) | diff -q - $(font_list) $(suppress_stderr); echo $$?)

.PHONY: all
all:
ifneq ($(fonts_changed), 0)
	$(extract_fonts)
	@echo
	$(list_fonts) > $(font_list)
endif

.PHONY: clean
clean:
	$(clear_fonts)
