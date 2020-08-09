#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Bryan Hu .

@Bryan Hu .

Made with love by Bryan Hu .


Version: TEST

Desc: THIS IS A TEST.

"""
from sys import path
import time

path.insert(0, ".")
path.insert(0, "..")
from relaX.time import *


class TestClass(object):
    def test_today(self):
        assert today() == str(
            str(time.gmtime(time.time()).tm_mon)
            + "/"
            + str(int(time.gmtime(time.time()).tm_mday))
            + "/"
            + str(time.gmtime(time.time()).tm_year)
        )

    def test_yesterday(self):
        assert yesterday() == str(
            str(time.gmtime(time.time()).tm_mon)
            + "/"
            + str(int(time.gmtime(time.time()).tm_mday) - 1)
            + "/"
            + str(time.gmtime(time.time()).tm_year)
        )

    def test_tomorrow(self):
        assert tommorrow() == str(
            str(time.gmtime(time.time()).tm_mon)
            + "/"
            + str(int(time.gmtime(time.time()).tm_mday) + 1)
            + "/"
            + str(time.gmtime(time.time()).tm_year)
        )
