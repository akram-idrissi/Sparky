from .actor import Actor
from components.input import Input
from components.sprite import Sprite
from core.collision import * 

class Player(Actor):
    def __init__(self, game):
        super().__init__(game)

        self.speed = 4
        self.input = None
        self.sprite = None

        self.load()

    def load(self):
        self.input = Input(self)
        self.sprite = Sprite(self)
        self.sprite.load_img('assets/idle/1.png')

    def process_input(self, events):
        self.velocity.xy = 0, 0
        if self.input.keyheld('left'):
            self.velocity.x -= self.speed
        if self.input.keyheld('right'):
            self.velocity.x += self.speed
        if self.input.keyheld('up'):
            self.velocity.y -= self.speed
        if self.input.keyheld('down'):
            self.velocity.y += self.speed

    def collision(self):
        rect = self.sprite.rect
        tiles = self.engine.layers['terrain'].rects

        self.position.x += self.velocity.x
        rect.x = self.position.x
        collisions = collidedtiles(rect, tiles) 
        pos, _ = vertical_movement(rect, self.velocity, collisions)
        self.position.x = pos.x

        self.position.y += self.velocity.y
        rect.y = self.position.y
        collisions = collidedtiles(rect, tiles) 
        pos, _ = horizontal_movement(rect, self.velocity, collisions)
        self.position.y = pos.y

    def update_actor(self): 
        self.collision()