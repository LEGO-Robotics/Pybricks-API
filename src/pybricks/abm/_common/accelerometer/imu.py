"""ABM-decorating pybricks._common.IMU."""


from ...._common import IMU
from ...util import act_decor, sense_decor


# IMU
# ---
for a in (
    'reset_heading',
):
    act_decor(IMU, a)

for s in (
    'heading',
    'angular_velocity',
):
    sense_decor(IMU, s)
