from world_element import WorldElement, ElementType

class Explosion(WorldElement):
    def __init__(self,
                 position,
                 potency,
                 dont_hurt = []):
        super().__init__(position = position,
                         model = "circle",
                         scale = potency,
                         element_type= ElementType.IGNORE
                         )
        
        hit_info = self.intersects(ignore = dont_hurt,debug = True)
        for entity in hit_info.entities:
            if entity.hittable == True:
                entity.get_hit(damage = potency * 4, push = potency * 100, emitter = self)
                dont_hurt.append(entity)        