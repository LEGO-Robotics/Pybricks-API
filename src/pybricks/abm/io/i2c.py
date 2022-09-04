"""ABM-decorating pybricks.iodevices.I2CDevice."""


from ...iodevices import I2CDevice
from ..util import act_decor, sense_decor


# I2CDevice
# (pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.I2CDevice)
# ---------------------------------------------------------------------
for a in (
    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.I2CDevice.write
    'write',
):
    act_decor(I2CDevice, a)

for s in (
    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.I2CDevice.read
    'read',
):
    sense_decor(I2CDevice, s)
