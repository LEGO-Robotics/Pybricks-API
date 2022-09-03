"""ABM-decorated Pybricks actuating & sensing functionalities."""


from abm.decor import act, sense

from .robotics import DriveBase


def decor(cls: type, method_name: str, decorator: callable, /):
    """Decorate class method with."""
    setattr(cls, method_name, decorator(getattr(cls, method_name)))


# robotics.DriveBase
# ==================
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
