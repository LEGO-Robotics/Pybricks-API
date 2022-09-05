"""ABM-decorating pybricks.nxtdevices.ColorSensor."""


from ...nxtdevices import ColorSensor
from ..util import sense_decor


# ColorSensor
# (pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.ColorSensor)
# -------------------------------------------------------------------------
for s in (
    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.ColorSensor.color
    # 'color',   # already decorated in _common.CommonColorSensor

    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.ColorSensor.ambient
    # 'ambient',   # already decorated in _common.CommonColorSensor

    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.ColorSensor.reflection
    # 'reflection',   # already decorated in _common.CommonColorSensor

    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.ColorSensor.rgb
    'rgb',
):
    sense_decor(ColorSensor, s)
