from .engine import Engine
from .window import Window
from actors.map import Map
from actors.player import Player
from components.layer import Layer


window = Window()
window.set_icon('assets/icon.png')
window.set_caption('Game Engine using pygame')

engine = Engine(window)
player = Player(engine)
player.set_position(100, 100)

map = Map(engine)
map.add_layer('terrain', Layer(map, 'assets/layers/terrain.csv', 'assets/terrain.png', 64))
