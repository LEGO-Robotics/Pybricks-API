"""ABM-decorating pybricks.nxtdevices.LightSensor."""


from ...nxtdevices import LightSensor
from ..util import sense_decor


# LightSensor
# (pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.LightSensor)
# -------------------------------------------------------------------------
for s in (
    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.LightSensor.ambient
    'ambient',

    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.LightSensor.reflection
    'reflection',
):
    sense_decor(LightSensor, s)
