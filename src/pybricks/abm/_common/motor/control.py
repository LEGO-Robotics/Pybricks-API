"""ABM-decorating pybricks._common.Control."""


from ...._common import Control
from ...util import act_decor, sense_decor


# Control
# -------
for a in (
    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.Motor.control.limits
    'limits',   # *** NOTE: OVERLOADED METHOD ***

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.Motor.control.pid
    'pid',   # *** NOTE: OVERLOADED METHOD ***

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.Motor.control.target_tolerances
    'target_tolerances',   # *** NOTE: OVERLOADED METHOD ***

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.Motor.control.stall_tolerances
    'stall_tolerances',   # *** NOTE: OVERLOADED METHOD ***
):
    act_decor(Control, a)

for s in (
    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.Motor.control.stalled
    'stalled',

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.Motor.control.done
    'done',

    # docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.Motor.control.load
    'load',
):
    sense_decor(Control, s)
