from src.gameplay.Ship import ShipType, Ship
from src.map.Location import Location

class Fleet(Location):

    def __init__(self,
                 name='',
                 home_base=None,  # planet object
                 ship_type_mapping=None,  # mapping from ShipType to number that should be initialized
                 ships=None,  # list of ship objects
                 anchor=None,  # Planet object
                 faction=None,  # Faction object
                 ):
        self.name = name
        self.home_base = home_base
        self.faction = faction
        self.ships = []
        if ships is not None:
            self.ships = ships
        else:
            for ship_type, num in ship_type_mapping.items():
                self.add_ship(Ship(ship_type=ship_type, faction=self.faction))

        self.anchor = None
        assert anchor is not None  # cannot init fleets in interplanetary space
        self.set_anchor(anchor)  # if anchor is None, should be in ip space
        Location.__init__(self,
                          name=name,
                          radial_position=self.anchor.radial_position,
                          orbits=False,
                          )

        self._selected = False

    def add_ship(self, ship):
        self.ships += [ship]

    def set_anchor(self, anchor):
        assert anchor is not None
        self.anchor = anchor
        self.anchor.add_anchored_fleet(self)

    def leave_anchor(self):
        assert self.anchor is not None
        self.anchor.remove_anchored_fleet(self)
        self.anchor = None

    def select(self):
        self._selected = True

    def unselect(self):
        self._selected = False

    def bounds_contain(self, x, y):
        return False

    def draw(self):
        if self.anchor is None:
            # in space, draw triangle
            pass
        else:
            # on a planet, displays card, but defer to planet to do that work
            pass


