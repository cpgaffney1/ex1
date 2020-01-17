from src.gameplay.Ship import Ship


class Fleet(object):

    def __init__(self,
                 name='',
                 home_base=None,  # planet object
                 ships=None,  # list of ship objects
                 ):
        self.name = name
        self.home_base = home_base
        self.ships = ships

    def add_ship(self, ship):
        self.ships += [ship]