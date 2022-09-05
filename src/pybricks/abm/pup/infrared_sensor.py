"""ABM-decorating pybricks.pupdevices.InfraredSensor."""


from ...pupdevices import InfraredSensor
from ..util import sense_decor


# InfraredSensor
# (docs.pybricks.com/en/latest/pupdevices/infraredsensor.html#pybricks.pupdevices.InfraredSensor)
# -----------------------------------------------------------------------------------------------
for s in (
    # docs.pybricks.com/en/latest/pupdevices/infraredsensor.html#pybricks.pupdevices.InfraredSensor.distance
    'distance',

    # docs.pybricks.com/en/latest/pupdevices/infraredsensor.html#pybricks.pupdevices.InfraredSensor.reflection
    'reflection',

    # docs.pybricks.com/en/latest/pupdevices/infraredsensor.html#pybricks.pupdevices.InfraredSensor.count
    'count',
):
    sense_decor(InfraredSensor, s)
