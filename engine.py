import pygame


class Engine:
    def __init__(self, window):
        self.running = True
        self.window = window
        
        self.sprites = []
        self.actors = set()

    def process_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
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

    def add_actor(self, actor):
        self.actors.add(actor)

    def remove_actor(self, actor):
        self.actors.remove(actor) if len(self.actors) > 0  else ''

    def add_sprite(self, sprite):
        self.sprites.append(sprite)

    # setters getters
    def is_running(self):
        return self.running

    def set_running(self, value):
        self.running = value
