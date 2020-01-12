from src.map.Location import Location
from src.util.Configuration import Configuration


class Planet(Location, Configuration):

    # location params
    radius = 0
    period = 0

    def __init__(self):
        Location.__init__(self)
        Configuration.__init__(self)