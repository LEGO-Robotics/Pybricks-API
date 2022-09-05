"""ABM-decorating pybricks.pupdevices.PFMotor."""


from ....pupdevices import PFMotor
from ...util import act_decor


# PFMotor
# (docs.pybricks.com/en/latest/pupdevices/pfmotor.html)
# -----------------------------------------------------
for a in (
    # 'dc',   # already decorated in _common.DCMotor
    # 'stop',   # already decorated in _common.DCMotor
    # 'brake',   # already decorated in _common.DCMotor
):
    act_decor(PFMotor, a)
