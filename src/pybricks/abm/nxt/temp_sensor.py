"""ABM-decorating pybricks.nxtdevices.TemperatureSensor."""


from ...nxtdevices import TemperatureSensor
from ..util import sense_decor


# LightSensor
# (pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.TemperatureSensor)
# -------------------------------------------------------------------------
for s in (
    # pybricks.com/ev3-micropython/nxtdevices#pybricks.nxtdevices.TemperatureSensor.temperature
    'temperature',
):
    sense_decor(TemperatureSensor, s)
