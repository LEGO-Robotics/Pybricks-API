"""ABM-decorating pybricks.nxtdevices.SoundSensor."""


from ...nxtdevices import SoundSensor
from ..util import sense_decor


# SoundSensor
# (pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.SoundSensor)
# -------------------------------------------------------------------------
for s in (
    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.SoundSensor.intensity
    'intensity',
):
    sense_decor(SoundSensor, s)
