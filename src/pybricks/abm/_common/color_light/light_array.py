"""ABM-decorating pybricks._common.LightArray."""


from ...._common import LightArray
from ...util import act_decor


# LightArray
# ----------
for a in (
    'on',
    'off',
):
    act_decor(LightArray, a)
