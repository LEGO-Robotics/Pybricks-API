"""ABM-decorated Pybricks actuating & sensing functionalities."""


from abm.decor import act, sense

from .robotics import DriveBase
from .tools import StopWatch
from . import tools


def decor(cls: type, method_name: str, decorator: callable, /):
    """Decorate class method with."""
    setattr(cls, method_name, decorator(getattr(cls, method_name)))


# robotics
# (docs.pybricks.com/en/latest/robotics.html)
# ===========================================

# DriveBase
# (docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase)
# -----------------------------------------------------------------------
for a in (
    # docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.straight
    'straight',

    # docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.turn
    'turn',

    # docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.curve
    'curve',

    # docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.settings
    'settings',

    # docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.drive
    'drive',

    # docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.stop
    'stop',

    # docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.reset
    'reset',
):
    decor(DriveBase, a, act)

for s in (
    # docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.distance
    'distance',

    # docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.angle
    'angle',

    # docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.state
    'state',
):
    decor(DriveBase, s, sense)


# tools
# (docs.pybricks.com/en/latest/tools)
# ===================================

# StopWatch
# (docs.pybricks.com/en/latest/tools/#pybricks.tools.StopWatch)
# -------------------------------------------------------------
for a in (
    # docs.pybricks.com/en/latest/tools/index.html#pybricks.tools.StopWatch.pause
    'pause',

    # docs.pybricks.com/en/latest/tools/index.html#pybricks.tools.StopWatch.resume
    'resume',

    # docs.pybricks.com/en/latest/tools/index.html#pybricks.tools.StopWatch.reset
    'reset',
):
    decor(StopWatch, a, act)

for s in (
    # docs.pybricks.com/en/latest/tools/index.html#pybricks.tools.StopWatch.time
    'time',
):
    decor(StopWatch, s, sense)

# wait
# (docs.pybricks.com/en/latest/tools/index.html#pybricks.tools.wait)
# ------------------------------------------------------------------
tools.wait: callable = act(tools.wait)
