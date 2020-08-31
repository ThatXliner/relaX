#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""To setup."""
from pathlib import Path
from setuptools import setup, find_packages
from relaX import __version__

# The directory containing this file
HERE = Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
REQUIREMENTS = (HERE / "requirements.txt").read_text().split("\n")
CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Programming Language :: Python :: 3 :: Only",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Development Status :: 3 - Alpha",
    "Natural Language :: English",
    "Intended Audience :: Developers",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: System Administrators",
    "Topic :: Utilities",
]
setup(
    name="relaX-library",
    version=__version__,
    author="Bryan Hu",
    author_email="bryan.hu.cn@gmail.com",
    description="A collection of usefulness...",
    long_description=README,
    long_description_content_type="text/markdown",
    # url="https://github.com/ThatXliner/relaX",
    project_urls={
        "Source Code": "https://github.com/ThatXliner/relaX",
        "Tracker": "https://github.com/ThatXliner/relaX/issues",
    },
    packages=find_packages(exclude=["tests"], include=["relaX"]),
    classifiers=CLASSIFIERS,
    python_requires=">=3.5",
    include_package_data=True,
    install_requires=[
        line for line in REQUIREMENTS if not line.startswith("#")
    ],
)
