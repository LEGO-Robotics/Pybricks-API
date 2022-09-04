"""ABM-decorating pybricks.ev3devices.GyroSensor."""


from ...ev3devices import GyroSensor
from ..util import act_decor, sense_decor


# GyroSensor
# (pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.GyroSensor)
# ------------------------------------------------------------------------
for a in (
    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.GyroSensor.reset_angle
    'reset_angle',
):
    act_decor(GyroSensor, a)

for s in (
    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.GyroSensor.speed
    'speed',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.GyroSensor.angle
    'angle',
):
    sense_decor(GyroSensor, s)
