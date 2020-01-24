from enum import Enum
import os
from configs.factions import mars, earth
import random


class ShipType(Enum):
    BATTLESHIP = 1
    CRUISER = 2
    DESTROYER = 3
    CORVETTE = 4
    CARGO = 5


class Ship(object):

    flight_plan = None  # FlightPlan object

    def __init__(self,
                 name='',
                 ship_type=None,  # ShipType
                 faction=None
                 ):
        self.ship_type = ship_type
        self.faction = faction
        self.name = name
        if not self.name:
            self.assign_random_name()

    def assign_random_name(self):
        data_folder = 'data'
        faction_folder = ''
        if self.faction == mars:
            faction_folder = 'mcrn'
        elif self.faction == earth:
            faction_folder = 'unn'
        fname = ''
        if self.ship_type == ShipType.BATTLESHIP:
            fname = 'battleship.txt'
        elif self.ship_type == ShipType.CRUISER:
            fname = 'cruiser.txt'
        elif self.ship_type == ShipType.DESTROYER:
            fname = 'destroyer.txt'
        elif self.ship_type == ShipType.CORVETTE:
            fname = 'corvette.txt'
        path = os.path.join(data_folder, faction_folder, fname)
        with open(path) as f:
            names = f.readlines()
        names = [x.strip() for x in names]

        while True:
            name = random.choice(names)
            if name not in self.faction.used_ship_names:
                self.name = name
                break





