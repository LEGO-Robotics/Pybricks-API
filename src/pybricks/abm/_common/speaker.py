"""ABM-decorating pybricks._common.Speaker."""


from ..._common import Speaker
from ..util import act_decor


# Speaker
# -------
for a in (
    'volume',
    'beep',
    'play_notes',

):
    act_decor(Speaker, a)
