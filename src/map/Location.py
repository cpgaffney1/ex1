class Location(object):

    # graphics
    img_path = ''

    # details
    sectors = []
    pops = []

    def __init__(self):
        pass

    def get_xy_location(self):
        return NotImplementedError

    def bounds_contain(self, x, y):
        return NotImplementedError
