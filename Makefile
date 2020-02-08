PYTHON := python3

dmg_dir := dmg/
otf_dir := otf/

font_list := font_list.txt

LS_OTF := TZ=utc ls -lhog $(otf_dir)*
otf_files_changed := $(shell $(LS_OTF) | diff -q - $(font_list) > /dev/null; echo $$?)

.PHONY: all
all:
ifneq ($(otf_files_changed), 0)
	$(PYTHON) ALL.py $(dmg_dir) $(otf_dir)
	@echo
	$(LS_OTF) > $(font_list)
endif

.PHONY: clean
clean:
	$(PYTHON) CLEAN.py $(font_list) $(otf_dir)
