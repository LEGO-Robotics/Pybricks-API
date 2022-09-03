"""ABM-decorated Pybricks actuating & sensing functionalities."""


from abm.decor import act, sense

from .hubs import (EV3Brick,   # noqa: F401
                   InventorHub, PrimeHub, CityHub, MoveHub, TechnicHub)
from .iodevices import (AnalogSensor,   # noqa: F401
                        DCMotor,
                        Ev3devSensor,
                        I2CDevice,
                        LUMPDevice,
                        LWP3Device,
                        PUPDevice,
                        UARTDevice)
from .robotics import DriveBase
from .tools import StopWatch
from . import tools


def decor(cls: type, method_name: str, decorator: callable, /):
    """Decorate class method with."""
    setattr(cls, method_name, decorator(getattr(cls, method_name)))


# hubs
# (docs.pybricks.com/en/latest/hubs | pybricks.com/ev3-micropython/hubs)
# ======================================================================

# EV3Brick
# (pybricks.com/ev3-micropython/hubs#pybricks.hubs.EV3Brick)
# ----------------------------------------------------------
# TODO

# InventorHub
# (docs.pybricks.com/en/latest/hubs/primehub.html#InventorHub)
# ------------------------------------------------------------
# TODO

# PrimeHub
# (docs.pybricks.com/en/latest/hubs/primehub.html#pybricks.hubs.PrimeHub)
# -----------------------------------------------------------------------
# TODO

# CityHub
# (docs.pybricks.com/en/latest/hubs/cityhub.html#pybricks.hubs.CityHub)
# ---------------------------------------------------------------------
# TODO

# MoveHub
# (docs.pybricks.com/en/latest/hubs/movehub.html#pybricks.hubs.MoveHub)
# ---------------------------------------------------------------------
# TODO

# TechnicHub
# (docs.pybricks.com/en/latest/hubs/technichub.html#pybricks.hubs.TechnicHub)
# ---------------------------------------------------------------------------
# TODO


# iodevices
# (docs.pybricks.com/en/latest/iodevices)
# =======================================

# AnalogSensor
# ------------
# TODO

# DCMotor
# -------
# TODO

# Ev3devSensor
# ------------
# TODO

# I2CDevice
# ---------
# TODO

# LUMPDevice
# ----------
# TODO

# LWP3Device
# (docs.pybricks.com/en/latest/iodevices/lwp3device.html#pybricks.iodevices.LWP3Device)
# -------------------------------------------------------------------------------------
# TODO

# PUPDevice
# (docs.pybricks.com/en/latest/iodevices/pupdevice.html#pybricks.iodevices.PUPDevice)
# -----------------------------------------------------------------------------------
# TODO

# UARTDevice
# ----------
# TODO


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
