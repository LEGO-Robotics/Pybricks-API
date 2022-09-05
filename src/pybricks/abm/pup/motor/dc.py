"""ABM-decorating pybricks.pupdevices.DCMotor."""


from ....pupdevices import DCMotor
from ...util import act_decor


# DCMotor
# (docs.pybricks.com/en/latest/pupdevices/dcmotor.html#pybricks.pupdevices.DCMotor)
# ---------------------------------------------------------------------------------
for a in (
    # 'dc',   # already decorated in _common.DCMotor
    # 'stop',   # already decorated in _common.DCMotor
    # 'brake',   # already decorated in _common.DCMotor
    # 'settings',   # already decorated in _common.DCMotor
):
    act_decor(DCMotor, a)
