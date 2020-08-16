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
# TODO: Make the main API robust and relax-grade
##########################################################################################
# Module getting #########################################################################
##########################################################################################
try:
    from pathlib2 import Path as p  # noqa: F401

    def _Path(path) -> p:

        return p(path).expanduser()


except ModuleNotFoundError:
    try:
        from pathlib import Path as p  # noqa: F401

        def _Path(path) -> p:

            return p(path).expanduser()

    except ModuleNotFoundError:
        raise ModuleNotFoundError(
            "You need to install the pathlib2 package. Try `python3 -m pip install "
            "pathlib2` or `pip install pathlib2`"
        )

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


def get_config_file(
    config_file_name: str, safe: bool = False, defaults: dict = {}
) -> dict:
    """
    You should use this: this is the main API.

    :param str config_file_name: This is the name of the project you want to extract
    the configuration from.
    :param bool safe: YAML may contain python objects. If this is set to False,
    you'll be `pickling` tthe python objects. By setting the safe option to `True`,
    you'll not be able to create python objects. Defaults to False.
    :return: This returns a dictionary containing the parsed YAML file. May return the
    defaults if any error(s) occurred.
    :rtype: dict

    """
    ###############################
    # Type verification ###########
    ###############################
    config_file_name = str(config_file_name)
    defaults = dict(defaults)
    safe = bool(safe)
    ###############################
    XFIG_PATH = _Path("~/Xfig_index.yml")

    def loads(file: p, *args, **kwargs):
        if safe:  # If safe mode is enabled
            return safe_load(file.read_text(), Loader=Loader)
        else:  # Or it isn't
            return load(file.read_text(), Loader=Loader)

    def create_config_file():
        new_config = _Path("~/{}.yml".format(config_file_name))
        if not new_config.exists():
            new_config.touch()
            new_config.write_text(
                dump(defaults, Dumper=Dumper, default_flow_style=False)
            )
        else:  # The 'new' config file exists
            config_file_stuff = loads(new_config)
            if config_file_stuff is not None and config_file_stuff is dict:
                new_config.write_text(
                    dump(
                        {**config_file_stuff, **defaults},
                        Dumper=Dumper,
                        default_flow_style=False,
                    )
                )
            else:
                new_config.write_text(
                    dump(defaults, Dumper=Dumper, default_flow_style=False)
                )

        return str(new_config)

    if XFIG_PATH.exists() and XFIG_PATH.is_file():
        try:
            cfp = loads(XFIG_PATH).get(config_file_name)
        except AttributeError:  # There is nothing in the config file
            # Create the config file from defaults given
            new_config = _Path("~/{}.yml".format(config_file_name))
            if not new_config.exists():
                new_config.touch()
            new_config.write_text(
                dump(str(defaults), Dumper=Dumper, default_flow_style=False)
            )
            return defaults

        # Check if the key points to something
        else:
            if cfp is not None:
                cfp = _Path(str(cfp))
                if cfp.exists() and cfp.is_file():
                    return loads(cfp)
                else:  # It doesn't exist
                    create_config_file()
                    return defaults
            else:
                return defaults

    else:  # The config index file doesn't exist
        XFIG_PATH.touch()
        XFIG_PATH.write_text(
            "---\n# This file was generated automatically by relaX.fig .\n"
        )
        return defaults
