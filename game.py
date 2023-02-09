from actor import Actor
from engine import Engine
from window import Window


window = Window()
window.set_icon('icon.png')
window.set_caption('Game Engine using pygame')

engine = Engine(window)
actor = Actor(engine)
