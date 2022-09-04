"""ABM-decorating pybricks.ev3devices.Motor."""


from ...ev3devices import Motor
from ..util import act_decor, sense_decor


# Motor
# (pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor)
# -------------------------------------------------------------------
for a in (
    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.reset_angle
    'reset_angle',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.stop
    'stop',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.brake
    'brake',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.hold
    'hold',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.run
    'run',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.run_time
    'run_time',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.run_angle
    'run_angle',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.run_target
    'run_target',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.run_until_stalled
    'run_until_stalled',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.dc
    'dc',
):
    act_decor(Motor, a)

for s in (
    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.speed
    'speed',

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.angle
    'angle',
):
    sense_decor(Motor, s)
