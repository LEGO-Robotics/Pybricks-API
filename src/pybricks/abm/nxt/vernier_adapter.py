"""ABM-decorating pybricks.nxtdevices.VernierAdapter."""


from ...nxtdevices import VernierAdapter
from ..util import sense_decor


# VernierAdapter
# (pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.VernierAdapter)
# ----------------------------------------------------------------------------
for s in (
    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.VernierAdapter.voltage
    'voltage',

    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.VernierAdapter.conversion
    'conversion',

    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.VernierAdapter.value
    'value',
):
    sense_decor(VernierAdapter, s)
