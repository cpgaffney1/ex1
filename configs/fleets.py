from src.gameplay.Fleet import Fleet
from src.gameplay.Ship import ShipType
import configs.factions as factions
from configs.planets import *

### Earth

e_home = Fleet(name='Home Fleet', home_base=earth, anchor=earth, faction=factions.earth,
               ship_type_mapping={
                   ShipType.BATTLESHIP: 3,
                   ShipType.CRUISER: 6,
                   ShipType.DESTROYER: 8,
                   ShipType.CORVETTE: 15,
               })

e_lunar = Fleet(name='Lunar Fleet', home_base=luna, anchor=luna, faction=factions.earth,
               ship_type_mapping={
                   ShipType.DESTROYER: 8,
                   ShipType.CORVETTE: 15,
               })

e_belt = Fleet(name='Belt Fleet', home_base=ceres, anchor=ceres, faction=factions.earth,
               ship_type_mapping={
                   ShipType.DESTROYER: 8,
                   ShipType.CORVETTE: 15,
               })

### Mars

m_home = Fleet(name='Home Fleet', home_base=mars, anchor=mars, faction=factions.mars,
               ship_type_mapping={
                   ShipType.BATTLESHIP: 3,
                   ShipType.CRUISER: 6,
                   ShipType.DESTROYER: 8,
                   ShipType.CORVETTE: 15,
               })