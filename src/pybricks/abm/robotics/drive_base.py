"""ABM-decorating pybricks.robotics.DriveBase."""


from ...robotics import DriveBase
from ..util import act_decor, sense_decor


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
    act_decor(DriveBase, a)

for s in (
    # docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.distance
    'distance',

    # docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.angle
    'angle',

    # docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.state
    'state',
):
    sense_decor(DriveBase, s)
