"""ABM-decorating pybricks.iodevices.AnalogSensor."""


from ...iodevices import AnalogSensor
from ..util import act_decor, sense_decor


# AnalogSensor
# (pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.AnalogSensor)
# ------------------------------------------------------------------------
for a in (
    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.AnalogSensor.active
    'active',

    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.AnalogSensor.passive
    'passive',
):
    act_decor(AnalogSensor, a)

for s in (
    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.AnalogSensor.voltage
    'voltage',

    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.AnalogSensor.resistance
    'resistance',
):
    sense_decor(AnalogSensor, s)
