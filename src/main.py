import pyglet
from gfx import Application
from src.gameplay.EventManager import event_manager
from src.gameplay.GameClock import GAME_SPEED, GameSpeed

app = Application.Application()

update_freq = 0.25
if GAME_SPEED == GameSpeed.SLOW:
    update_freq = 0.4
elif GAME_SPEED == GameSpeed.MEDIUM:
    update_freq = 0.2
elif GAME_SPEED == GameSpeed.FAST:
    update_freq = 0.01

pyglet.clock.schedule_interval(event_manager.run_events, 0.25)
app.run()
