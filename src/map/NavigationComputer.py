from enum import Enum
from src.gameplay.GameClock import GameTime


class InterceptType(Enum):
    DOCKING = 1
    HIGH_G_INTERCEPT = 2


class Position(object):

    def __init__(self, x=0, y=0, vx=0, vy=0, ax=0, ay=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay


class RadialPosition(object):

    def __init__(self,
                 primary_body=None,
                 r=0,
                 theta=0,
                 omega=0
                 ):
        self.primary_body = primary_body
        self.r = r  # mAU
        self.theta = theta  # degrees
        self.omega = omega  # degrees / day


class FlightPlan(object):
    # Define flight path between two points. ax and ay form acceleration vector.
    # At GameTime tm, will negate ax and ay for de-acceleration.
    # tm = None denotes that no flip occurs
    def __init__(self,
                 start,  # Position obj
                 end,  # Position obj
                 ax,
                 ay,
                 tm,  # GameTime object
                 ):
        self.start = start
        self.end = end
        self.ax = ax
        self.ay = ay
        self.tm = tm

class NavigationComputer(object):

    # navigation computer accepts inputs in terms of mAU, degrees, and hours, but internally works with km

    def __init__(self):
        pass

    def navigate(self, start, end, intercept_type=InterceptType.DOCKING):
        # start and end position objects. InterceptType enum
        pass

    # def navigate_constant_velocity(self, start, end, vel=0, angular_vel=0):
    #     # vel in units of mAU / hour, angular_vel in units of degrees per hour
    #     assert vel != 0 or angular_vel != 0
    #     if vel != 0:
    #         return NotImplementedError
    #     if angular_vel != 0:
    #         fp = FlightPlan(start, end, )



nav_computer = NavigationComputer()