from src.gameplay.GameClock import game_clock
from src.gameplay.GameClock import GameTime
from enum import Enum

class Frequency(Enum):
    HOURLY = 1
    DAILY = 2
    MONTHLY = 3


class EventManager(object):

    hourly_fns = []
    daily_fns = []
    monthly_fns = []

    def __init__(self):
        cur_time = game_clock.time()
        self.last_hourly_update = cur_time
        self.last_daily_update = cur_time
        self.last_monthly_update = cur_time

    def register_periodic_event(self, frequency, function):  # Frequency enum, callback function
        if frequency == Frequency.HOURLY:
            self.hourly_fns += [function]
        elif frequency == Frequency.DAILY:
            self.daily_fns += [function]
        elif frequency == Frequency.MONTHLY:
            self.monthly_fns += [function]

    def deregister_event(self, function):
        if function in self.hourly_fns:
            self.hourly_fns.remove(function)
        if function in self.daily_fns:
            self.daily_fns.remove(function)
        if function in self.monthly_fns:
            self.monthly_fns.remove(function)

    def run_events(self, dt):  # dt is real delta time. Not used
        if game_clock.paused():
            return
        cur_time = game_clock.time()
        if cur_time - self.last_hourly_update > GameTime(hours=1):
            for fn in self.hourly_fns:
                fn(cur_time - self.last_hourly_update)
            self.last_hourly_update = cur_time
        if cur_time - self.last_daily_update > GameTime(days=1):
            for fn in self.daily_fns:
                fn(cur_time - self.last_daily_update)
            self.last_daily_update = cur_time
        if cur_time - self.last_monthly_update > GameTime(months=1):
            for fn in self.monthly_fns:
                fn(cur_time - self.last_monthly_update)
            self.last_monthly_update = cur_time


event_manager = EventManager()
