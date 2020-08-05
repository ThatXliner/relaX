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
path.insert(0, "..")
from relaX.fig import get_config_file


class TestClass(object):
    def test_no(self):
        stuff = get_config_file("Unexisting config file name").get("nothing")
        assert stuff == None

    def test_spam(self):
        stuff = get_config_file("test", defaults={"have_spam": True})["have_spam"]
        assert stuff == True
