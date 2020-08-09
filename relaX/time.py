#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Bryan Hu .

@Bryan Hu .

Made with love by Bryan Hu .


Version: see __init__.py

Desc: A collection of useful time-related functions and objects.

"""

import time


def getTime() -> str:
    """
    Returns the current time. In a easy-to-process,
    human-readable, format. Kinda raw though...
    """
    return str(time.strftime(time.asctime(time.localtime(time.time()))))


def daysBeforeToday(amount: int) -> str:
    """Returns a string representing some number of days before today.

    :param int amount: How many days before today do you want to get?
    :return: A string of the date described above.
    :rtype: str

    """
    amount = int(float(amount)) if isinstance(amount, int) else amount
    _ = time.gmtime(time.time())
    return str(
        str(_.tm_mon) + "/" + str(int(_.tm_mday - amount)) + "/" + str(_.tm_year)
    )


def daysAfterToday(amount: int) -> str:
    """Returns a string representing some number of days after today.

    :param int amount: How many days after today do you want to get?
    :return: A string of the date described above.
    :rtype: str

    """
    amount = int(float(amount)) if isinstance(amount, int) else amount
    return daysBeforeToday(amount * -1)  # Double negatives


def yesterday() -> str:
    """
    Returns yesterday's date.

    :return: A string of the date described above.
    :rtype: str

    """
    return daysBeforeToday(1)


def today() -> str:
    """
    Returns today's date.

    :return: A string of the date described above.
    :rtype: str

    """
    return daysAfterToday(0)


def tommorrow() -> str:
    """
    Returns tommorrow's date.

    :return: A string of the date described above.
    :rtype: str

    """
    return daysAfterToday(1)


class Date(object):
    def __init__(
        self,
        month=time.gmtime(time.time()).tm_mon,
        day=time.gmtime(time.time()).tm_mday,
        year=time.gmtime(time.time()).tm_year,
    ):
        self.month = int(float(month))
        self.day = int(float(day))
        self.year = int(float(year))

        self.date = [self.month, self.day, self.year]
        self.json_date = dict(zip(["month", "day", "year"], self.date))

    def __str__(self):
        return "/".join(self.date)

    def __repr__(self):
        return self.__str__()

    def __dict__(self):
        return self.json_date

    def __getitem__(self, key):
        return self.json_date[key.lower()]
