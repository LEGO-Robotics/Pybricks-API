"""ABM-decorating utilities."""


from collections.abc import Sequence

from abm.decor import act, sense


__all__: Sequence[str] = 'act_decor', 'sense_decor'


def _decor(cls: type, method_name: str, decorator: callable, /):
    """Decorate class method."""
    setattr(cls, method_name, decorator(getattr(cls, method_name)))


def act_decor(cls: type, method_name: str, /):
    """Decorate class method with `act`."""
    _decor(cls, method_name, act)


def sense_decor(cls: type, method_name: str, /):
    """Decorate class method with `sense`."""
    _decor(cls, method_name, sense)
