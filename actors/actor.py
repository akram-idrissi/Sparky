import pygame

class Actor:
    """
    This is a base Actor class with a handful of overridable methods, each actor also has
    a set of components.

    Derived classes will want to override the Actor.update_actor() 
    and Actor.process_input(). The initializer can accept an Actor().
    When subclassing the Actor class, be sure to call the base initializer.

    Attributes:
        components: a set that contains unique components objects.
        engine: a reference to the engine object.
        window: a reference to the window object.
        position: a vector that define the x and y coordinates of the actor.
        velocity: a vector that updates the position each frame.
        acceleration: a vector that updates the velocity each frame.
    """
    def __init__(self, engine):
        self.components = set()
        self.engine = engine
        self.engine.add_actor(self)
        self.acceleration = pygame.math.Vector2()
        self.position = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.window = self.engine.window

    def add_component(self, component):
        self.components.add(component)

    def remove_component(self, component):
        self.components.add(component) if len(self.components) > 0 else ''

    def update(self):
        """ Updates actor's components and the actor itself """
        for component in self.components:
            component.update()
        self.update_actor()

    def update_actor(self):
        """ An overridable method for updating actor behavior """
        self.velocity += self.acceleration
        self.position += self.velocity
    
    def process_input(self, events):
        """ 
        An overridable method that handles actor input
        Arguments:
            events: list of events triggered.
        """
        pass
