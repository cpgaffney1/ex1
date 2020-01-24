import configs.planets
import configs.fleets


def set_sun_draw_location(screen_size):
    ### THIS MUST HAPPEN FIRST
    width, height = screen_size
    configs.planets.sun.draw_location = (width / 2, height / 2)


def get_planets():
    planets = [
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

    for planet in planets:
        planet.draw_location = planet.px_location()

    return planets


def get_fleets():
    fleets = [
        configs.fleets.e_home,
    ]

    # should not need to draw fleets immediately

    return fleets
