"""ABM-decorating pybricks.iodevices.LWP3Device."""


from ...iodevices import LWP3Device
from ..util import act_decor, sense_decor


# LWP3Device
# (docs.pybricks.com/en/latest/iodevices/lwp3device.html#pybricks.iodevices.LWP3Device)
# -------------------------------------------------------------------------------------
for a in (
    # docs.pybricks.com/en/latest/iodevices/lwp3device.html#pybricks.iodevices.LWP3Device.name
    # 'name',   # *** NOTE: OVERLOADED METHOD ***

    # docs.pybricks.com/en/latest/iodevices/lwp3device.html#pybricks.iodevices.LWP3Device.write
    'write',
):
    act_decor(LWP3Device, a)

for s in (
    # docs.pybricks.com/en/latest/iodevices/lwp3device.html#pybricks.iodevices.LWP3Device.read
    'read',
):
    sense_decor(LWP3Device, s)
