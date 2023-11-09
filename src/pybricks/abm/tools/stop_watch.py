"""ABM-decorating pybricks.tools.StopWatch."""


from ...tools import StopWatch
from ..util import act_decor, sense_decor


# StopWatch
# (docs.pybricks.com/en/latest/tools#pybricks.tools.StopWatch)
# ------------------------------------------------------------
for a in (
    # docs.pybricks.com/en/latest/tools#pybricks.tools.StopWatch.pause
    'pause',

    # docs.pybricks.com/en/latest/tools#pybricks.tools.StopWatch.resume
    'resume',

    # docs.pybricks.com/en/latest/tools#pybricks.tools.StopWatch.reset
    'reset',
):
    act_decor(StopWatch, a)

for s in (
    # docs.pybricks.com/en/latest/tools#pybricks.tools.StopWatch.time
    'time',
):
    sense_decor(StopWatch, s)
