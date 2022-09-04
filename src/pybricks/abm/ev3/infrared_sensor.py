"""ABM-decorating pybricks.ev3devices.InfraredSensor."""


from ...ev3devices import InfraredSensor
from ..util import sense_decor


# InfraredSensor
# (pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.InfraredSensor)
# ----------------------------------------------------------------------------
for s in (
    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.InfraredSensor.distance
    'distance',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.InfraredSensor.beacon
    'beacon',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.InfraredSensor.buttons
    'buttons',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.InfraredSensor.keypad
    'keypad',
):
    sense_decor(InfraredSensor, s)
