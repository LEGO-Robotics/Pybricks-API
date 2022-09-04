"""ABM-decorating pybricks.nxtdevices.EnergyMeter."""


from ...nxtdevices import EnergyMeter
from ..util import sense_decor


# EnergyMeter
# (pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.EnergyMeter)
# -------------------------------------------------------------------------
for s in (
    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.EnergyMeter.storage
    'storage',

    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.EnergyMeter.input
    'input',

    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.EnergyMeter.output
    'output',
):
    sense_decor(EnergyMeter, s)
