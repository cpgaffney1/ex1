from src.map.Location import Location
from src.gfx.shapes_util import *
from pyglet.gl import *
from src.map.astronomical_util import radial_location_px_to_cartesian_px, milli_au_to_pixels, radial_location_to_cartesian
from enum import Enum
from src.gameplay.EventManager import event_manager, Frequency
from src.map.NavigationComputer import RadialPosition, Position
import random

orbit_color = (0, 128, 255)
sun_color = (255, 255, 0)


class PlanetType(Enum):
    STAR = 1
    PLANET = 2
    GAS_GIANT = 3
    DWARF_PLANET = 4
    MOON = 5
    ASTEROID = 6
    COMET = 7


# RADIUS IN MILLI AU
planet_type_to_radius = {
    PlanetType.STAR: 200,
    PlanetType.PLANET: 50,
    PlanetType.GAS_GIANT: 100,
    PlanetType.DWARF_PLANET: 25,
    PlanetType.MOON: 25,
    PlanetType.ASTEROID: 10,
    PlanetType.COMET: 10,
}


class Planet(Location):

    def __init__(self,
                 name='Sol',
                 img_name='',
                 img_anchor=(0, 0),
                 # astronomical params
                 radius=None,  # in AU
                 period=None,  # in days
                 draw_location=(0, 0),  # x, y only for the sun
                 primary_body=None,  # planet object, None should be the sun
                 radial_degrees=None,  # degrees, not applicable to sun.
                 planet_type=None,  # PlanetType enum
                 # details
                 controller=None,  # faction object. None means not controllable
                 ):
        assert planet_type is not None
        self.planet_type = planet_type

        if primary_body is None:
            assert name == 'Sol'
            assert self.is_sun()
        if not self.is_sun():
            assert radius is not None
            assert period is not None
            assert primary_body is not None
            assert radial_degrees is not None
        radial_pos = None
        cartesian_pos = None
        if self.is_sun():
            cartesian_pos = Position(x=0, y=0)
            orbits = False
        else:
            radius = 1000. * radius  # NOTE: SELF.RADIUS IS INPUT AS AU, BUT STORED AS MILLI AU
            radial_velocity = 360. / period  # 360 degrees per year
            radial_pos = RadialPosition(primary_body=primary_body, r=radius, theta=radial_degrees, omega=radial_velocity)
            orbits = True
        Location.__init__(self,
                          name=name,
                          radial_position=radial_pos,
                          cartesian_position=cartesian_pos,
                          orbits=orbits,
                          draw_location=draw_location)

        self.img_name = img_name
        self.img_anchor = img_anchor

        self.planet_type = planet_type

        self.controller = controller

        self.draw_location = self.px_location()

    # def anchor_points(self):
    #     body_radius = planet_type_to_radius[self.planet_type]
    #     angular_velocity = 360. / self.period  # 360 degrees / period days
    #     l1 = RadialPosition(self.primary_body.radial_position(), self.radius + body_radius, self.radial_degrees,
    #                         angular_velocity)
    #     l2 = RadialPosition(self.primary_body.radial_position(), self.radius - body_radius, self.radial_degrees,
    #                         angular_velocity)
    #     return [l1, l2]
    # def low_orbit(self, degrees=None):
    #     if degrees is None:
    #         degrees = random.randint(0, 360)
    #     body_radius = planet_type_to_radius[self.planet_type]
    #     period = 10  # days (unrealistic)
    #     angular_velocity = 360. / period  # 360 degrees / period days
    #     return RadialPosition((x, y), body_radius, degrees, angular_velocity)

    def bounds_contain(self, x, y):
        x, y = float(x), float(y)
        my_x, my_y = self.draw_location
        d = math.sqrt((my_x - x) ** 2 + (my_y - y) ** 2)
        return d < milli_au_to_pixels(planet_type_to_radius[self.planet_type])

    def draw(self):
        # orbit line
        print(self.planet_type)
        if self.is_sun():
            body_radius_pixels = milli_au_to_pixels(planet_type_to_radius[self.planet_type])
            body = make_filled_circle(self.px_location(), body_radius_pixels, sun_color)
        else:
            radius = self.radial_position.r
            orbit_radius_pixels = milli_au_to_pixels(radius)
            orbit = make_circle(self.radial_position.primary_body.px_location(), orbit_radius_pixels, orbit_color, num_points=math.ceil(radius))
            orbit.draw(GL_LINE_LOOP)

            body_radius_pixels = milli_au_to_pixels(planet_type_to_radius[self.planet_type])
            body = make_filled_circle(self.px_location(), body_radius_pixels, self.controller.color)

    def is_sun(self):
        return self.planet_type == PlanetType.STAR

    # def draw_zoomed(self):
    #     if not self.img_name:
    #         return False
    #     img = pyglet.image.load('data/{}'.format(self.img_name))
    #     img.blit(*self.img_anchor)
    #     return True
    #
    # def can_zoom(self):
    #     return self.img_name != ''


