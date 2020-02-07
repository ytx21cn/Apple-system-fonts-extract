dmg_dir := dmg/
otf_dir := otf/

.PHONY: all
all:
	python3 ALL.py $(dmg_dir) $(otf_dir)

.PHONY: clean
clean:
	python3 CLEAN.py $(otf_dir)
