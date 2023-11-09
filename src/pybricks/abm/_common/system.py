"""ABM-decorating pybricks._common.System."""


from ..._common import System
from ..util import act_decor, sense_decor


# System
# ------
for a in (
    'set_stop_button',
    'shutdown',
):
    act_decor(System, a)

for s in (
    'reset_reason',
    'name',
):
    sense_decor(System, s)
