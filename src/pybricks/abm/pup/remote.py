"""ABM-decorating pybricks.pupdevices.Remote."""


from ...pupdevices import Remote
from ..util import act_decor


# Remote
# (docs.pybricks.com/en/latest/pupdevices/remote.html#pybricks.pupdevices.Remote)
# -------------------------------------------------------------------------------
for a in (
    # docs.pybricks.com/en/latest/pupdevices/remote.html#pybricks.pupdevices.Remote.name
    'name',   # *** NOTE: OVERLOADED METHOD ***
):
    act_decor(Remote, a)
