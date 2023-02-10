from actors.actor import Actor
from components.animate_sprite import AnimateSprite


class Player(Actor):
    def __init__(self, game):
        super().__init__(game)

        self.animation = None
        self.load()

    def load(self):
        self.animation = AnimateSprite(self)
        self.animation.add_animation("run", [
            self.animation.load_img('assets/dino/run1.png'),
            self.animation.load_img('assets/dino/run2.png'),
        ])

    def update_actor(self):
        pass