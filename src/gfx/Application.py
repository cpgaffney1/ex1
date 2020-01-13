import pyglet
import configs.planets
from pyglet.gl import *
import time
from enum import Enum

# Zooming constants
ZOOM_IN_FACTOR = 1.2
ZOOM_OUT_FACTOR = 1/ZOOM_IN_FACTOR


class ScreenMode(Enum):
    MENU = 1
    MAP = 2
    CLOSEUP = 3


class Application(pyglet.window.Window):

    fullscreen = False
    resizable = False
    size = (1280, 720)
    planets = []
    click_time = 0
    click_count = 0
    zoomed_planet = None
    screen_mode = ScreenMode.MAP

    def __init__(self):
        if self.fullscreen:
            self.resizable = False
        super(Application, self).__init__(
            fullscreen=self.fullscreen,
            resizable=self.resizable,
        )
        width, height = self.size
        if self.fullscreen:
            width, height = self.get_size()
        else:
            self.set_size(width, height)

        # Initialize camera values
        self.left = 0
        self.right = width
        self.bottom = 0
        self.top = height
        self.zoom_level = 1
        self.zoomed_width = width
        self.zoomed_height = height

        configs.planets.sun.location = (self.get_size()[0] / 2, self.get_size()[1] / 2)

        self.planets = [
            configs.planets.sun,
            configs.planets.earth,
            configs.planets.mars,
            configs.planets.mercury,
            configs.planets.venus,
            configs.planets.jupiter,
            configs.planets.saturn,
            configs.planets.uranus,
            configs.planets.neptune,
            configs.planets.pluto,
            # asteroids
            configs.planets.ceres,
            configs.planets.vesta,
            configs.planets.pallas,
            configs.planets.hygiea,
            configs.planets.juno,
            configs.planets.psyche,
            configs.planets.eros,
            configs.planets.chiron,
            # moons
            configs.planets.luna,
            configs.planets.io,
            configs.planets.europa,
            configs.planets.ganymede,
            configs.planets.callisto,
            configs.planets.tethys,
            configs.planets.rhea,
            configs.planets.titan,
            configs.planets.iapetus,
            configs.planets.triton,

        ]

        for planet in self.planets:
            planet.location = planet.get_xy_location()

    def draw_planets(self):
        for planet in self.planets:
            planet.draw()

    def init_gl(self, width, height):
        # Set clear color
        glClearColor(0 / 255, 0 / 255, 0 / 255, 0 / 255)

        # Set antialiasing
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_POLYGON_SMOOTH)
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)

        # Set alpha blending
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Set viewport
        glViewport(0, 0, width, height)

    def on_resize(self, width, height):
        if self.screen_mode != ScreenMode.MAP:
            return
        if self.fullscreen:
            return
        # Set window values
        self.width = width
        self.height = height
        # Initialize OpenGL context
        self.init_gl(width, height)

    def on_mouse_press(self, x, y, button, modifiers):
        t = time.time()
        if t - self.click_time < 0.25:
            self.click_count += 1
        else:
            self.click_count = 1
            self.click_time = time.time()

        # DOUBLE CLICK
        if self.click_count >= 2:
            for planet in self.planets:
                if planet.bounds_contain(x, y) and planet.can_zoom():
                    self.zoomed_planet = planet
                    self.screen_mode = ScreenMode.CLOSEUP
                    return

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        # Move camera
        if self.screen_mode != ScreenMode.MAP:
            return
        self.left -= dx * self.zoom_level
        self.right -= dx * self.zoom_level
        self.bottom -= dy * self.zoom_level
        self.top -= dy * self.zoom_level

        for planet in self.planets:
            planet.move(-dx, -dy, self.zoom_level)

    def on_mouse_scroll(self, x, y, dx, dy):
        if self.screen_mode != ScreenMode.MAP:
            return
        # Get scale factor
        f = ZOOM_IN_FACTOR if dy > 0 else ZOOM_OUT_FACTOR if dy < 0 else 1
        # If zoom_level is in the proper range
        if .2 < self.zoom_level * f < 5:
            self.zoom_level *= f

            mouse_x = x / self.width
            mouse_y = y / self.height

            mouse_x_in_world = self.left + mouse_x * self.zoomed_width
            mouse_y_in_world = self.bottom + mouse_y * self.zoomed_height

            self.zoomed_width *= f
            self.zoomed_height *= f

            self.left = mouse_x_in_world - mouse_x * self.zoomed_width
            self.right = mouse_x_in_world + (1 - mouse_x) * self.zoomed_width
            self.bottom = mouse_y_in_world - mouse_y * self.zoomed_height
            self.top = mouse_y_in_world + (1 - mouse_y) * self.zoomed_height

    def on_draw(self):

        # Initialize Projection matrix
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # Initialize Modelview matrix
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # Save the default modelview matrix
        glPushMatrix()
        # Clear window with ClearColor
        glClear(GL_COLOR_BUFFER_BIT)

        width, height = self.size
        glOrtho(0, width, 0, height, 1, -1)

        if self.screen_mode == ScreenMode.CLOSEUP:
            self.zoomed_planet.draw_zoomed()
        else:
            self.draw_planets()

        # Remove default modelview matrix
        glPopMatrix()

    def run(self):
        pyglet.app.run()