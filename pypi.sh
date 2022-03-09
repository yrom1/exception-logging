#!/usr/bin/env bash
echo "This fails if you didn't bump the version beforehand"
rm -rf dist
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m build
python3 -m pip install --upgrade twine
python3 -m twine upload dist/*
