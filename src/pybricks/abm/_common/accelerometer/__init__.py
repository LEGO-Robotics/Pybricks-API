"""ABM-decorating pybricks._common.Accelerometer."""


from ...._common import Accelerometer
from ...util import sense_decor
from . import simple, imu   # noqa: F401


# Accelerometer
# -------------
for s in (
    'acceleration',
    'tilt',
):
    sense_decor(Accelerometer, s)
