"""ABM-decorating pybricks.pupdevices.DCMotor."""


from ....pupdevices import DCMotor
from ...util import act_decor


# DCMotor
# (docs.pybricks.com/en/latest/pupdevices/dcmotor.html#pybricks.pupdevices.DCMotor)
# ---------------------------------------------------------------------------------
for a in (
    'dc',
    'stop',
    'brake',
    'settings',   # *** NOTE: OVERLOADED METHOD ***
):
    act_decor(DCMotor, a)
