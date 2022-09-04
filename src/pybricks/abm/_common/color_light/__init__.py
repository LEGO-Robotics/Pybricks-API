"""ABM-decorating pybricks._common.ColorLight."""


from ...._common import ColorLight
from ...util import act_decor
from . import light_array, light_matrix   # noqa: F401


# ColorLight
# ----------
for a in (
    'on',
    'off',
    'blink',
    'animate',
):
    act_decor(ColorLight, a)
