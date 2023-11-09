"""ABM-decorating pybricks.pupdevices.Motor."""


from ....pupdevices import Motor
from ...util import act_decor, sense_decor
from . import dc, pf   # noqa: F401


# Motor
# (docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor)
# -----------------------------------------------------------------------------
for a in (
    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.reset_angle
    # 'reset_angle',   # already decorated in _common.Motor

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.stop
    # 'stop',   # already decorated in _common.DCMotor

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.brake
    # 'brake',   # already decorated in _common.DCMotor

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.hold
    # 'hold',   # already decorated in _common.Motor

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.run
    # 'run',   # already decorated in _common.Motor

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.run_time
    # 'run_time',   # already decorated in _common.Motor

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.run_angle
    # 'run_angle',   # already decorated in _common.Motor

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.run_target
    # 'run_target',   # already decorated in _common.Motor

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.track_target
    # 'track_target',   # already decorated in _common.Motor

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.run_until_stalled
    # 'run_until_stalled',   # already decorated in _common.Motor

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.dc
    # 'dc',   # already decorated in _common.DCMotor

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.settings
    # 'settings',   # already decorated in _common.DCMotor
):
    act_decor(Motor, a)

for s in (
    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.speed
    # 'speed',   # already decorated in _common.Motor

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.angle
    # 'angle',   # already decorated in _common.Motor
):
    sense_decor(Motor, s)
