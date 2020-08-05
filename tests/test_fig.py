#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Bryan Hu .

@Bryan Hu .

Made with love by Bryan Hu .


Version: vTEST

Desc: THIS IS A TEST.

"""
from sys import path
from pathlib2 import Path

path.insert(0, Path(Path(Path(__file__).parent).parent / "relaX"))
from relaX.fig import get_config_file


def test():
    stuff = get_config_file("Unexisting config file name").get("nothing")
