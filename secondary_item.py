
from ursina import Entity,mouse


class SecondaryItem(Entity):
    def __init__(self,name,carrier):
        super().__init__(position = carrier.position,
                         model = "quad",
                         scale = .3)

        self.name = name
        self.carrier = carrier
        self.pivot = Entity(position = self.carrier.position)
        self.parent = self.pivot

    def update_flying(self):
        self.pivot.x = self.carrier.x
        self.pivot.y = self.carrier.y

        self.position = (mouse.position - self.carrier.screen_position).normalized()*1.2