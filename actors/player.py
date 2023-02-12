from .actor import Actor
from components.input import Input
from components.animSprite import SingleImgAnimation


class Player(Actor):
    def __init__(self, game):
        super().__init__(game)

        self.input = None
        self.animation = None
        self.load()

    def load(self):
        self.input = Input(self)
        self.animation = SingleImgAnimation(self, 8)
        self.animation.load_img('assets/attack.png')
        self.animation.load_frames()

    def process_input(self, events):
        pass

    def update_actor(self):
        pass
