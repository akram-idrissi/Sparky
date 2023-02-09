class Component:
    def __init__(self, actor):
        self.actor = actor
        self.actor.add_component(self)

    def update(self):
        pass

    def draw(self):
        pass
    