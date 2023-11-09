"""ABM-decorating pybricks.ev3devices.ColorSensor."""


from ...ev3devices import ColorSensor
from ..util import sense_decor


# ColorSensor
# (pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.ColorSensor)
# -------------------------------------------------------------------------
for s in (
    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.ColorSensor.color
    'color',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.ColorSensor.ambient
    'ambient',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.ColorSensor.reflection
    'reflection',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.ColorSensor.rgb
    'rgb',
):
    sense_decor(ColorSensor, s)
