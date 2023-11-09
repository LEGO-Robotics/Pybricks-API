"""ABM-decorating pybricks.ev3devices.TouchSensor."""


from ...ev3devices import TouchSensor
from ..util import sense_decor


# TouchSensor
# (pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.TouchSensor)
# -------------------------------------------------------------------------
for s in (
    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.TouchSensor.pressed
    'pressed',
):
    sense_decor(TouchSensor, s)
