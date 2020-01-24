import numpy as np
from src.map.NavigationComputer import Position
from enum import Enum

AU_PIXEL_FACTOR = 300.
MILLI_AU_PIXEL_FACTOR = AU_PIXEL_FACTOR / 1000.
AU_TO_KM = 1.496e+8


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


def planet_radius(planet_type):
    return planet_type_to_radius[planet_type]


def radial_location_px_to_cartesian_px(primary_location, radius, degrees):
    # primary location x,y in milli au, radius in milli au
    # RETURNS location in pixels
    xp, yp = primary_location
    xp_mau, yp_mau = pixels_to_milli_au(xp), pixels_to_milli_au(yp)
    x, y = radial_location_to_cartesian((xp_mau, yp_mau), radius, degrees)
    return milli_au_to_pixels(x), milli_au_to_pixels(y)


def pixels_to_milli_au(px):
    return px / MILLI_AU_PIXEL_FACTOR


def milli_au_to_pixels(mau):
    return mau * MILLI_AU_PIXEL_FACTOR


def milli_au_to_km(mau):
    return mau * AU_TO_KM / 1000.


def km_to_milli_au(km):
    return km * 1000. / AU_TO_KM


def radial_location_to_cartesian(primary_loc, radius, degrees):
    # inputs all in mAU and degrees
    # convert to radians
    x, y = primary_loc
    rad = degrees * np.pi / 180.
    xp = radius * np.cos(rad)
    yp = radius * np.sin(rad)
    return x + xp, y + yp


def radial_velocity_to_cartesian(radius, degrees, degrees_omega):
    # inputs all in mAU and degrees
    # convert to radians
    omega = degrees_omega * np.pi / 180.
    rad = degrees * np.pi / 180.
    vx = radius * -np.sin(rad) * omega
    vy = radius * np.cos(rad) * omega
    return vx, vy


def radial_acceleration_to_cartesian(radius, degrees, degrees_omega):
    # inputs all in mAU and degrees
    # convert to radians
    omega = degrees_omega * np.pi / 180.
    rad = degrees * np.pi / 180.
    ax = radius * -np.cos(rad) * omega**2
    ay = radius * -np.sin(rad) * omega**2
    return ax, ay


def radial_position_to_cartesian(radial_position):
    x, y = radial_location_to_cartesian(
        radial_position.primary_loc, radial_position.radius, radial_position.degrees)
    vx, vy = radial_velocity_to_cartesian(radial_position.radius, radial_position.degrees, radial_position.omega)
    ax, ay = radial_acceleration_to_cartesian(radial_position.radius, radial_position.degrees, radial_position.omega)
    return Position(x, y, vx, vy, ax, ay)
