from .engine import Engine
from .window import Window
from actors.map import Map
from actors.player import Player
from components.layer import Layer, AnimatedLayer


window = Window()
window.set_icon('assets/icon.png')
window.set_caption('Game Engine using pygame')

engine = Engine(window)
player = Player(engine)
player.set_position(100, 100)

map = Map(engine)
frames = {
    0: 
    [
        'assets/coins/silver/0.png',
        'assets/coins/silver/1.png',
        'assets/coins/silver/2.png',
        'assets/coins/silver/3.png'
    ],

    1: 
    [
        'assets/coins/gold/0.png',
        'assets/coins/gold/1.png',
        'assets/coins/gold/2.png',
        'assets/coins/gold/3.png'
    ]
    }
map.add_layer('coins', AnimatedLayer(map, 'assets/layers/coins.csv', frames, 64))
map.add_layer('terrain', Layer(map, 'assets/layers/terrain.csv', 'assets/terrain.png', 64))
