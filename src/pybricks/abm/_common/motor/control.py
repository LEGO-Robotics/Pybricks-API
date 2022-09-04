"""ABM-decorating pybricks._common.Control."""


from ...._common import Control
from ...util import act_decor, sense_decor


# Control
# -------
for a in (
    'limits',   # *** NOTE: OVERLOADED METHOD ***
    'pid',   # *** NOTE: OVERLOADED METHOD ***
    'target_tolerances',   # *** NOTE: OVERLOADED METHOD ***
    'stall_tolerances',   # *** NOTE: OVERLOADED METHOD ***
):
    act_decor(Control, a)

for s in (
    'stalled',
    'done',
    'load',
):
    sense_decor(Control, s)
