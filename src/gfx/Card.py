from src.gfx.shapes_util import make_filled_rectangle
from pyglet.text import Label


class CardLayout(object):

    def __init__(self,
                 screen_width,
                 screen_height,
                 horizontal=True
                ):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.horizontal = horizontal
        self.cards = []

    def add_card(self, title, info, img_path, selected_cb=None):
        card_width = self.screen_width / 12.
        card_height = self.screen_height / 7.
        c = Card(title, info, img_path=img_path, selected_cb=selected_cb, width=card_width, height=card_height)
        self.cards += [c]

    def draw(self):
        card_spacing = 0.01 * self.screen_height
        if self.horizontal:
            x = card_spacing
            y = card_spacing
            for card in self.cards:
                card.origin = (x, y)
                card.draw()
                x += card.width + card_spacing
        else:
            # TODO
            pass


class Card(object):

    def __init__(self,
                 title,
                 info,
                 img_path='',
                 width=None,
                 height=None,
                 origin=None,  # x, y
                 color=(128, 128, 128),
                 selected_cb=None,
                 ):
        self.origin = origin
        self.width = width
        self.height = height
        self.color = color
        self.title = title
        self.info = info
        self.img_path = img_path
        self.selected_cb = selected_cb

    def draw(self):
        make_filled_rectangle(self.origin, self.width, self.height, self.color)
        title = Label(self.title, font_name='Verdana',
                      x=self.origin[0] + self.width * 0.02,
                      y=self.origin[1] + self.height - self.height * 0.02,
                      width=self.width * 0.9, height=self.height * 0.2,
                      anchor_x='left', anchor_y='top')
        title.draw()
        info = Label(self.info, font_name='Verdana',
                      x=self.origin[0] + self.width * 0.02,
                      y=self.origin[1] + self.height - 2 * self.height * 0.02 - self.height * 0.2,
                      width=self.width * 0.9, height=self.height * 0.15,
                      anchor_x='left', anchor_y='top')
        info.draw()

    def bounds_contain(self, x, y):
        x0, y0 = self.origin
        return x0 < x < x0 + self.width and y0 < y < y0 + self.height

    def selected(self):
        print('here')
        if self.selected_cb is not None:
            self.selected_cb()