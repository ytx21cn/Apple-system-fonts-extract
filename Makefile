dmg_dir := dmg/
otf_dir := otf/

test_dir := 1\ 2
test_target := $(test_dir)/test

SUBST_SPACE = $(shell find $(1) -type f \( ! -path $(test_target) \) | sed 's/\ /\\\ /g')
test_prereq := $(call SUBST_SPACE, $(test_dir)/*)

.PHONY: all
all: $(test_dir)
	python3 ALL.py $(dmg_dir) $(otf_dir)


.PHONY: clean
clean:
	python3 CLEAN.py $(otf_dir)

# Experimental section

.PHONY: test
test: $(test_target)

.PHONY: test_clean
test_clean:
	-rm $(test_target)

$(test_target): $(test_prereq)
	@echo $^
	echo 'hello world' > '$@'
