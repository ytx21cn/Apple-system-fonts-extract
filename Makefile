PYTHON := python3

dmg_dir := dmg/
otf_dir := otf/

font_list := font_list.txt

FIND_DMG := find $(dmg_dir) -type f -name *.dmg
FIND_OTF := find $(otf_dir) -type f -name *.otf
ESCAPE_SPACES := sed 's/ /\\ /'

dmg_files := $(shell $(FIND_DMG); exit 0 | $(ESCAPE_SPACES))
otf_files := $(shell $(FIND_OTF); exit 0 | $(ESCAPE_SPACES))

.PHONY: all
all: $(font_list)

$(font_list): $(dmg_files) $(otf_files)
	$(PYTHON) ALL.py $(dmg_dir) $(otf_dir)
	@echo
	TZ=utc $(FIND_OTF) -exec ls -lhog {} \; > $(font_list)

.PHONY: clean
clean:
	$(PYTHON) CLEAN.py $(font_list) $(otf_dir)
