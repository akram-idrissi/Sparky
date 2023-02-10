class Component:
    def __init__(self, actor):
        self.actor = actor
        self.actor.add_component(self)
        
        self.engine = self.actor.get_engine()
        self.window = self.actor.window

    def update(self):
        pass

    def draw(self):
        pass
    