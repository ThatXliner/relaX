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
    """Returns the current time.

    In a easy-to-process, human-readable, format. Kinda raw though...
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
        """This date object is a object wrapper of all of the functions defined in this file.

        :param type month: The month to set the date to. Defaults to
        time.gmtime(time.time()).tm_mon.
        :param type day: The day to set the date to. Defaults to
        time.gmtime(time.time()).tm_mday.
        :param type year: The year to set the date to. Defaults to
        time.gmtime(time.time()).tm_year.
        :return: Nothing.
        :rtype: None

        """
        self.month = abs(int(float(month)))
        tmonth = self.month  # Optimization.
        self.month = tmonth if tmonth <= 12 else (tmonth % 12) + 1
        self.year = abs(int(float(year)))
        mday = self._calculate_mday(tmonth, self.year)
        self.day = abs(int(float(day)))
        tday = self.day  # Optimization.
        self.day = tday if tday <= mday else (tday % mday) + 1
        self.date = [self.month, self.day, self.year]
        self.json_date = dict(zip(["month", "day", "year"], self.date))
        self.mday = mday

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

    def _calculate_mday(self, tmonth, year):
        if tmonth % 2 == 0:  # Even month
            if tmonth == 2:
                mday = 29 if year % 4 == 0 else 28
            else:
                mday = 30
        else:
            mday = 31
        return mday

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

    def days_before_today(self, amount: int) -> str:
        """Returns a string representing some number of days before today.

        :param int amount: How many days before today do you want to get?
        :return: A string of the date described above.
        :rtype: str

        """
        amount = int(float(amount))
        return str(
            Date(month=self.month, day=self.day, year=self.year).add_days(amount * -1)
        )

    def add_days(self, amount: int) -> None:
        """Increments the amount of days after today.

        :param int amount: The amount of days to add.
        :return: Nothing.
        :rtype: None

        """
        amount = abs(int(float(amount)))
        if self.day + amount > self.mday:  # Next month
            if self.month + 1 > self.year:  # Next year
                self.year += 1  # Increment year
                self.day += amount  # Increment day
                # Increment month
                self.month += (  # Calculate months
                    self.day // self._calculate_mday(self.month, self.year)
                ) % 12  # Turn it into months
                # Modulo incremented days
                self.day = self.day % self._calculate_mday(self.month, self.year)
            else:  # Not next year
                self.month += 1  # Increment month
                self.day += amount  # Increment day
                # Modulo incremented days
                self.day = self.day % self._calculate_mday(self.month, self.year)
        else:  # Normal
            self.day += amount
