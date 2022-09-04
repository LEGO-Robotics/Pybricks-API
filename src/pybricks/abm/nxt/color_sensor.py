"""ABM-decorating pybricks.nxtdevices.ColorSensor."""


from ...nxtdevices import ColorSensor
from ..util import sense_decor


# ColorSensor
# (pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.ColorSensor)
# -------------------------------------------------------------------------
for s in (
    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.ColorSensor.color
    'color',

    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.ColorSensor.ambient
    'ambient',

    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.ColorSensor.reflection
    'reflection',

    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.ColorSensor.rgb
    'rgb',
):
    sense_decor(ColorSensor, s)
