from src.map.NavigationComputer import RadialPosition
from src.map.astronomical_util import radial_location_px_to_cartesian_px
from src.gameplay.EventManager import event_manager, Frequency

class Location(object):

    # details
    name = ''
    sectors = []
    pops = []

    # location
    draw_location = (0, 0)

    def __init__(self,
                 name='',
                 radial_position=None,
                 cartesian_position=None,
                 orbits=True,
                 draw_location=None,
                 ):
        self.name = name
        assert radial_position is not cartesian_position  # not both None
        self.radial_position = radial_position
        self.cartesian_position = cartesian_position
        self.orbits = orbits
        self.draw_location = draw_location

        if self.orbits:
            event_manager.register_periodic_event(Frequency.HOURLY, self.move_in_orbit)

    def bounds_contain(self, x, y):
        return NotImplementedError

    def px_location(self):
        if self.cartesian_position is not None:
            return self.draw_location
        if self.radial_position is not None:
            loc = radial_location_px_to_cartesian_px(self.radial_position.primary_body.px_location(),
                                                     self.radial_position.r, self.radial_position.theta)
            return loc

    def translate_px(self, dx, dy, zoom_level):
        px, py = self.draw_location
        self.draw_location = (px - dx * zoom_level, py - dy * zoom_level)

    def move_in_orbit(self, delta_time):
        # Only used if the location is in orbit
        if not self.orbits or self.radial_position is None:
            return RuntimeError
        angular_velocity = self.radial_position.omega
        delta_theta = angular_velocity * delta_time.days()
        self.radial_position.theta += delta_theta
        self.draw_location = radial_location_px_to_cartesian_px(self.radial_position.primary_body.px_location(),
                                                                self.radial_position.r, self.radial_position.theta)

    def enter_orbit(self, radial_position):
        if self.orbits:
            return RuntimeError
        self.orbits = True
        self.radial_position = radial_position
        event_manager.register_periodic_event(Frequency.HOURLY, self.move_in_orbit)

    def leave_orbit(self, cartesian_position):
        if not self.orbits:
            return RuntimeError
        self.radial_position = None
        event_manager.deregister_event(self.move_in_orbit)
        self.cartesian_position = cartesian_position
        self.orbits = False

    def draw(self):
        return NotImplementedError

