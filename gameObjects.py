from game import Game
from actor import Actor
from window import Window


window = Window()
window.set_icon('icon.png')
window.set_caption('Game Engine using pygame')

game = Game(window)
actor = Actor(game)
