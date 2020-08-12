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
            "You need to install the pathlib2 package. Try `python3 -m pip install \
pathlib2` or `pip install pathlib2`"
        )

# try:  # Try basic import
#     from .errors import UnsupportedPythonVersion
# except ImportError:
#     try:  # Maybe no dot?
#         from errors import UnsupportedPythonVersion
#     except ImportError:  # Editing the sys.path is a last resort
#         from sys import path
#
#         path.insert(0, str(_Path(__file__).parent))
#         from errors import UnsupportedPythonVersion

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
    config_file_name = (
        str(config_file_name)
        if not isinstance(config_file_name, str)
        else config_file_name
    )
    defaults = dict(defaults) if not isinstance(defaults, dict) else defaults
    safe = bool(safe) if not isinstance(safe, bool) else safe
    ###############################
    XFIG_PATH = _Path("~/Xfig_index.yml")
    if XFIG_PATH.exists() and XFIG_PATH.is_file():
        try:
            cfp = load(XFIG_PATH.read_text(), Loader=Loader).get(config_file_name)
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
                    if safe:  # If safe mode is enabled
                        return safe_load(cfp.read_text(), Loader=Loader)
                    else:  # Or it isn't
                        return load(cfp.read_text(), Loader=Loader)
                else:  # It doesn't exist
                    # Create the config file from defaults given
                    new_config = _Path("~/{}.yml".format(config_file_name))
                    if not new_config.exists():
                        new_config.touch()
                        new_config.write_text(
                            dump(
                                str(defaults), Dumper=Dumper, default_flow_style=False,
                            )
                        )
                    else:  # The 'new' config file exists
                        new_config.write_text(
                            dump(
                                str(
                                    {
                                        **defaults,
                                        **load(new_config.read_text(), Loader=Loader),
                                    }
                                ),
                                Dumper=Dumper,
                                default_flow_style=False,
                            )
                        )
                    return defaults
            else:
                return defaults

    else:  # The config index file doesn't exist
        XFIG_PATH.touch()
        XFIG_PATH.write_text(
            "---\n# This file was generated automatically by relaX.fig .\n"
        )
        return defaults
