from enum import Enum, auto


class ExternalFrequency(Enum):
    frequency_off = 0
    frequency_5MHz = auto()
    frequency_10MHz = auto()
    frequency_20MHz = auto()
    frequency_25MHz = auto()
    max_frequencies = auto()


class BandwidthLimiter(Enum):
    bw_full = 0
    bw_20MHz = auto()
    bw_25MHz = auto()


class Channel(Enum):
    channel_A = 0
    channel_B = auto()
    channel_C = auto()
    channel_D = auto()
    external = auto()
    max_channels = external
    trigger_aux = auto()
    max_trigger_sources = auto()


class ChannelBufferIndex(Enum):
    channel_A_max = 0
    channel_A_min = auto()
    channel_B_max = auto()
    channel_B_min = auto()
    channel_C_max = auto()
    channel_C_min = auto()
    channel_D_max = auto()
    channel_D_min = auto()
    max_channel_buffers = auto()


class Range(Enum):
    range_10mV = 0
    range_20mV = auto()
    range_50mV = auto()
    range_100mV = auto()
    range_200mV = auto()
    range_500mV = auto()
    range_1V = auto()
    range_2V = auto()
    range_5V = auto()
    range_10V = auto()
    range_20V = auto()
    range_50V = auto()
    max_ranges = auto()


class Coupling(Enum):
    AC = 0
    DC_1M = auto()
    DC_50r = auto()


class EtsMode(Enum):
    # ETS disabled
    off = 0
    # Return ready as soon as requested no of interleaves is available
    fast = auto()
    # Return ready every time a new set of no_of_cycles is collected
    slow = auto()
    modes_max = auto()


class TimeUnits(Enum):
    fs = 0
    ps = auto()
    ns = auto()
    us = auto()
    ms = auto()
    s = auto()
    max_time_units = auto()


class SweepType(Enum):
    up = 0
    down = auto()
    updown = auto()
    downup = auto()
    max_sweep_types = auto()


class WaveType(Enum):
    sine = 0
    square = auto()
    triangle = auto()
    ramp_up = auto()
    ramp_down = auto()
    sinc = auto()
    gaussian = auto()
    half_sine = auto()
    dc_voltage = auto()
    max_wave_types = auto()


class ExtraOperations(Enum):
    es_off = 0
    whitenoise = auto()
    prbs = auto()  # pseudo-random bit stream


class SigGenTrigType(Enum):
    rising = 0
    falling = auto()
    gate_high = auto()
    gate_low = auto()


class SigGenTrigSource(Enum):
    none = 0
    scope_trig = auto()
    aux_in = auto()
    ext_in = auto()
    soft_trig = auto()
    trigger_raw = auto()


class IndexMode(Enum):
    single = 0
    dual = auto()
    quad = auto()
    max_index_modes = auto()


class ThresholdMode(Enum):
    level = 0
    window = auto()


class ThresholdDirection(Enum):
    above = 0  # using upper threshold
    below = auto()  # using upper threshold
    rising = auto()  # using upper threshold
    falling = auto()  # using upper threshold
    rising_or_falling = auto()  # using upper threshold
    above_lower = auto()  # using lower threshold
    below_lower = auto()  # using lower threshold
    rising_lower = auto()  # using lower threshold
    falling_lower = auto()  # using lower threshold
    # Windowing using both thresholds
    inside = above
    outside = below
    enter = rising
    exit = falling
    enter_or_exit = rising_or_falling
    positive_runt = 9
    negative_runt = auto()
    # no trigger set
    none = rising


class TriggerState(Enum):
    dont_care = 0
    true = auto()
    false = auto()
    max = auto()


class RatioMode(Enum):
    none = 0
    aggregate = 1
    average = 2
    decimate = 4
    distribution = 8


class PulseWidthType(Enum):
    none = 0
    less_than = auto()
    greater_than = auto()
    in_range = auto()
    out_of_range = auto()


class Temperatures(Enum):
    what_are_available = 0
    internal_temperature = 1


class PicoInfo(Enum):
    driver_version = 0
    usb_version = 1
    hardware_version = 2
    variant_info = 3
    batch_and_serial = 4
    cal_date = 5
    kernal_version = 6
    digital_hardware_version = 7
    analogue_hardware_version = 8
    firmware_version_1 = 9
    fireware_version_2 = ord("A")
