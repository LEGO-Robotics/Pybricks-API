"""ABM-decorating pybricks.nxtdevices.TouchSensor."""


from ...nxtdevices import TouchSensor
from ..util import sense_decor


# TouchSensor
# (pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.TouchSensor)
# -------------------------------------------------------------------------
for s in (
    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.TouchSensor.pressed
    'pressed',
):
    sense_decor(TouchSensor, s)
