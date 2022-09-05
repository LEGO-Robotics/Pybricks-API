"""ABM-decorating pybricks.pupdevices.ColorDistanceSensor."""


from ....pupdevices import ColorDistanceSensor
from ...util import act_decor, sense_decor


# ColorDistanceSensor
# (docs.pybricks.com/en/latest/pupdevices/colordistancesensor.html#pybricks.pupdevices.ColorDistanceSensor)
# ---------------------------------------------------------------------------------------------------------
for a in (
    # docs.pybricks.com/en/latest/pupdevices/colordistancesensor.html#pybricks.pupdevices.ColorDistanceSensor.detectable_colors
    # 'detectable_colors',   # already decorated in _common.CommonColorSensor
):
    act_decor(ColorDistanceSensor, a)

for s in (
    # docs.pybricks.com/en/latest/pupdevices/colordistancesensor.html#pybricks.pupdevices.ColorDistanceSensor.color
    # 'color',   # already decorated in _common.CommonColorSensor

    # docs.pybricks.com/en/latest/pupdevices/colordistancesensor.html#pybricks.pupdevices.ColorDistanceSensor.reflection
    # 'reflection',   # already decorated in _common.CommonColorSensor

    # docs.pybricks.com/en/latest/pupdevices/colordistancesensor.html#pybricks.pupdevices.ColorDistanceSensor.ambient
    # 'ambient',   # already decorated in _common.CommonColorSensor

    # docs.pybricks.com/en/latest/pupdevices/colordistancesensor.html#pybricks.pupdevices.ColorDistanceSensor.distance
    'distance',

    # docs.pybricks.com/en/latest/pupdevices/colordistancesensor.html#pybricks.pupdevices.ColorDistanceSensor.hsv
    # 'hsv',   # already decorated in _common.CommonColorSensor
):
    sense_decor(ColorDistanceSensor, s)
