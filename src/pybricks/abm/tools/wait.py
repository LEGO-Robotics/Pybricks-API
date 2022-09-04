"""ABM-decorating pybricks.tools.wait(...)."""


from abm.decor import act

from ... import tools


# wait
# (docs.pybricks.com/en/latest/tools#pybricks.tools.wait)
# -------------------------------------------------------
tools.wait: callable = act(tools.wait)
