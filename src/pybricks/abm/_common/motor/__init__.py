"""ABM-decorating pybricks._common.Motor."""


from ...._common import Motor
from ...util import act_decor, sense_decor
from . import control, dc   # noqa: F401


# Motor
# -----
for a in (
    'reset_angle',
    'hold',
    'run',
    'run_time',
    'run_angle',
    'run_target',
    'run_until_stalled',
    'track_target',
):
    act_decor(Motor, a)

for s in (
    'angle',
    'speed',
):
    sense_decor(Motor, s)
