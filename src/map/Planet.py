from src.map.Location import Location
from src.gfx.shapes_util import *
from src.gfx.Card import CardLayout
from pyglet.gl import *
from src.map.astronomical_util import milli_au_to_pixels, planet_radius, PlanetType
from enum import Enum
from src.map.NavigationComputer import RadialPosition, Position

orbit_color = (0, 128, 255)
sun_color = (255, 255, 0)


class Planet(Location):

    def __init__(self,
                 name='Sol',
                 img_name='',
                 img_anchor=(0, 0),
                 # astronomical params
                 radius=None,  # in AU
                 period=None,  # in days
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
                          orbits=orbits
                          )

        self.img_name = img_name
        self.img_anchor = img_anchor

        self.planet_type = planet_type
        self.controller = controller

        self.fleets = []

        self.selected_layout = None

    def bounds_contain(self, x, y):
        x, y = float(x), float(y)
        my_x, my_y = self.px_location()
        d = math.sqrt((my_x - x) ** 2 + (my_y - y) ** 2)
        return d < milli_au_to_pixels(planet_radius(self.planet_type))

    def draw(self):
        # orbit line
        if self.is_sun():
            body_radius_pixels = milli_au_to_pixels(planet_radius(self.planet_type))
            body = make_filled_circle(self.px_location(), body_radius_pixels, sun_color)
        else:
            radius = self.radial_position.r
            orbit_radius_pixels = milli_au_to_pixels(radius)
            orbit = make_circle(self.radial_position.primary_body.px_location(), orbit_radius_pixels, orbit_color,
                                num_points=math.ceil(radius))
            orbit.draw(GL_LINE_LOOP)

            body_radius_pixels = milli_au_to_pixels(planet_radius(self.planet_type))
            body = make_filled_circle(self.px_location(), body_radius_pixels, self.controller.color)

    def is_sun(self):
        return self.planet_type == PlanetType.STAR

    def draw_zoomed(self):
        if not self.img_name:
            return False
        img = pyglet.image.load('data/{}'.format(self.img_name))
        img.blit(*self.img_anchor)
        return True

    def draw_selected(self, screen_width, screen_height):
        self.selected_layout = CardLayout(screen_width, screen_height)
        self.selected_layout.add_card(self.name, self.controller.abbreviation, '')
        for fleet in self.fleets:
            self.selected_layout.add_card(fleet.name, 'Fleet INFO', '', fleet.select)
        self.selected_layout.draw()

    def can_zoom(self):
        return self.img_name != ''

    def add_anchored_fleet(self, fleet):
        self.fleets += [fleet]

    def remove_anchored_fleet(self, fleet):
        self.fleets.remove(fleet)

    def __str__(self):
        return 'Planet({})'.format(self.name)


