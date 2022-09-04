"""ABM-decorating pybricks.pupdevices.Motor."""


from ....pupdevices import Motor
from ...util import act_decor, sense_decor
from . import dc, pf   # noqa: F401


# Motor
# (docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor)
# -----------------------------------------------------------------------------
for a in (
    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.reset_angle
    'reset_angle',

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.stop
    'stop',

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.brake
    'brake',

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.hold
    'hold',

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.run
    'run',

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.run_time
    'run_time',

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.run_angle
    'run_angle',

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.run_target
    'run_target',

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.track_target
    'track_target',

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.run_until_stalled
    'run_until_stalled',

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.dc
    'dc',

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.settings
    'settings',   # *** NOTE: OVERLOADED METHOD ***
):
    act_decor(Motor, a)

for s in (
    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.speed
    'speed',

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.angle
    'angle',
):
    sense_decor(Motor, s)
