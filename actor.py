class Actor:
    
    def __init__(self, game):
        self.game = game
        self.game.add_actor(self)

        self.components = set()

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
    
    def process_input(self):
        pass
