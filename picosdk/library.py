#
# Copyright (C) 2018 Pico Technology Ltd. See LICENSE file for terms.
#
"""
Definition of the Library class, which is the abstract representation of a picotech device driver.
Note: Many of the functions in this class are missing: these are populated by the psN000(a).py modules, which subclass
this type and attach the missing methods.
"""

import sys
from ctypes.util import find_library

from picosdk.errors import (
    CannotFindPicoSDKError,
    CannotOpenPicoSDKError,
)


class Library(object):
    def __init__(self, name):
        self.name = name
        self._clib = self._load()

    def _load(self):
        library_path = find_library(self.name)

        # 'find_library' fails in Cygwin.
        if not sys.platform == "cygwin":
            if library_path is None:
                env_var_name = "PATH" if sys.platform == "win32" else "LD_LIBRARY_PATH"
                raise CannotFindPicoSDKError(
                    f"PicoSDK ({self.name}) not found, check {env_var_name}"
                )

        try:
            if sys.platform == "win32":
                from ctypes import WinDLL

                result = WinDLL(library_path)
            elif sys.platform == "cygwin":
                from ctypes import CDLL

                library_path = self.name
                result = CDLL(library_path + ".dll")
            else:
                from ctypes import cdll

                result = cdll.LoadLibrary(library_path)
        except OSError as e:
            raise CannotOpenPicoSDKError(
                f"PicoSDK ({self.name}) not compatible (check 32 vs 64-bit): {e}"
            )
        return result

    def __str__(self):
        return f"picosdk {self.name} library"

    def make_symbol(
        self, python_name, c_name, return_type, argument_types, docstring=None
    ):
        """Used by python wrappers for particular drivers to register C functions on the class."""
        c_function = getattr(self._clib, c_name)
        c_function.restype = return_type
        c_function.argtypes = argument_types
        if docstring is not None:
            c_function.__doc__ = docstring
        # make the functions available under *both* their original and generic names
        setattr(self, python_name, c_function)
        setattr(self, c_name, c_function)
