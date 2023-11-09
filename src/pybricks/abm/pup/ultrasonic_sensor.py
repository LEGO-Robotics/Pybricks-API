"""ABM-decorating pybricks.pupdevices.UltrasonicSensor."""


from ...pupdevices import UltrasonicSensor
from ..util import sense_decor


# UltrasonicSensor
# (docs.pybricks.com/en/latest/pupdevices/ultrasonicsensor.html#pybricks.pupdevices.UltrasonicSensor)
# ---------------------------------------------------------------------------------------------------
for s in (
    # docs.pybricks.com/en/latest/pupdevices/ultrasonicsensor.html#pybricks.pupdevices.UltrasonicSensor.distance
    'distance',

    # docs.pybricks.com/en/latest/pupdevices/ultrasonicsensor.html#pybricks.pupdevices.UltrasonicSensor.presence
    'presence',
):
    sense_decor(UltrasonicSensor, s)
