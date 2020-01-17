from src.map.Location import Location
from enum import Enum
from src.map.NavigationComputer import nav_computer, FlightPlan, Position
from src.map.astronomical_util import radial_position_to_cartesian
import random


class ShipType(Enum):
    BATTLESHIP = 1
    CRUISER = 2
    DESTROYER = 3
    CORVETTE = 4
    CARGO = 5


class Ship(Location):

    flight_plan = None  # FlightPlan object

    def __init__(self,
                 name='',
                 ship_type=None,  # ShipType
                 anchor=None,  # Planet object
                 ):
        Location.__init__(self)
        self.name = name
        self.ship_type = ship_type
        self.anchor = anchor
        anchor_pts = self.anchor.anchor_points()
        loc = anchor_pts[0]
        if bool(random.getrandbits(1)):
            loc = anchor_pts[1]

        self.position = radial_position_to_cartesian(loc)

        if not self.name:
            self.assign_random_name()

    def assign_random_name(self):
        pass



