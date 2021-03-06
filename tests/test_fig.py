#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# flake8: noqa
"""
Author: Bryan Hu .

@Bryan Hu .

Made with love by Bryan Hu .


Version: TEST

Desc: THIS IS A TEST.

"""
from sys import path

path.insert(0, ".")
path.insert(0, "..")
from relaX.fig import get_config_file
import pytest


class TestClass(object):
    def test_no(self):
        stuff = get_config_file("Unexisting config file name").get("nothing")
        assert stuff == None
        stuff = get_config_file("Unexisting config file name").get("nothing")
        assert stuff == None

    def test_spam(self):
        stuff = get_config_file("test", defaults={"have_spam": True})["have_spam"]
        assert stuff == True
        stuff = get_config_file("test")["have_spam"]
        assert stuff == True
