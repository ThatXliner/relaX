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

path.insert(0, ".")
from relaX.fig import get_config_file


def test():
    stuff = get_config_file("Unexisting config file name").get("nothing")
