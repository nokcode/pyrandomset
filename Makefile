.PHONY: all build upload clean
TEST="--repository testpypi"

all: build

build:
	python3 setup.py sdist bdist_wheel

upload:
	python3 -m twine upload dist/*

clean:
	rm -rf build/ dist/ pyrandomset.egg-info/
