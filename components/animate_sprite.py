from .sprite import Sprite

class AnimateSprite(Sprite):
    """
    Sprite subclass responsible for rendering animations.

    Attributes:
        animations: a dict that stores multiple animations.
        current_animation: keeps track of the current animation we're on.
        frames: has frames of a specific animation.
        index: keeps track of which animation should be drawn.
    """
    def __init__(self, actor):
        super().__init__(actor)

        self.animations = {}
        self.current_animation = None
        self.frames = []
        self.index = 0

    def update(self):
        self.frames = self.animations[self.current_animation]
        self.index %= len(self.frames)
        self.image = self.frames[int(self.index)]
        self.index += 0.1

    def add_frames(self, name, frames):
        """ Adds more frames to an animation """
        if(name and len(frames) > 0):
            self.animations[name] += frames
 
    def add_animation(self, name, frames):
        """ Adds a new animation """
        if(name and len(frames) > 0):
            self.animations[name] = frames
            self.current_animation = name

    # getters setters
    def set_animation(self, name):
        """ Updates the current animation """
        if(name): self.current_animation = name 

    def get_animation(self, name):
        """ Returns the current animation """
        if name:
            return self.current_animation
        return None

    def get_frames(self, name):
        """ Gets frames of a specific animation """
        if name and name in self.animations.keys:
            return self.animations[name]
        return None

    def set_frames(self, name, frames):
        """ Sets frames of a specific animation """
        if(name and name in self.animations.keys):
            self.animations[name] = frames
            self.current_animation = name
