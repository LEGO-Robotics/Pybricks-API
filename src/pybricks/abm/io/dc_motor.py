"""ABM-decorating pybricks.iodevices.DCMotor."""


from ...iodevices import DCMotor
from ..util import act_decor


# DCMotor
# (pybricks.com/ev3-micropython/iodevices#dc-motor)
# -------------------------------------------------
for a in (
    # 'dc',   # already decorated in _common.DCMotor
    # 'stop',   # already decorated in _common.DCMotor
):
    act_decor(DCMotor, a)
