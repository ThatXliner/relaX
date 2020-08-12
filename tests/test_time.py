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

        assert Date().today == today()

    def test_yesterday(self):
        assert yesterday() == str(
            str(time.gmtime(time.time()).tm_mon)
            + "/"
            + str(int(time.gmtime(time.time()).tm_mday) - 1)
            + "/"
            + str(time.gmtime(time.time()).tm_year)
        )

        assert Date().yesterday() == yesterday()

    def test_tomorrow(self):
        assert tomorrow() == str(
            str(time.gmtime(time.time()).tm_mon)
            + "/"
            + str(int(time.gmtime(time.time()).tm_mday) + 1)
            + "/"
            + str(time.gmtime(time.time()).tm_year)
        )

        assert Date().tomorrow() == tomorrow()

    def test_OK_invalid_args(self):
        d = Date(yadda="iefyi")
        d.yesterday(yadda="iefyi")
        d.days_after_today(yadda="iefyi")
        d.increment_days(yadda="iefyi")

    def test_str_method(self):
        d = {"month": "8", "day": "12", "year": "2020"}
        assert str(Date()) == "8/12/2020"

    def test_catches_(self):
        try:
            Date(month="hi")
        except ValueError:
            pass
        try:
            Date().increment_days("12.hi")
        except ValueError:
            pass
