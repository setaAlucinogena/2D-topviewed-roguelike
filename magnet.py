from secondary_item import SecondaryItem
from ursina import color,Vec3,time,boxcast,distance,Audio

from world_element import ElementType, WorldElement

class Magnet(SecondaryItem):
    def __init__(self,name,carrier):
        super().__init__(name = name, carrier = carrier)
        self.attractive = False
        self.color = color.gray

        self.magnetic_objects = []
        self.strength = 13

    def get_magnetic_objects(self):
        #tmp = WorldElement(position = self.position,model = "cube",scale = (10,10,2),element_type=ElementType.IGNORE)
        #tmp.visible = False

        #hit_info = tmp.intersects(ignore = [self])

        self.magnetic_objects = []

        hit_info = boxcast(origin = Vec3(self.world_position[0],self.world_position[1],self.world_position[2]), thickness = 15,distance = 15,ignore = [self])
        if hit_info.hit:
            for entity in hit_info.entities:
                if entity.magnetic:
                    print("Almenys tenim 1")
                    self.magnetic_objects.append(entity)

    def use(self):
        Audio("lighter.mp3",autoplay = True,loop = False)
        self.attractive = (not self.attractive)
        if not self.attractive:
            if len(self.magnetic_objects)>0:
                for obj in self.magnetic_objects:
                    obj.stop_being_dragged()
        else:
            Audio("electricity_discharge.mp3",autoplay = True,loop = False)

        #que la atractio vingui desde el imant. haura de obtenir una llista de tots els objectes magnètics. pero només un cop per ús.

    #def stop_using(self):
    #    self.magnetic_objects = []

    def update(self):
        
        self.get_magnetic_objects()

        for obj in self.magnetic_objects:
            d = distance(self,obj)
            if self.attractive == True:
                
                if d > 1:
                    obj.get_attracted_by_magnet(strength = self.strength, emitter = self,ignore_list = [self.carrier])
                else:
                    
                    obj.stop_being_dragged()
            #else:
            #    tmp = Vec3(obj.x-self.world_position[0], obj.y-self.world_position[1],0)
            #
            #    obj.position += tmp.normalized() * self.strength * time.dt