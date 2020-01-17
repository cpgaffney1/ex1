from enum import Enum
import time


class GameTime(object):

    _hours = 0.  # time in hours

    def __init__(self,
                 seconds=0.,
                 hours=0.,
                 days=0.,
                 months=0.
                 ):
        self._hours = seconds / 3600. + hours + 24*days + 30*24*months

    def seconds(self):
        return self._hours / 3600.

    def hours(self):
        return self._hours

    def days(self):
        return self.hours() / 24

    def months(self):
        return self.days() / 30

    def __sub__(self, other):
        return GameTime(hours=self.hours() - other.hours())

    def __add__(self, other):
        return GameTime(hours=self.hours() + other.hours())

    def __lt__(self, other):
        return self.hours() < other.hours()

    def __gt__(self, other):
        return self.hours() > other.hours()

    def __le__(self, other):
        return self.hours() <= other.hours()

    def __ge__(self, other):
        return self.hours() >= other.hours()

    def __str__(self):
        return '{}'.format(self._hours)


class GameSpeed(Enum):
    SLOW = 1  # real second == game hour
    MEDIUM = 2  # real second == game day
    FAST = 3  # real second == game 7 days


GAME_SPEED = GameSpeed.FAST

# converts real seconds to game seconds
_game_speed_mapping = {
    GameSpeed.SLOW: 60 * 60,
    GameSpeed.MEDIUM: 60 * 60 * 24,
    GameSpeed.FAST: 60 * 60 * 24 * 7,
}

# Keeps track of game time in seconds. Game time may run faster or slower than real time
class GameClock(object):

    _realtime_previous_advance = time.time()
    _realtime_pause_start = _realtime_previous_advance
    _time = GameTime()
    _paused = True

    def __init__(self, speed):
        self._speed = speed

    def pause(self):
        print('Pausing')
        self._realtime_pause_start = time.time()
        self._paused = True

    def unpause(self):
        print('Un-pausing')
        self._paused = False

    def switch_paused(self):
        if self.paused():
            self.unpause()
        else:
            self.pause()

    def paused(self):
        return self._paused

    def set_game_speed(self, speed):
        # GameSpeed enum
        self._speed = speed

    def advance(self, seconds=0, hours=0):
        if self.paused():
            return False
        self._time += GameTime(seconds=seconds, hours=hours)
        return True

    def time(self):
        cur_time = time.time()
        if self._realtime_pause_start is not None:
            paused_time = cur_time - self._realtime_pause_start
            if not self.paused():
                self._realtime_pause_start = None
        else:
            paused_time = 0
        delta_seconds = cur_time - self._realtime_previous_advance - paused_time
        self._time += GameTime(seconds=delta_seconds * _game_speed_mapping[self._speed])
        self._realtime_previous_advance = cur_time
        return self._time


game_clock = GameClock(GAME_SPEED)
