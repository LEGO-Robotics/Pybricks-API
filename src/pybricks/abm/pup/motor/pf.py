"""ABM-decorating pybricks.pupdevices.PFMotor."""


from ....pupdevices import PFMotor
from ...util import act_decor


# PFMotor
# (docs.pybricks.com/en/latest/pupdevices/pfmotor.html)
# -----------------------------------------------------
for a in (
    'dc',
    'stop',
    'brake',
):
    act_decor(PFMotor, a)
