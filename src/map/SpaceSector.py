# SpaceSector will not be configurable at start up


class SpaceSector(object):

    inner_radius = 0
    outer_radius = 0
    degrees = 0

    navies = []

    def __init__(self, inner_radius, outer_radius, degrees):
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.degrees = degrees

    def add_navies(self, navies):
        self.navies += navies
