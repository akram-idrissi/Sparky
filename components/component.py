class Component:
    def __init__(self, actor):
        """
        Simple base class for components definition
        
        The base class for game components. Derived classes will want to
        override the Component.update() and Component.draw(). 
        The initializer can accept an Actor().

        When subclassing the Component class, be sure to call the base initializer.

        Attributes:
            actor: a reference to the owner of this component.
            engine: a reference to the engine object.
            window: a reference to the window object.
        """
        self.actor = actor
        self.actor.add_component(self)
        
        self.engine = self.actor.get_engine()
        self.window = self.actor.window

    def update(self):
        pass

    def draw(self):
        pass
    