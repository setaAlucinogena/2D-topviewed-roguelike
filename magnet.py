from secondary_item import SecondaryItem
from ursina import color,Vec3,time

from world_element import ElementType, WorldElement

class Magnet(SecondaryItem):
    def __init__(self,name,carrier):
        super().__init__(name = name, carrier = carrier)
        self.attractive = True
        self.color = color.gray

        self.magnetic_objects = []
        self.strength = .1

    def get_magnetic_objects(self):
        tmp = WorldElement(position = self.position,model = "cube",scale = (10,10,2),element_type=ElementType.IGNORE)
        tmp.visible = False

        hit_info = tmp.intersects(ignore = [self])
        if hit_info.hit:
            for entity in hit_info.entities:
                if entity.magnetic:
                    print("Almenys tenim 1")
                    self.magnetic_objects.append(entity)

    def use(self):
        self.attractive = (not self.attractive)
        
        #que la atractio vingui desde el imant. haura de obtenir una llista de tots els objectes magnètics. pero només un cop per ús.

    #def stop_using(self):
    #    self.magnetic_objects = []

    def update(self):
        #if len(self.magnetic_objects) == 0:
        self.get_magnetic_objects()#fer aquest worldelement a cada frame esta costant molt espai i molta ram eh

        for obj in self.magnetic_objects:
            if self.attractive == True:
                tmp = Vec3(self.world_position[0]-obj.x, self.world_position[1]-obj.y,0)
            else:
                tmp = Vec3(obj.x-self.world_position[0], self.world_position[1]-self.y,0)

            obj.position += tmp.normalized() * self.strength * time.dt