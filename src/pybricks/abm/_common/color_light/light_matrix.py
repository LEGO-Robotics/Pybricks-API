"""ABM-decorating pybricks._common.LightMatrix."""


from ...._common import LightMatrix
from ...util import act_decor


# LightMatrix
# -----------
for a in (
    'orientation',
    'image',
    'animate',
    'pixel',
    'off',
    'number',
    'char',
    'text',
):
    act_decor(LightMatrix, a)
