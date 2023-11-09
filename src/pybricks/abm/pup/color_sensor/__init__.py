"""ABM-decorating pybricks.pupdevices.ColorSensor."""


from ....pupdevices import ColorSensor
from ...util import act_decor, sense_decor
from . import distance   # noqa: F401


# ColorSensor
# (docs.pybricks.com/en/latest/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor)
# -----------------------------------------------------------------------------------------
for a in (
    # docs.pybricks.com/en/latest/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor.detectable_colors
    # 'detectable_colors',   # already decorated in _common.CommonColorSensor
):
    act_decor(ColorSensor, a)

for s in (
    # docs.pybricks.com/en/latest/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor.color
    # 'color',   # already decorated in _common.AmbientColorSensor

    # docs.pybricks.com/en/latest/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor.reflection
    # 'reflection',   # already decorated in _common.CommonColorSensor

    # docs.pybricks.com/en/latest/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor.ambient
    # 'ambient',   # already decorated in _common.CommonColorSensor

    # docs.pybricks.com/en/latest/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor.hsv
    # 'hsv',   # already decorated in _common.AmbientColorSensor
):
    sense_decor(ColorSensor, s)
