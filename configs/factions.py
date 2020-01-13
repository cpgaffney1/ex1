from src.gameplay.Faction import Faction

earth = Faction(name='United Nations',
                abbreviation='UN',
                adjective='UN',
                ship_prefix='UNN',
                color=(0, 0, 204))

mars = Faction(name='Martian Congressional Republic',
               abbreviation='MCR',
               adjective='Martian',
               ship_prefix='MCRN',
               color=(204, 0, 0))

opa = Faction(name='Outer Planets Alliance',
               abbreviation='OPA',
               adjective='Belter',
               ship_prefix='OPAS',
               color=(0, 153, 76))

nonaligned = Faction(name='Nonaligned',
               abbreviation='',
               adjective='',
               ship_prefix='',
               color=(96, 96, 96))

