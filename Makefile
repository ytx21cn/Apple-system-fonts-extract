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

$(font_list): $(otf_files)
	python3 ALL.py $(dmg_dir) $(otf_dir)
	@echo
	$(FIND_OTF) -exec ls {} \; > $(font_list)

.PHONY: clean
clean:
	python3 CLEAN.py $(font_list) $(otf_dir)
