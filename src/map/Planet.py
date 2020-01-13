from src.map.Location import Location
from src.gfx.shapes_util import *
from pyglet.gl import *
from src.map.astronomical_util import radial_location_to_xy, au_to_pixels
from enum import Enum

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


planet_type_to_radius = {
    PlanetType.STAR: 0.2,
    PlanetType.PLANET: 0.05,
    PlanetType.GAS_GIANT: 0.1,
    PlanetType.DWARF_PLANET: 0.025,
    PlanetType.MOON: 0.025,
    PlanetType.ASTEROID: 0.01,
    PlanetType.COMET: 0.01,
}


class Planet(Location):

    def __init__(self,
                 name='Sol',
                 img_name='',
                 img_anchor=(0, 0),
                 # astronomical params
                 radius=0,  # in AU
                 period=0,  # in days
                 location=(0, 0),  # x, y only for the sun
                 primary_body=None,  # planet object, None should be the sun
                 radial_degrees=0,  # degrees, not applicable to sun.
                 planet_type=None,  # PlanetType enum
                 # details
                 controller=None,  # faction object. None means not controllable
                 ):
        Location.__init__(self)

        self.name = name
        self.img_name = img_name
        self.img_anchor = img_anchor
        self.radius = radius
        self.period = period
        self.location = location
        self.primary_body = primary_body
        self.radial_degrees = radial_degrees
        self.planet_type = planet_type

        self.controller = controller

        self.validate()

        self.location = self.get_xy_location()

    def validate(self):
        if self.primary_body is None:
            assert self.name == 'Sol'
        assert self.planet_type is not None

    def can_zoom(self):
        return self.img_name != ''

    def change_virtual_location(self, dx, dy, zoom_level):
        px, py = self.virtual_location
        self.virtual_location = (px - dx * zoom_level, py - dy * zoom_level)

    def move(self, dx, dy, zoom_level):
        px, py = self.location
        self.location = (px - dx * zoom_level, py - dy * zoom_level)

    def get_xy_location(self):
        if self.primary_body is None:
            return self.location[0], self.location[1]
        else:
            loc = radial_location_to_xy(self.primary_body.get_xy_location(), self.radius, self.radial_degrees)
            return loc

    def bounds_contain(self, x, y):
        x, y = float(x), float(y)
        my_x, my_y = self.location

        d = math.sqrt((my_x - x) ** 2 + (my_y - y) ** 2)
        if self.name == 'Mars':
            print('dist')
            print(d)

            print(au_to_pixels(planet_type_to_radius[self.planet_type]))
            print((x, y))
            print((my_x, my_y))
        return d < au_to_pixels(planet_type_to_radius[self.planet_type])

    def draw(self):
        # orbit line
        if self.primary_body is None:
            body_radius_pixels = au_to_pixels(planet_type_to_radius[self.planet_type])
            body = make_filled_circle(self.get_xy_location(), body_radius_pixels, sun_color)
        else:
            orbit_radius_pixels = au_to_pixels(self.radius)
            orbit = make_circle(self.primary_body.get_xy_location(), orbit_radius_pixels, orbit_color, num_points=math.ceil(self.radius) * 50)
            orbit.draw(GL_LINE_LOOP)

            body_radius_pixels = au_to_pixels(planet_type_to_radius[self.planet_type])
            body = make_filled_circle(self.get_xy_location(), body_radius_pixels, self.controller.color)

    def draw_zoomed(self):
        if not self.img_name:
            return False
        img = pyglet.image.load('data/{}'.format(self.img_name))
        img.blit(*self.img_anchor)
        return True


