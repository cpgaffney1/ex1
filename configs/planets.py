from src.map.Planet import Planet, PlanetType
import configs.factions as factions

sun = Planet(
    name='Sol',
    draw_location=(0, 0),  # set dynamically
    planet_type=PlanetType.STAR,
)

# Inners

earth = Planet(
    name='Earth',
    img_name='earth.jpg',
    img_anchor=(0, 0),
    radius=1,
    period=365,
    primary_body=sun,
    radial_degrees=45,
    planet_type=PlanetType.PLANET,
    controller=factions.earth,
)

luna = Planet(
    name='Luna',
    img_name='luna.png',
    radius=0.1,
    period=60,
    primary_body=earth,
    radial_degrees=90,
    planet_type=PlanetType.MOON,
    controller=factions.earth,
)

mars = Planet(
    name='Mars',
    img_name='mars.jpg',
    radius=1.4,
    period=686,
    primary_body=sun,
    radial_degrees=160,
    planet_type=PlanetType.PLANET,
    controller=factions.mars,
)

# Belt

ceres = Planet(
    name='Ceres',
    img_name='ceres.png',
    radius=1.8,
    period=965,
    primary_body=sun,
    radial_degrees=130,
    planet_type=PlanetType.DWARF_PLANET,
    controller=factions.earth,
)

vesta = Planet(
    name='Vesta',
    img_name='vesta.jpg',
    radius=1.8,
    period=965,
    primary_body=sun,
    radial_degrees=170,
    planet_type=PlanetType.ASTEROID,
    controller=factions.mars,
)

pallas = Planet(
    name='Pallas',
    img_name='pallas.jpg',
    radius=1.8,
    period=965,
    primary_body=sun,
    radial_degrees=195,
    planet_type=PlanetType.ASTEROID,
    controller=factions.mars,
)

hygiea = Planet(
    name='Hygiea',
    img_name='',
    radius=1.8,
    period=965,
    primary_body=sun,
    radial_degrees=220,
    planet_type=PlanetType.ASTEROID,
    controller=factions.earth,
)

juno = Planet(
    name='Juno',
    img_name='juno.jpg',
    radius=1.8,
    period=965,
    primary_body=sun,
    radial_degrees=110,
    planet_type=PlanetType.ASTEROID,
    controller=factions.earth,
)

psyche = Planet(
    name='Psyche',
    img_name='psyche.jpg',
    radius=1.8,
    period=965,
    primary_body=sun,
    radial_degrees=260,
    planet_type=PlanetType.ASTEROID,
    controller=factions.earth,
)

eros = Planet(
    name='Eros',
    img_name='eros.jpg',
    radius=1.8,
    period=965,
    primary_body=sun,
    radial_degrees=20,
    planet_type=PlanetType.ASTEROID,
    controller=factions.earth,
)

chiron = Planet(
    name='Chiron',
    img_name='chiron.jpg',
    radius=1.8,
    period=965,
    primary_body=sun,
    radial_degrees=70,
    planet_type=PlanetType.ASTEROID,
    controller=factions.earth,
)


# nonaligned planets

mercury = Planet(
    name='Mercury',
    radius=0.4,
    period=120,  # this is wrong
    primary_body=sun,
    radial_degrees=230,
    planet_type=PlanetType.DWARF_PLANET,
    controller=factions.nonaligned,
)

venus = Planet(
    name='Venus',
    radius=0.7,
    period=224,
    primary_body=sun,
    radial_degrees=80,
    planet_type=PlanetType.PLANET,
    controller=factions.nonaligned,
)

jupiter = Planet(
    name='Jupiter',
    radius=3.1,
    period=365 * 11,
    primary_body=sun,
    radial_degrees=210,
    planet_type=PlanetType.GAS_GIANT,
    controller=factions.nonaligned,
)

io = Planet(
    name='Io',
    img_name='io.jpg',
    radius=0.15,
    period=60,
    primary_body=jupiter,
    radial_degrees=240,
    planet_type=PlanetType.MOON,
    controller=factions.nonaligned,
)

europa = Planet(
    name='Europa',
    img_name='europa.jpg',
    radius=0.2,
    period=70,
    primary_body=jupiter,
    radial_degrees=300,
    planet_type=PlanetType.MOON,
    controller=factions.nonaligned,
)

ganymede = Planet(
    name='Ganymede',
    img_name='ganymede.jpg',
    radius=0.25,
    period=80,
    primary_body=jupiter,
    radial_degrees=130,
    planet_type=PlanetType.MOON,
    controller=factions.earth,
)

callisto = Planet(
    name='Callisto',
    img_name='',
    radius=0.3,
    period=80,
    primary_body=jupiter,
    radial_degrees=300,
    planet_type=PlanetType.MOON,
    controller=factions.mars,
)

saturn = Planet(
    name='Saturn',
    radius=4.2,
    period=365 * 29,
    primary_body=sun,
    radial_degrees=180,
    planet_type=PlanetType.GAS_GIANT,
    controller=factions.nonaligned,
)

tethys = Planet(
    name='Tethys',
    img_name='',
    radius=0.15,
    period=60,
    primary_body=saturn,
    radial_degrees=60,
    planet_type=PlanetType.MOON,
    controller=factions.nonaligned,
)

rhea = Planet(
    name='Rhea',
    img_name='',
    radius=0.2,
    period=70,
    primary_body=saturn,
    radial_degrees=10,
    planet_type=PlanetType.MOON,
    controller=factions.nonaligned,
)

titan = Planet(
    name='Titan',
    img_name='',
    radius=0.25,
    period=80,
    primary_body=saturn,
    radial_degrees=130,
    planet_type=PlanetType.MOON,
    controller=factions.nonaligned,
)

iapetus = Planet(
    name='Iapetus',
    img_name='',
    radius=0.3,
    period=90,
    primary_body=saturn,
    radial_degrees=280,
    planet_type=PlanetType.MOON,
    controller=factions.nonaligned,
)

uranus = Planet(
    name='Uranus',
    radius=5.6,
    period=365 * 84,
    primary_body=sun,
    radial_degrees=350,
    planet_type=PlanetType.GAS_GIANT,
    controller=factions.nonaligned,
)

neptune = Planet(
    name='Neptune',
    radius=6.7,
    period=365 * 164,
    primary_body=sun,
    radial_degrees=330,
    planet_type=PlanetType.GAS_GIANT,
    controller=factions.nonaligned,
)

triton = Planet(
    name='Triton',
    img_name='',
    radius=0.14,
    period=60,
    primary_body=neptune,
    radial_degrees=50,
    planet_type=PlanetType.MOON,
    controller=factions.nonaligned,
)

pluto = Planet(
    name='Pluto',
    radius=7.9,
    period=365 * 247,
    primary_body=sun,
    radial_degrees=240,
    planet_type=PlanetType.DWARF_PLANET,
    controller=factions.nonaligned,
)