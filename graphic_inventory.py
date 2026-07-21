from ursina import *

class GraphicInventory(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            position = (0,0,-.1),
            scale = 1
            )

        self.inventory  = []
        self.current_index = 0

        self.left_slot = None
        self.middle_slot = None
        self.right_slot = None


    def increment_index(self,increment):
        
        if (self.current_index + increment) > 0 and (self.current_index + increment) < (len(self.inventory)-1):
            return (self.current_index + increment)
        else:
            return self.current_index


    

    def update_view(self,increment):
        self.current_index = self.increment_index(increment)
        self.update_slots()
        

    def update_slots(self):
        if self.current_index == 0:
            self.left_slot = None
            self.middle_slot = Entity(
                parent = self,
                model = "quad",
                texture = self.inventory[0].texture,
                position = (0,0,0)
                )
            self.right_slot = Entity(
                parent = self,
                model = "quad",
                texture = self.inventory[1].texture,
                position = (.2,0,0)
                )
        elif self.current_index == (len(self.inventory) - 1):
            self.left_slot = Entity(
                parent = self,
                model = "quad",
                texture = self.inventory[self.current_index - 1].texture,
                position = (-.2,0,0)
                )
            self.middle_slot = Entity(
                parent = self,
                model = "quad",
                texture = self.inventory[self.current_index].texture,
                position = (0,0,0)
                )
            self.right_slot = None
        else:
            self.left_slot = Entity(
                parent = self,
                model = "quad",
                texture = self.inventory[self.current_index - 1].texture,
                position = (-.2,0,0)
                )
            self.middle_slot = Entity(
                parent = self,
                model = "quad",
                texture = self.inventory[self.current_index].texture,
                position = (0,0,0)
                )
            self.right_slot = Entity(
                parent = self,
                model = "quad",
                texture = self.inventory[self.current_index + 1].texture,
                position = (.2,0,0)
                )


