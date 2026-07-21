from ursina import *
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
        if len(self.units) > 0:
            self.units = []

        if updated_max != None:
            self.max = updated_max


        cum_x = 0
        for i in range(self.max):
            print("IT")
            if i < active:
                current_unit = Entity(parent = self,color = color.red,model = "quad",scale = 1,texture = self.active_unit)

            else:
                current_unit = Entity(parent = self,color = color.black,model = "quad",scale = 1,texture = self.inactive_unit)

            current_unit.x = cum_x
            cum_x += current_unit.scale[0] + .15
            #current_unit.alpha = 100
            self.units.append(current_unit)

                
