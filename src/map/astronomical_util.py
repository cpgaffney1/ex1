import numpy as np

AU_PIXEL_FACTOR = 300.


def radial_location_to_xy(primary_location, radius, degrees):
    x, y = primary_location
    radius_pixels = au_to_pixels(radius)
    radians = degrees * np.pi / 180.
    xp = np.cos(radians) * radius_pixels
    yp = np.sin(radians) * radius_pixels
    return x + xp, y + yp


def au_to_pixels(au):
    return au * AU_PIXEL_FACTOR
