"""ABM-decorating pybricks._common.AmbientColorSensor."""


from ...._common import AmbientColorSensor
from ...util import sense_decor


# AmbientColorSensor
# ------------------
for s in (
    'color',
    'hsv',
):
    sense_decor(AmbientColorSensor, s)
