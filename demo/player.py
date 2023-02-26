from actors.actor import Actor
from components.input import Input
from components.sprite import Sprite
from core.collision import *


class Player(Actor):
    def __init__(self, game):
        super().__init__(game)

        self.speed = 2
        self.input = None
        self.sprite = None
        self.jump = False
        self.momentum = 0
        self.timer = 0
        self.gravity = 0.8
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
        if self.input.keydown(events, 'space'):
            if self.timer < 6:
                self.acceleration.y = -5

    def collision(self):
        rect = self.sprite.rect
        tiles = self.engine.layers['terrain'].rects

        self.position.x += self.velocity.x
        rect.x = self.position.x
        collisions = collidedtiles(rect, tiles)
        pos, _ = horizontal_movement(rect, self.velocity, collisions)
        self.position.x = pos.x

        self.position.y += self.velocity.y
        rect.y = self.position.y
        collisions = collidedtiles(rect, tiles)
        pos, sides = vertical_movement(rect, self.velocity, collisions)
        if sides['bottom']:
            self.acceleration.y = 0
            self.timer = 0
        else:
            self.timer += 1
        self.position.y = pos.y

    def update_actor(self):
        self.engine.scroll[0] += (self.velocity.x - self.engine.scroll[0])
        super().update_actor()
        self.acceleration.y += 0.2
        if self.acceleration.y > 3: self.acceleration.y = 3
        self.collision()
