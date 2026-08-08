from ursina import *
from ursina import destroy
from copy import copy

class CounterBar(Entity):
    def __init__(self,position,scale = .05,max = 1,active_unit = None,inactive_unit = None):
        #self.n_active = n_active
        super().__init__(position = position,
                         scale = scale,
                         parent = camera.ui)
        self.max = max
        self.active_unit = active_unit
        self.inactive_unit = inactive_unit

        self.units = []
            
    def update_bar(self,active,updated_max = None):
        print("UPDATE BAR")
        if len(self.units) > 0:
            for u in self.units:
                destroy(u)
            self.units = []

        if updated_max != None:
            print("updating max")
            self.max = updated_max


        cum_x = 0
        for i in range(self.max):
            if i < active:
                current_unit = Entity(parent = self,color = color.red,model = "quad",scale = 1,texture = self.active_unit)

            else:
                current_unit = Entity(parent = self,color = color.black,model = "quad",scale = 1,texture = self.inactive_unit)

            current_unit.x = cum_x
            cum_x += current_unit.scale[0] + .15
            self.units.append(current_unit)

                
