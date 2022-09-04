"""ABM-decorating pybricks._common.DCMotor"""


from ...._common import DCMotor
from ...util import act_decor


# DCMotor
# -------
for a in (
    'dc',
    'stop',
    'brake',
    'settings',   # *** NOTE: OVERLOADED METHOD ***
):
    act_decor(DCMotor, a)
