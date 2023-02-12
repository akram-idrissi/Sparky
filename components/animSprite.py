from .sprite import Sprite

class AnimSprite(Sprite):
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
        if not self.current_animation: return 
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


class SingleImgAnimation(Sprite):
    def __init__(self, actor, columns, rows=1):
        super().__init__(actor)

        self.index = 0
        self.frame = {}
        self.frames = []
        self.rows = rows
        self.columns = columns

    def load_frames(self):
        frame_height = self.rect.h // self.rows
        frame_width = self.rect.w // self.columns

        for row in range(self.rows):
            for column in range(self.columns):
                self.frames.append([frame_width * column, frame_height * row, frame_width, frame_height])

    def update(self):
        length = len(self.frames)
        self.index = self.index % length
        self.frame = self.frames[int(self.index)]
        self.index += 0.1
        
    def draw(self):
        if not self.image or not self.frame: return 
        self.screen.blit(self.image, self.actor.get_position(), (self.frame[0], self.frame[1], self.frame[2], self.frame[3]))
