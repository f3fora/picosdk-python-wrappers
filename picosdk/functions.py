#
# Copyright (C) 2018 Pico Technology Ltd. See LICENSE file for terms.
#
from __future__ import division
from picosdk.constants import PicoStatus
from picosdk.errors import PicoSDKCtypesError


def ok(status):
    # checks for PICO_OK status return
    status = PicoStatus(status)
    if status != PicoStatus.ok:
        raise PicoSDKCtypesError(status)
