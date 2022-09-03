"""ABM-decorated Pybricks actuating & sensing functionalities."""


from abm.decor import act, sense

from .hubs import (EV3Brick,   # noqa: F401
                   InventorHub, PrimeHub, CityHub, MoveHub, TechnicHub)
from .ev3dev._speaker import Speaker as EV3Speaker
from .iodevices import (AnalogSensor as IOAnalogSensor,
                        DCMotor as IODCMotor,
                        Ev3devSensor as IOEV3DevSensor,
                        I2CDevice as IOI2CDevice,
                        LUMPDevice as IOLUMPDevice,
                        LWP3Device as IOLWP3Device,
                        PUPDevice as IOPUpDevice,
                        UARTDevice as IOUARTDevice)
from .messaging import (Connection,   # noqa: F401
                        Mailbox, LogicMailbox, NumericMailbox, TextMailbox,
                        BluetoothMailboxServer, BluetoothMailboxClient)
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
for ev3_speaker_act in (
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
    decor(EV3Speaker, ev3_speaker_act, act)


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

# IOAnalogSensor
# (pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.AnalogSensor)
# ------------------------------------------------------------------------
for io_analog_sensor_act in (
    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.AnalogSensor.active
    'active',

    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.AnalogSensor.passive
    'passive',
):
    decor(IOAnalogSensor, io_analog_sensor_act, act)

for io_analog_sensor_sense in (
    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.AnalogSensor.voltage
    'voltage',

    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.AnalogSensor.resistance
    'resistance',
):
    decor(IOAnalogSensor, io_analog_sensor_sense, sense)

# IODCMotor
# (pybricks.com/ev3-micropython/iodevices#dc-motor)
# -------------------------------------------------
for io_dc_motor_act in (
    'dc',
    'stop',
):
    decor(IODCMotor, io_dc_motor_act, act)

# IOEV3DevSensor
# (pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.Ev3devSensor)
# ------------------------------------------------------------------------
for io_ev3dev_sensor_sense in (
    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.Ev3devSensor.read
    'read',
):
    decor(IOEV3DevSensor, io_ev3dev_sensor_sense, sense)

# IOI2CDevice
# (pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.I2CDevice)
# ---------------------------------------------------------------------
for io_i2c_device_act in (
    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.I2CDevice.write
    'write',
):
    decor(IOI2CDevice, io_i2c_device_act, act)

for io_i2c_device_sense in (
    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.I2CDevice.read
    'read',
):
    decor(IOI2CDevice, io_i2c_device_sense, sense)

# IOLUMPDevice
# (pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.LUMPDevice)
# ----------------------------------------------------------------------
for io_lump_device_act in (
    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.LUMPDevice.write
    'write',
):
    decor(IOLUMPDevice, io_lump_device_act, act)

for io_lump_device_sense in (
    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.LUMPDevice.read
    'read',
):
    decor(IOLUMPDevice, io_lump_device_sense, sense)

# IOLWP3Device
# (docs.pybricks.com/en/latest/iodevices/lwp3device.html#pybricks.iodevices.LWP3Device)
# -------------------------------------------------------------------------------------
for io_lwp3_device_act in (
    # docs.pybricks.com/en/latest/iodevices/lwp3device.html#pybricks.iodevices.LWP3Device.name
    'name',

    # docs.pybricks.com/en/latest/iodevices/lwp3device.html#pybricks.iodevices.LWP3Device.write
    'write',
):
    decor(IOLWP3Device, io_lwp3_device_act, act)

for io_lwp3_device_sense in (
    # docs.pybricks.com/en/latest/iodevices/lwp3device.html#pybricks.iodevices.LWP3Device.read
    'read',
):
    decor(IOLWP3Device, io_lwp3_device_sense, sense)

# IOPUpDevice
# (docs.pybricks.com/en/latest/iodevices/pupdevice.html#pybricks.iodevices.PUPDevice)
# -----------------------------------------------------------------------------------
for io_pup_device_act in (
    # docs.pybricks.com/en/latest/iodevices/pupdevice.html#pybricks.iodevices.PUPDevice.write
    'write',
):
    decor(IOPUpDevice, io_pup_device_act, act)

for io_pup_device_sense in (
    # docs.pybricks.com/en/latest/iodevices/pupdevice.html#pybricks.iodevices.PUPDevice.info
    'info',

    # docs.pybricks.com/en/latest/iodevices/pupdevice.html#pybricks.iodevices.PUPDevice.read
    'read',
):
    decor(IOPUpDevice, io_pup_device_sense, sense)

# UARTDevice
# ----------
# TODO


# robotics
# (docs.pybricks.com/en/latest/robotics.html)
# ===========================================

# DriveBase
# (docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase)
# -----------------------------------------------------------------------
for drive_base_act in (
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
    decor(DriveBase, drive_base_act, act)

for drive_base_sense in (
    # docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.distance
    'distance',

    # docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.angle
    'angle',

    # docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.state
    'state',
):
    decor(DriveBase, drive_base_sense, sense)


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
# (docs.pybricks.com/en/latest/tools#pybricks.tools.StopWatch)
# ------------------------------------------------------------
for stop_watch_act in (
    # docs.pybricks.com/en/latest/tools#pybricks.tools.StopWatch.pause
    'pause',

    # docs.pybricks.com/en/latest/tools#pybricks.tools.StopWatch.resume
    'resume',

    # docs.pybricks.com/en/latest/tools#pybricks.tools.StopWatch.reset
    'reset',
):
    decor(StopWatch, stop_watch_act, act)

for stop_watch_sense in (
    # docs.pybricks.com/en/latest/tools#pybricks.tools.StopWatch.time
    'time',
):
    decor(StopWatch, stop_watch_sense, sense)

# wait
# (docs.pybricks.com/en/latest/tools#pybricks.tools.wait)
# -------------------------------------------------------
tools.wait: callable = act(tools.wait)
