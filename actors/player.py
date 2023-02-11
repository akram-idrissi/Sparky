from .actor import Actor
from components.input import Input
from components.animSprite import AnimSprite


class Player(Actor):
    def __init__(self, game):
        super().__init__(game)

        self.input = None
        self.animation = None
        self.load()

    def load(self):
        self.input = Input(self)
        self.animation = AnimSprite(self)
        self.animation.add_animation("run", [
            self.animation.load_img('assets/dino/run1.png'),
            self.animation.load_img('assets/dino/run2.png'),
        ])

    def update_actor(self):
        pass