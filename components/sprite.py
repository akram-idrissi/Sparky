import pygame
from .component import Component

class Sprite(Component):
    """
    Simple base class for visible game objects.

    This class is responsible for rendering and updating all 
    engine graphics. It renders a single sprite per instance, 
    for an animated image check AnimSprite()

    Derived classes can override the Sprite.update() and Sprite.draw() 
    and assign Sprite.image and Sprite.rect attributes. 

    When subclassing the Sprite class, be sure to call the base initializer.

    Attributes:
        image: surface to render
        rect: an image rectangle 
        flip_flag: a flag that allows or prevent img flipping
        flip_axis = keeps track on which axis we should flip img  
        engine: a reference to the engine object.
        screen: a reference to the display surface.
    """
    def __init__(self, actor):
        super().__init__(actor)

        self.rect = None
        self.image = None
        self.offset = (0, 0)
        self.flip_flag = False
        self.flip_axis = (0, 0)
        self.engine.add_sprite(self)
        self.screen = self.window.screen

    def load_img(self, img):
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft=self.actor.position)
        return self.image

    def scale(self, x, y):
        self.image = pygame.transform.scale(self.image, (x, y))
    
    def flip(self, x=None, y=None):
        if not x and not y: 
            self.image = pygame.transform.flip(self.image, self.flip_axis[0], self.flip_axis[1])

    def update(self):
        if not self.rect: return
        self.rect.topleft = self.actor.position

    def draw(self):
        if not self.image: return
        self.screen.blit(self.image, (self.actor.position))
