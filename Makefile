PYTHON := python3

dmg_dir := dmg/
otf_dir := otf/

otf_phony := .otf
font_list := font_list.txt

LS_OTF := TZ=utc ls -lhog $(otf_dir)*
otf_files_changed := $(shell $(LS_OTF) | diff -q - $(font_list) > /dev/null; echo $$?)

.PHONY: all
all: $(otf_phony) $(font_list)

.PHONY: $(otf_phony)
$(otf_phony):
ifneq ($(otf_files_changed), 0)
	$(PYTHON) ALL.py $(dmg_dir) $(otf_dir)
	@echo
endif

$(font_list):
ifneq ($(otf_files_changed), 0)
	$(LS_OTF) > $@
endif

.PHONY: clean
clean:
	$(PYTHON) CLEAN.py $(font_list) $(otf_dir)
