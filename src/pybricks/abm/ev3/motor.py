"""ABM-decorating pybricks.ev3devices.Motor."""


from ...ev3devices import Motor
from ..util import act_decor, sense_decor


# Motor
# (pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor)
# -------------------------------------------------------------------
for a in (
    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.reset_angle
    # 'reset_angle',   # already decorated in _common.Motor

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.stop
    # 'stop',   # already decorated in _common.DCMotor

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.brake
    # 'brake',   # already decorated in _common.DCMotor

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.hold
    # 'hold',   # already decorated in _common.Motor

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.run
    # 'run',   # already decorated in _common.Motor

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.run_time
    # 'run_time',   # already decorated in _common.Motor

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.run_angle
    # 'run_angle',   # already decorated in _common.Motor

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.run_target
    # 'run_target',   # already decorated in _common.Motor

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.run_until_stalled
    # 'run_until_stalled',   # already decorated in _common.Motor

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.dc
    # 'dc',   # already decorated in _common.DCMotor
):
    act_decor(Motor, a)

for s in (
    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.speed
    # 'speed',   # already decorated in _common.Motor

    # pybricks.com/ev3-micropython/ev3devices#pybricks.ev3devices.Motor.angle
    # 'angle',   # already decorated in _common.Motor
):
    sense_decor(Motor, s)
