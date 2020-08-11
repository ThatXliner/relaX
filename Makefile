OPTIMIZE_LEVEL = -OO
BUILDER := py_compile
python3:
	@echo "Building..."
	python3 ${OPTIMIZE_LEVEL} -m relaX/*.py
python3.8:
	@echo "Building..."
	python3.8 ${OPTIMIZE_LEVEL} -m relaX/*.py
