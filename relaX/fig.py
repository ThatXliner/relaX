#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Bryan Hu .

@Bryan Hu .

Made with love by Bryan Hu .


Version: v1.0

Desc: relaXfig is a simple configuration system designed to be integrated into pretty
much everything. Currently, it isn't that relaxing. But in the future, it'll support
complex configuration and other features.

Example:

>>> from relaX.fig import get_config_file
>>> have_spam = get_config_file("Project_name")["have spam?"]


relax.

"""

##########################################################################################
# Module getting #########################################################################
##########################################################################################
try:
    from pathlib2 import Path as p  # noqa: F401

    def Path(path) -> p:
        """You should not use this. This is little shortcut."""
        return p(path).expanduser()


except ModuleNotFoundError:
    try:
        from pathlib import Path as p  # noqa: F401

        def Path(path) -> p:
            """You should not use this. This is little shortcut."""
            return p(path).expanduser()

    except ModuleNotFoundError:
        raise ModuleNotFoundError(
            "You need to install the pathlib2 package. Try `python3 -m pip install \
pathlib2` or `pip install pathlib2`"
        )

try:  # Try basic import
    from .errors import UnsupportedPythonVersion
except ImportError:
    try:  # Maybe no dot?
        from errors import UnsupportedPythonVersion
    except ImportError:  # Editing the sys.path is a last resort
        from sys import path

        path.insert(0, Path(Path(__file__).parent))
        from errors import UnsupportedPythonVersion

try:
    from yaml import load, safe_load, dump

    try:
        from yaml import CLoader as Loader, CDumper as Dumper
    except ImportError:
        from yaml import Loader, Dumper

except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "You have to install the pyyaml package for relaX.fig . Try `python3 -m pip \
install pyyaml` or `pip install pyyaml`"
    )

##########################################################################################
# Main API ###############################################################################
##########################################################################################


class get_config_file(object):
    """
    You should use this.

    This is the main API.

    :param str config_file_name: This is the name of the project you want to extract the
    configuration from.
    :param bool safe: YAML may contain python objects. If this is set to False, you'll be
    `pickling` tthe python objects. By setting the safe option to `True`, you'll not be
    able to create python objects. Defaults to False.
    :attr type main: This is the internal dict object that was extracted from the
    configuration file.

    """

    def __init__(self, config_file_name: str, safe: bool = False, defaults: dict = {}):
        """
        You should use this: this is the main API.

        :param str config_file_name: This is the name of the project you want to extract
        the configuration from.
        :param bool safe: YAML may contain python objects. If this is set to False,
        you'll be `pickling` tthe python objects. By setting the safe option to `True`,
        you'll not be able to create python objects. Defaults to False.
        :return: This returns a dictionary containing the parsed YAML file.
        May return an empty dictionary if the file couldn't be found.
        :rtype: dict

        """
        config_file_name = (
            str(config_file_name)
            if not isinstance(config_file_name, str)
            else config_file_name
        )
        defaults = dict(defaults) if not isinstance(defaults, dict) else defaults

        safe = bool(safe) if not isinstance(safe, bool) else safe
        if Path("~/Xfig_index.yml").exists() and Path("~/Xfig_index.yml").is_file():
            try:
                cfp = load(Path("~/Xfig_index.yml").read_text(), Loader=Loader).get(
                    config_file_name
                )
            except AttributeError:  # There is nothing in the config file
                new_config = Path("~/{}.yml".format(config_file_name))
                if not new_config.exists():
                    new_config.touch()
                new_config.write_text(
                    dump(defaults, Loader=Loader, default_flow_style=False)
                )
                cfp = defaults

            # Check if the key points to something
            if cfp is not None:
                cfp = Path(str(cfp))
                if cfp.exists() and cfp.is_file():
                    if safe:  # If safe mode is enabled
                        self.main = safe_load(cfp.read_text(), Loader=Loader)
                    else:  # Or it isn't
                        self.main = load(cfp.read_text(), Loader=Loader)
            else:
                self.main = {}

        else:  # The config index file doesn't exist
            Path("~").touch("Xfig_index.yml")
            Path("~/Xfig_index.yml").write_text(
                "# This file was generated automatically by Xfig."
            )
            self.main = {}

    def __getitem__(self, key):
        """Magic method for getitem."""
        return self.main.get(key)

    def __len__(self):
        """Magic method for len."""
        return len(self.main)

    def __dict__(self):
        """Magic method for dict."""
        return dict(self.main)

    def __repr__(self):
        """Magic method for repr."""
        return repr(self.main)

    def __str__(self):
        """Magic method for str."""
        return str(self.main)

    def get(self, *args, **kwargs):
        """Get method."""
        return self.main.get(*args, **kwargs)
