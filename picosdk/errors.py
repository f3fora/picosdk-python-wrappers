#
# Copyright (C) 2019 Pico Technology Ltd. See LICENSE file for terms.
#

from picosdk.constants import PicoStatus


class PicoError(Exception):
    """All errors thrown explicitly by this package will be PicoError's."""

    pass


class FeatureNotSupportedError(PicoError):
    """raised when a feature is not supported on the connected device."""

    pass


class CannotFindPicoSDKError(PicoError, IOError):
    pass


class CannotOpenPicoSDKError(PicoError, IOError):
    pass


class DeviceNotFoundError(PicoError, IOError):
    pass


class ArgumentOutOfRangeError(PicoError, ValueError):
    pass


class ValidRangeEnumValueNotValidForThisDevice(FeatureNotSupportedError, ValueError):
    pass


class DeviceCannotSegmentMemoryError(FeatureNotSupportedError, TypeError):
    pass


class InvalidMemorySegmentsError(PicoError, ValueError):
    pass


class InvalidTimebaseError(PicoError, ValueError):
    pass


class InvalidTriggerParameters(PicoError, ValueError):
    pass


class InvalidCaptureParameters(PicoError, ValueError):
    pass


class PicoSDKCtypesError(PicoError, IOError):
    def __init__(self, status: PicoStatus, *args):
        super().__init__(*args)
        self.status = status
        super().__init__(f"PicoSDKCtypesError {self.status.value}: {self.status.name}")

    def __str__(self):
        return f"PicoSDKCtypesError {self.status.value}: {self.status.name}"

    def __repr__(self):
        return f"PicoSDKCtypesError(status={self.status})"


class ClosedDeviceError(PicoError, IOError):
    pass


class NoChannelsEnabledError(PicoError, ValueError):
    pass


class NoValidTimebaseForOptionsError(PicoError, ValueError):
    pass


class UnknownConstantError(PicoError, TypeError):
    pass
