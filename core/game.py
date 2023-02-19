from .engine import Engine
from .window import Window
from actors.map import Map
from audio.music import Music
from actors.actor import Actor
from actors.player import Player
from components.sprite import Sprite 
from components.layer import Layer, AnimatedLayer, SingleImgLayer

# initializing objects
window = Window()
engine = Engine(window)
music = Music()
music.load('assets/audio/music.wav')
music.play(-1)

# setting the window
window.set_icon('assets/icon.png')
window.set_caption('Game Engine using pygame')

# background
actor = Actor(engine)
background = Sprite(actor)
background.load_img('assets/background.png')
background.scale(1280, 704)

# animated tiles data
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

frames2 = {
    2: 
    [
        'assets/palm_bg/bg_palm_1.png',
        'assets/palm_bg/bg_palm_2.png',
        'assets/palm_bg/bg_palm_3.png',
        'assets/palm_bg/bg_palm_4.png'
    ],
}

frames3 = {
    0: 
    [
        'assets/palm_large/large_1.png',
        'assets/palm_large/large_2.png',
        'assets/palm_large/large_3.png',
        'assets/palm_large/large_4.png'
    ],
    1: 
    [
        'assets/palm_small/small_1.png',
        'assets/palm_small/small_2.png',
        'assets/palm_small/small_3.png',
        'assets/palm_small/small_4.png'
    ],
}

# creating map and layers
map = Map(engine)
bg_palms_layer = AnimatedLayer(map, 'assets/layers/bg_palms.csv', frames2, 64)
coins_layer = AnimatedLayer(map, 'assets/layers/coins.csv', frames, 64)
crates_layer = SingleImgLayer(map, 'assets/layers/crates.csv', 'assets/crate.png', 64)
terrain_layer = Layer(map, 'assets/layers/terrain.csv', 'assets/terrain.png', 64)

coins_layer.offset = (-coins_layer.rect.w // 2, 0)
bg_palms_layer.offset = (0, bg_palms_layer.rect.h // 2)
crates_layer.offset = (0, -crates_layer.rect.h // 2)

map.add_layer('terrain', terrain_layer)
map.add_layer('palms_bg', bg_palms_layer)
map.add_layer('coins', coins_layer)
map.add_layer('crates', crates_layer)

# creating the player
player = Player(engine)
player.position.xy = 600, 520
