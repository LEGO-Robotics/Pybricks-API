"""ABM-decorating pybricks._common.Keypad."""


from ..._common import Keypad
from ..util import sense_decor


# Keypad
# ------
for s in (
    'pressed',
):
    sense_decor(Keypad, s)
