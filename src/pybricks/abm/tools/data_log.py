"""ABM-decorating pybricks.tools.DataLog."""


from ...tools import DataLog
from ..util import act_decor


# DataLog
# (pybricks.com/ev3-micropython/tools#pybricks.tools.DataLog)
# -----------------------------------------------------------
for a in (
    # pybricks.com/ev3-micropython/tools#pybricks.tools.DataLog.log
    'log',
):
    act_decor(DataLog, a)
