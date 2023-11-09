"""ABM-decorating pybricks.iodevices.Ev3devSensor."""


from ...iodevices import Ev3devSensor
from ..util import sense_decor


# Ev3devSensor
# (pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.Ev3devSensor)
# ------------------------------------------------------------------------
for s in (
    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.Ev3devSensor.read
    'read',
):
    sense_decor(Ev3devSensor, s)
