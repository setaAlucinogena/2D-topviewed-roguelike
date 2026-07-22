from ursina import *

from world_element import WorldElement


class SubRoom(Entity):
    game_controller = None
    def __init__(self,position,scale,local_id):
        super().__init__(
            model = "quad",
            scale = scale,
            color = color.cyan, 
            position = position
            
            )

        #self.objects = []

        self.colliders = []
        
        self.loaded = False
        self.freezed = True
        self.local_id = local_id

        #goto treu-ho
        self.spawn_walls_colliders()
    def spawn_walls_colliders(self):
        #en el futur podran ser colliders fets de mesh, perque els terres no seran full cuadrats
        upper = WorldElement(position = self.position,scale = (self.scale[0],0,2))
        lower = WorldElement(position = self.position,scale = (self.scale[0],0,2))
        upper.y+=self.scale[1] / 2
        lower.y-=self.scale[1] / 2
        upper.collider.visible = True
        lower.collider.visible = True
        self.colliders.append(upper)
        self.colliders.append(lower)



    #def get_possible_next_rooms(self,all_rooms):
        



        

        
        
    
    
        