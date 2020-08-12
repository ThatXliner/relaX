# OPTIMIZE_LEVEL = -OO
# BUILDER := py_compile
# python3:
# 	@echo "Building..."
# 	python3 ${OPTIMIZE_LEVEL} -m ${BUILDER} relaX/*.py
# 	python3 setup.py sdist bdist_wheel
# python3.8:
# 	@echo "Building..."
# 	python3.8 ${OPTIMIZE_LEVEL} -m ${BUILDER} relaX/*.py
# 	python3.8 setup.py sdist bdist_wheel
