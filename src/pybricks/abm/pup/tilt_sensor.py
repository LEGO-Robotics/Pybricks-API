"""ABM-decorating pybricks.pupdevices.TiltSensor."""


from ...pupdevices import TiltSensor
from ..util import sense_decor


# TiltSensor
# (docs.pybricks.com/en/latest/pupdevices/tiltsensor.html#pybricks.pupdevices.TiltSensor)
# ---------------------------------------------------------------------------------------
for s in (
    # docs.pybricks.com/en/latest/pupdevices/tiltsensor.html#pybricks.pupdevices.TiltSensor.tilt
    'tilt',
):
    sense_decor(TiltSensor, s)
