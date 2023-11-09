"""ABM-decorating pybricks.pupdevices.Light."""


from ...pupdevices import Light
from ..util import act_decor


# Light
# (docs.pybricks.com/en/latest/pupdevices/light.html#pybricks.pupdevices.Light)
# -----------------------------------------------------------------------------
for a in (
    # docs.pybricks.com/en/latest/pupdevices/light.html#pybricks.pupdevices.Light.on
    'on',

    # docs.pybricks.com/en/latest/pupdevices/light.html#pybricks.pupdevices.Light.off
    'off',
):
    act_decor(Light, a)
