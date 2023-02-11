from .engine import Engine
from .window import Window
from actors.player import Player


window = Window()
window.set_icon('assets/icon.png')
window.set_caption('Game Engine using pygame')

engine = Engine(window)
player = Player(engine)
player.set_position(100, 100)
