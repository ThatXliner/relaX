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
    ) -> None:
        """This date object is a object wrapper of all of the functions defined in this
        file.

        :param type month: The month to set the date to. Defaults to time.gmtime(time.time()).tm_mon.
        :param type day: The day to set the date to. Defaults to time.gmtime(time.time()).tm_mday.
        :param type year: The year to set the date to. Defaults to time.gmtime(time.time()).tm_year.
        :return: Nothing.
        :rtype: None

        """
        # NOTE: Should the take-care method be truncation or modulo?
        self.month = abs(int(float(month)))
        month = self.month  # Optimization.
        self.month = month if month <= 12 else (month % 12) + 1
        self.year = abs(int(float(year)))
        year = self.year  # Optimization.
        self.day = abs(int(float(day)))
        day = self.day  # Optimization.
        if year % 4 == 0 and month == 2:  # Leap year AND February.
            mdays = 29
            self.day = day if day <= mdays else (day % mdays) + 1
        elif day > (30 if month % 2 == 0 else 31):
            mdays = 30 if month % 2 == 0 else 31
            mdays = 28 if month % 2 == 0 else mdays
            self.day = day % mdays + 1
        self.date = [self.month, self.day, self.year]
        self.json_date = dict(zip(["month", "day", "year"], self.date))

    def __str__(self) -> str:
        """__str__ method."""
        return "/".join(self.date)

    def __repr__(self) -> str:
        """__repr__ method."""
        return self.__str__()

    def __dict__(self) -> dict:
        """__dict__ method."""
        return self.json_date

    def __getitem__(self, key) -> int:
        """A shorter (and safer) version of dict(Date())['key']. Case insensitive.

        :param type key: The key.
        :return: An integer value of the corresponding key.
        :rtype: int

        """
        return self.json_date.get(key.lower())

    def update_time(self) -> None:
        """To update the time.

        :return: Nothing.
        :rtype: None

        """
        _ = time.gmtime(time.time())  # Optimization.
        self.month = int(float(_.tm_mon))
        self.day = int(float(_.tm_mday))
        self.year = int(float(_.tm_year))

        self.date = [self.month, self.day, self.year]
        self.json_date = dict(zip(["month", "day", "year"], self.date))

    def daysBeforeToday(self, amount: int) -> str:
        """Returns a string representing some number of days before today.

        :param int amount: How many days before today do you want to get?
        :return: A string of the date described above.
        :rtype: str

        """
        pass
