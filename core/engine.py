import pygame


class Engine:
    def __init__(self, window):
        self.running = True
        self.window = window
        
        self.layers = {}
        self.sprites = []
        self.actors = set()
        self.scroll = [0, 0]

    def process_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.window.close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.window.close()
            
        for actor in self.actors:
            actor.process_input(events)

    def update(self):
        for actor in self.actors:
            actor.update()

    def draw(self):
        self.window.fill()
        for sprite in self.sprites:
            sprite.draw()
        self.window.update()

    def add_layer(self, name, layer):
        if name not in self.layers.keys() : self.layers[name] = layer

    def add_actor(self, actor):
        self.actors.add(actor)

    def remove_actor(self, actor):
        self.actors.remove(actor) if len(self.actors) > 0  else ''

    def add_sprite(self, sprite):
        self.sprites.append(sprite)
