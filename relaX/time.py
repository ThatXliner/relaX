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


def yesterday() -> str:
    """Returns a formatted string of yesterday's date.

    :return: The formatted string of yesterday's date.
    :rtype: str

    """
    return str(Date().yesterday())


def today() -> str:
    """Returns a formatted string of today's date.

    :return: The formatted string of today's date.
    :rtype: str

    """
    return str(Date())


def tomorrow() -> str:
    """Returns a formatted string of tomorrow's date.

    :return: The formatted string of tomorrow's date.
    :rtype: str

    """
    return str(Date().tomorrow())


class Date(object):
    # TODO: Write better docs
    """A relaX-grade date object."""

    def __init__(
        self,
        month=time.localtime(time.time()).tm_mon,
        day=time.localtime(time.time()).tm_mday,
        year=time.localtime(time.time()).tm_year,
        *args,
        **kwargs
    ) -> None:
        """This date object is a object wrapper of all of the functions defined in this file.

        :param type month: The month to set the date to. Defaults to
        time.localtime(time.time()).tm_mon.
        :param type day: The day to set the date to. Defaults to
        time.localtime(time.time()).tm_mday.
        :param type year: The year to set the date to. Defaults to
        time.localtime(time.time()).tm_year.
        :return: Nothing.
        :rtype: None

        """
        # TODO: Also implement the seconds, hour, and minutes
        try:
            self.month = abs(int(float(month)))
        except ValueError:
            raise ValueError("Invalid month")
        tmonth = self.month  # Optimization.
        self.month = tmonth if tmonth <= 12 else (tmonth % 12) + 1
        try:
            self.year = abs(int(float(year)))
        except ValueError:
            raise ValueError("Invalid year")
        mday = self._calculate_mday(tmonth, self.year)
        try:
            self.day = abs(int(float(day)))
        except ValueError:
            raise ValueError("Invalid day")
        tday = self.day  # Optimization.
        self.day = tday if tday <= mday else (tday % mday) + 1
        self.date = [self.month, self.day, self.year]
        self.json_date = dict(zip(["month", "day", "year"], self.date))
        self.mday = mday

    def __str__(self) -> str:
        """__str__ method."""
        return "/".join(map(str, self.date))

    def __repr__(self) -> str:
        return repr(self.__str__())

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

    def __add__(self, other):
        """__add__ magic method.

        :param type other: Description of parameter `other`.
        :return: Description of returned object.
        :rtype: type

        """
        if isinstance(other, Date):
            self.month += other.month
            self.day += other.day
            self.year += other.year
            self.update()
            return Date(month=self.month, day=self.day, year=self.year,)

        else:
            self.increment_days(other)
            return self

    def __gt__(self, other):
        """Short summary.

        :param type other: Description of parameter `other`.
        :return: Description of returned object.
        :rtype: type

        """
        ojd = other.date
        jd = self.date
        if isinstance(other, Date):
            return jd[0] > ojd[0] and jd[1] > ojd[1] and jd[2] > ojd[2]
        else:
            raise TypeError("Expected a Date object, got %s" % type(other))

    def __le__(self, other):
        """Short summary.

        :param type other: Description of parameter `other`.
        :return: Description of returned object.
        :rtype: type

        """
        return not other > self

    def __lt__(self, other):
        return other <= self and not other == self

    def __ne__(self, other):
        return not other == self

    def __eq__(self, other):
        if isinstance(other, Date):
            return self.date == other.date
        elif isinstance(other, (list, tuple)):
            return self.date == map(int, map(float, other[:2]))
        else:
            raise TypeError(
                "Expected a Date object or an iterable with at begins with 3 numbers,"
                " got %s" % repr(type(other))
            )

    @property
    def is_leap_year(self, year=None):
        if year is None:
            year = self.year
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def _calculate_mday(self, tmonth, year, *args, **kwargs):
        if tmonth % 2 == 0:  # Even month
            if tmonth == 2:
                mday = 29 if self.is_leap_year() else 28
            else:
                mday = 30
        else:
            mday = 31
        return mday

    def sync_time(self, *args, **kwargs) -> None:
        """To update the time to your local timezone.

        :return: Nothing.
        :rtype: None

        """
        _ = time.localtime(time.time())  # Optimization.
        self.month = int(float(_.tm_mon))
        self.day = int(float(_.tm_mday))
        self.year = int(float(_.tm_year))

        self.date = [self.month, self.day, self.year]
        self.json_date = dict(zip(["month", "day", "year"], self.date))
        return self

    def days_before_today(self, amount: int = 1, *args, **kwargs) -> str:
        """Returns a string representing some number of days before today.

        :param int amount: How many days before today do you want to get?
        :return: A string of the date described above.
        :rtype: str

        """
        try:
            amount = int(float(amount))
        except ValueError:
            raise ValueError("Invalid amount value")
        edited = self.json_date
        edited["day"] -= amount
        d = Date(**edited)
        del edited
        return str(d)

    def days_after_today(self, amount: int = 1, *args, **kwargs) -> str:
        """Returns a string representing some number of days after today.

        :param int amount: How many days after today do you want to get?
        Defaults to 1 day.
        :return: A string of the date described above.
        :rtype: str

        """
        try:
            amount = int(float(amount))
        except ValueError:
            raise ValueError("Invalid amount value")
        return self.days_before_today(amount * -1)  # Double negatives

    def increment_days(self, amount: int = 1, *args, **kwargs):
        """Increments the amount of days after today.

        :param int amount: The amount of days to add. Defaults to 1 day.
        :return: Nothing.
        :rtype: None

        """
        amount = int(float(amount))
        if (self.day + amount) > self.mday:  # Next month
            # Increment day
            self.increment_months(self.day // self.mday)
            self.day += amount % self.mday
        else:  # Normal
            self.day += amount
        self.update()
        return self


    def yesterday(self, *args, **kwargs) -> str:
        """
        Returns yesterday's date.

        :return: A string of the date described above.
        :rtype: str

        """
        return self.days_before_today(1)  # We explicitly use 1 to improve clarity.


    def today(self, *args, **kwargs) -> str:
        """
        Returns today's date.

        :return: A string of the date described above.
        :rtype: str

        """
        return self.__str__()


    def tomorrow(self, *args, **kwargs) -> str:
        """
        Returns tomorrow's date.

        :return: A string of the date described above.
        :rtype: str

        """
        return self.days_after_today(1)  # We explicitly use 1 to improve clarity.

    def increment_months(self, amount: int = 1):
        """Increments the amount of months after today.

        :param int amount: The amount of months to add. Defaults to 1 month.
        :return: Nothing.
        :rtype: None

        """
        try:
            amount = int(float(amount))
        except ValueError:
            raise ValueError("Invalid amount value")
        tmonth = self.month + amount
        if tmonth <= 12:
            self.month = tmonth
        else:
            self.month = (tmonth % 12) + 1
            self.year += tmonth // 12
        self.update()
        return self

    def update(self):
        self.date = [self.month, self.day, self.year]
        self.json_date = dict(zip(["month", "day", "year"], self.date))
