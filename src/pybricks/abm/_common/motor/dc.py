"""ABM-decorating pybricks._common.DCMotor"""


from ...._common import DCMotor
from ...util import act_decor


# DCMotor
# -------
for dc_motor_act in (
    'dc',
    'stop',
    'brake',
    'settings',   # *** NOTE: OVERLOADED METHOD ***
):
    act_decor(DCMotor, dc_motor_act)
