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