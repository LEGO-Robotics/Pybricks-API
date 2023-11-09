"""ABM-decorating pybricks.pupdevices.ColorLightMatrix."""


from ...pupdevices import ColorLightMatrix
from ..util import act_decor


# ColorLightMatrix
# (docs.pybricks.com/en/latest/pupdevices/colorlightmatrix.html#pybricks.pupdevices.ColorLightMatrix)
# ---------------------------------------------------------------------------------------------------
for a in (
    # docs.pybricks.com/en/latest/pupdevices/colorlightmatrix.html#pybricks.pupdevices.ColorLightMatrix.on
    'on',

    # docs.pybricks.com/en/latest/pupdevices/colorlightmatrix.html#pybricks.pupdevices.ColorLightMatrix.off
    'off',
):
    act_decor(ColorLightMatrix, a)
