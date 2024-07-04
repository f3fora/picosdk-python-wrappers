from ctypes import c_uint32, c_uint16, c_int16, Structure, c_uint64


class TriggerConditions(Structure):
    _pack_ = 1
    _fields_ = [
        ("channelA", c_uint32),
        ("channelB", c_uint32),
        ("channelC", c_uint32),
        ("channelD", c_uint32),
        ("external", c_uint32),
        ("aux", c_uint32),
        ("pulseWidthQualifier", c_uint32),
    ]


class TriggerChannelProperties(Structure):
    _pack_ = 1
    _fields_ = [
        ("thresholdUpper", c_int16),
        ("hysteresisUpper", c_uint16),
        ("thresholdLower", c_int16),
        ("hysteresisLower", c_uint16),
        ("channel", c_uint32),
        ("thresholdMode", c_uint32),
    ]


class PwqConditions(Structure):
    _pack_ = 1
    _fields_ = [
        ("channelA", c_uint32),
        ("channelB", c_uint32),
        ("channelC", c_uint32),
        ("channelD", c_uint32),
        ("external", c_uint32),
        ("aux", c_uint32),
    ]


class TriggerInfo(Structure):
    _pack_ = 1
    _fields_ = [
        ("status", c_uint32),
        ("segmentIndex", c_uint32),
        ("triggerIndex", c_uint32),
        ("triggerTime", c_uint64),
        ("timeUnits", c_uint16),
        ("reserved0", c_uint16),
        ("timeStampCounter", c_uint64),
    ]
