class Faction(object):

    def __init__(self,
                 name='',
                 abbreviation='',
                 adjective='',
                 ship_prefix='',
                 color=(0, 0, 0),  # RGB
                 ):
        self.name = name
        self.abbreviation = abbreviation
        self.adjective = adjective
        self.ship_prefix = ship_prefix
        self.color = color
        self.used_ship_names = []

    def reserve_used_ship_name(self, name):
        self.used_ship_names += name

    def release_used_ship_name(self, name):
        self.used_ship_names.remove(name)

    def __eq__(self, other):
        return self.name == other.name
