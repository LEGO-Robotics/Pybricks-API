"""ABM-decorating pybricks.pupdevices.ForceSensor."""


from ...pupdevices import ForceSensor
from ..util import sense_decor


# ForceSensor
# (docs.pybricks.com/en/latest/pupdevices/forcesensor.html#pybricks.pupdevices.ForceSensor)
# -----------------------------------------------------------------------------------------
for s in (
    # docs.pybricks.com/en/latest/pupdevices/forcesensor.html#pybricks.pupdevices.ForceSensor.force
    'force',

    # docs.pybricks.com/en/latest/pupdevices/forcesensor.html#pybricks.pupdevices.ForceSensor.distance
    'distance',

    # docs.pybricks.com/en/latest/pupdevices/forcesensor.html#pybricks.pupdevices.ForceSensor.pressed
    'pressed',

    # docs.pybricks.com/en/latest/pupdevices/forcesensor.html#pybricks.pupdevices.ForceSensor.touched
    'touched',
):
    sense_decor(ForceSensor, s)
