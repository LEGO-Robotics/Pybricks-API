"""ABM-decorating EV3 Speaker."""


from ...ev3dev._speaker import Speaker
from ..util import act_decor


# Speaker
# -------
for a in (
    # pybricks.com/ev3-micropython/hubs#pybricks.hubs.EV3Brick.speaker.beep
    'beep',

    # pybricks.com/ev3-micropython/hubs#pybricks.hubs.EV3Brick.speaker.play_notes
    'play_notes',

    # pybricks.com/ev3-micropython/hubs#pybricks.hubs.EV3Brick.speaker.play_file
    'play_file',

    # pybricks.com/ev3-micropython/hubs#pybricks.hubs.EV3Brick.speaker.say
    'say',

    # pybricks.com/ev3-micropython/hubs#pybricks.hubs.EV3Brick.speaker.set_speech_options
    'set_speech_options',

    # pybricks.com/ev3-micropython/hubs#pybricks.hubs.EV3Brick.speaker.set_volume
    'set_volume',
):
    act_decor(Speaker, a)
