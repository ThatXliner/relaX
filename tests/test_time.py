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
import pytest

path.insert(0, ".")
path.insert(0, "..")
from relaX.time import *


class TestClass(object):
    def test_today(self):
        assert today() == str(
            str(time.localtime(time.time()).tm_mon)
            + "/"
            + str(int(time.localtime(time.time()).tm_mday))
            + "/"
            + str(time.localtime(time.time()).tm_year)
        )

        assert Date().today() == today()

    def test_yesterday(self):
        assert yesterday() == str(
            str(time.localtime(time.time()).tm_mon)
            + "/"
            + str(int(time.localtime(time.time()).tm_mday) - 1)
            + "/"
            + str(time.localtime(time.time()).tm_year)
        )

        assert Date().yesterday() == yesterday()

    def test_tomorrow(self):
        assert tomorrow() == str(
            str(time.localtime(time.time()).tm_mon)
            + "/"
            + str(int(time.localtime(time.time()).tm_mday) + 1)
            + "/"
            + str(time.localtime(time.time()).tm_year)
        )

        assert Date().tomorrow() == tomorrow()

    def test_OK_invalid_args(self):
        d = Date(yadda="iefyi")
        d.yesterday(yadda="iefyi")
        d.days_after_today(yadda="iefyi")
        d.increment_days(yadda="iefyi")

    def test_str_method(self):
        d = {"month": "8", "day": "12", "year": "2020"}
        assert str(Date(**d)) == "8/12/2020"

    def test_catches_(self):
        try:
            Date(month="hi")
        except ValueError:
            pass
        try:
            Date().increment_days("12.hi")
        except ValueError:
            pass

    def test_date_eq_date(self):
        assert Date() == Date()

    def test_ded(self):
        assert Date(1, 1, 1) == Date(1, 1, 1)

    def test_eq_add_i(self):
        assert (Date(month=1, day=1, year=2021) + 1) == Date(month=1, day=2, year=2021)

    def test_add_d(self):
        assert (Date(0, 0, 100) + Date(1, 45, 100)) == Date(1, 45, 200)

    def test_more(self):
        assert (Date(8, 15, 2020) > Date(0, 0, 100)) == True
