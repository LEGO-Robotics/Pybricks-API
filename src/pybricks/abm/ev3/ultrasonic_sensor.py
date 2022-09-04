"""ABM-decorating pybricks.ev3devices.UltrasonicSensor."""


from ...ev3devices import UltrasonicSensor
from ..util import sense_decor


# UltrasonicSensor
# (pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.UltrasonicSensor)
# -----------------------------------------------------------------------------------
for s in (
    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.UltrasonicSensor.distance
    'distance',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.UltrasonicSensor.presence
    'presence',
):
    sense_decor(UltrasonicSensor, s)
