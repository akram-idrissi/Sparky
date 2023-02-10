import pygame

class Actor:
    
    def __init__(self, engine):
        self.components = set()
        self.engine = engine
        self.engine.add_actor(self)
        self.acceleration = pygame.math.Vector2()
        self.position = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.window = self.engine.get_window()

    def add_component(self, component):
        self.components.add(component)

    def remove_component(self, component):
        self.components.add(component) if len(self.components) > 0 else ''

    def update(self):
        for component in self.components:
            component.update()
        self.update_actor()

    def update_actor(self):
        pass
    
    def process_input(self, events):
        pass

    # getters setters
    def get_engine(self):
        return self.engine

    def get_position(self):
        return self.position
    
    def set_position(self, x, y):
        self.position.x = x; self.position.y = y
    
    def get_velocity(self):
        return self.velocity
    
    def set_velocity(self, x, y):
        self.velocity.x = x; self.velocity.y = y
    
    def get_acceleration(self):
        return self.velocity
    
    def set_acceleration(self, x, y):
        self.acceleration.x = x; self.acceleration.y = y
    