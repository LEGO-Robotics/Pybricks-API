"""ABM-decorating pybricks._common.Battery."""


from ...._common import Battery
from ...util import sense_decor
from . import charger   # noqa: F401


# Battery
# -------
for s in (
    'voltage',
    'current',
):
    sense_decor(Battery, s)
