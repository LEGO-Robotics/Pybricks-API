"""ABM-decorating pybricks.iodevices.PUPDevice."""


from ...iodevices import PUPDevice
from ..util import act_decor, sense_decor


# PUPDevice
# (docs.pybricks.com/en/latest/iodevices/pupdevice.html#pybricks.iodevices.PUPDevice)
# -----------------------------------------------------------------------------------
for a in (
    # docs.pybricks.com/en/latest/iodevices/pupdevice.html#pybricks.iodevices.PUPDevice.write
    'write',
):
    act_decor(PUPDevice, a)

for s in (
    # docs.pybricks.com/en/latest/iodevices/pupdevice.html#pybricks.iodevices.PUPDevice.info
    'info',

    # docs.pybricks.com/en/latest/iodevices/pupdevice.html#pybricks.iodevices.PUPDevice.read
    'read',
):
    sense_decor(PUPDevice, s)
