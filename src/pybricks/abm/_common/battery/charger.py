"""ABM-decorating pybricks._common.Charger."""


from ...._common import Charger
from ...util import sense_decor


# Charger
# -------
for s in (
    'connected',
    'status',
    'current',
):
    sense_decor(Charger, s)
