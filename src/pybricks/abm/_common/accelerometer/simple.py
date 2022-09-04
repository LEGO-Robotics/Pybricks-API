"""ABM-decorating pybricks._common.SimpleAccelerometer."""


from ...._common import SimpleAccelerometer
from ...util import sense_decor


# SimpleAccelerometer
# -------------------
for s in (
    'acceleration',
    'up',
):
    sense_decor(SimpleAccelerometer, s)
