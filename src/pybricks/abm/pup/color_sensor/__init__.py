"""ABM-decorating pybricks.pupdevices.ColorSensor."""


from ....pupdevices import ColorSensor
from ...util import act_decor, sense_decor
from . import distance   # noqa: F401


# ColorSensor
# (docs.pybricks.com/en/latest/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor)
# -----------------------------------------------------------------------------------------
for a in (
    # docs.pybricks.com/en/latest/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor.detectable_colors
    'detectable_colors',   # *** NOTE: OVERLOADED METHOD ***
):
    act_decor(ColorSensor, a)

for s in (
    # docs.pybricks.com/en/latest/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor.color
    'color',

    # docs.pybricks.com/en/latest/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor.reflection
    'reflection',

    # docs.pybricks.com/en/latest/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor.ambient
    'ambient',

    # docs.pybricks.com/en/latest/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor.hsv
    'hsv',
):
    sense_decor(ColorSensor, s)
