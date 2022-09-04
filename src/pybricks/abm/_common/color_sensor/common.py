"""ABM-decorating pybricks._common.CommonColorSensor."""


from ...._common import CommonColorSensor
from ...util import act_decor, sense_decor


# CommonColorSensor
# -----------------
for a in (
    'detectable_colors',   # *** NOTE: OVERLOADED METHOD ***
):
    act_decor(CommonColorSensor, a)

for s in (
    'color',
    'hsv',
    'ambient',
    'reflection',
):
    sense_decor(CommonColorSensor, s)
