"""ABM-decorating pybricks.iodevices.UARTDevice."""


from ...iodevices import UARTDevice
from ..util import act_decor, sense_decor


# UARTDevice
# (pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.UARTDevice)
# ----------------------------------------------------------------------
for a in (
    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.UARTDevice.write
    'write',

    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.UARTDevice.clear
    'clear',
):
    act_decor(UARTDevice, a)

for s in (
    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.UARTDevice.read
    'read',

    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.UARTDevice.read_all
    'read_all',

    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.UARTDevice.waiting
    'waiting',
):
    sense_decor(UARTDevice, s)
