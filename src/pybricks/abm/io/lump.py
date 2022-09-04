"""ABM-decorating pybricks.iodevices.LUMPDevice."""


from ...iodevices import LUMPDevice
from ..util import act_decor, sense_decor


# LUMPDevice
# (pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.LUMPDevice)
# ----------------------------------------------------------------------
for a in (
    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.LUMPDevice.write
    # 'write',   # AttributeError: type object 'LUMPDevice' has no attribute 'write'
):
    act_decor(LUMPDevice, a)

for s in (
    # pybricks.com/ev3-micropython/iodevices#pybricks.iodevices.LUMPDevice.read
    'read',
):
    sense_decor(LUMPDevice, s)
