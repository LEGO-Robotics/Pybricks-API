"""ABM-decorating pybricks.pupdevices.ColorDistanceSensor."""


from ....pupdevices import ColorDistanceSensor
from ...util import act_decor, sense_decor


# ColorDistanceSensor
# (docs.pybricks.com/en/latest/pupdevices/colordistancesensor.html#pybricks.pupdevices.ColorDistanceSensor)
# ---------------------------------------------------------------------------------------------------------
for a in (
    # docs.pybricks.com/en/latest/pupdevices/colordistancesensor.html#pybricks.pupdevices.ColorDistanceSensor.detectable_colors
    'detectable_colors',   # *** NOTE: OVERLOADED METHOD ***
):
    act_decor(ColorDistanceSensor, a)

for s in (
    # docs.pybricks.com/en/latest/pupdevices/colordistancesensor.html#pybricks.pupdevices.ColorDistanceSensor.color
    'color',

    # docs.pybricks.com/en/latest/pupdevices/colordistancesensor.html#pybricks.pupdevices.ColorDistanceSensor.reflection
    'reflection',

    # docs.pybricks.com/en/latest/pupdevices/colordistancesensor.html#pybricks.pupdevices.ColorDistanceSensor.ambient
    'ambient',

    # docs.pybricks.com/en/latest/pupdevices/colordistancesensor.html#pybricks.pupdevices.ColorDistanceSensor.distance
    'distance',

    # docs.pybricks.com/en/latest/pupdevices/colordistancesensor.html#pybricks.pupdevices.ColorDistanceSensor.hsv
    'hsv',
):
    sense_decor(ColorDistanceSensor, s)
