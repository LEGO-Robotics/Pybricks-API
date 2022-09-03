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
from .ev3dev._speaker import Speaker as EV3Speaker
from .robotics import DriveBase
from .tools import DataLog, StopWatch
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

# EV3Speaker
# ----------
for a in (
    # pybricks.com/ev3-micropython/hubs#pybricks.hubs.EV3Brick.speaker.beep
    'beep',

    # pybricks.com/ev3-micropython/hubs#pybricks.hubs.EV3Brick.speaker.play_notes
    'play_notes',

    # pybricks.com/ev3-micropython/hubs#pybricks.hubs.EV3Brick.speaker.play_file
    'play_file',

    # pybricks.com/ev3-micropython/hubs#pybricks.hubs.EV3Brick.speaker.say
    'say',

    # pybricks.com/ev3-micropython/hubs#pybricks.hubs.EV3Brick.speaker.set_speech_options
    'set_speech_options',

    # pybricks.com/ev3-micropython/hubs#pybricks.hubs.EV3Brick.speaker.set_volume
    'set_volume',
):
    decor(EV3Speaker, a, act)


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

# DataLog
# (pybricks.com/ev3-micropython/tools#pybricks.tools.DataLog)
# -----------------------------------------------------------
for data_log_act in (
    # pybricks.com/ev3-micropython/tools#pybricks.tools.DataLog.log
    'log',
):
    decor(DataLog, data_log_act, act)

# StopWatch
# (docs.pybricks.com/en/latest/tools/#pybricks.tools.StopWatch)
# -------------------------------------------------------------
for stop_watch_act in (
    # docs.pybricks.com/en/latest/tools/index.html#pybricks.tools.StopWatch.pause
    'pause',

    # docs.pybricks.com/en/latest/tools/index.html#pybricks.tools.StopWatch.resume
    'resume',

    # docs.pybricks.com/en/latest/tools/index.html#pybricks.tools.StopWatch.reset
    'reset',
):
    decor(StopWatch, stop_watch_act, act)

for stop_watch_sense in (
    # docs.pybricks.com/en/latest/tools/index.html#pybricks.tools.StopWatch.time
    'time',
):
    decor(StopWatch, stop_watch_sense, sense)

# wait
# (docs.pybricks.com/en/latest/tools/index.html#pybricks.tools.wait)
# ------------------------------------------------------------------
tools.wait: callable = act(tools.wait)
