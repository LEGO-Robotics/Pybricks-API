"""ABM-decorating pybricks.nxtdevices.UltrasonicSensor."""


from ...nxtdevices import UltrasonicSensor
from ..util import sense_decor


# UltrasonicSensor
# (pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.UltrasonicSensor)
# ------------------------------------------------------------------------------
for s in (
    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.UltrasonicSensor.distance
    'distance',
):
    sense_decor(UltrasonicSensor, s)
