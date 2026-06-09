from world_element import WorldElement,ElementType
from ursina import time, destroy

class Projectile(WorldElement):
    def __init__(self, position,damage,push,direction,speed,dont_hurt,guided_towards = None):
        super().__init__(
            position = position,
            scale = .5,
            parryable = True
            )

        self.damage = damage
        self.push = push
        self.direction = direction
        self.speed = speed

        self.last_parried_by = None
        self.dont_hurt = dont_hurt
        
        self.guided_towards = guided_towards

    def get_parried(self, emitter, parry_level = 0):
        self.last_parried_by = emitter
        if parry_level == 0:
            self.direction = -self.direction #nivell de parry 0
        elif parry_level == 1:
            self.direction = (self.dont_hurt[0].position - self.position).normalized() #nivell de parry 1
        elif parry_level == 2:
            self.guided_towards = self.dont_hurt[0]
            #nivell de parry 2 ja es el perfect parry, que el projectil seguira com un missil guiat al bitcho que l hagi llençat

        self.dont_hurt = [emitter]


    def check_collisions(self):
        collisions_info = self.intersects(ignore = [self])
        if collisions_info.hit:
            for entity in collisions_info.entities:
                if entity not in self.dont_hurt and (entity.element_type != ElementType.IGNORE and entity.element_type != ElementType.TRIGGER):#per algun motiu no va quan el projectil no fa mal al enemic
                    print(entity.element_type)
                    if entity.hittable:
                        entity.get_hit(damage = self.damage, push = self.push, emitter = self)
                    destroy(self,delay = .3)



    def update(self):
        self.check_collisions()
        if self.guided_towards != None:
            self.direction = (self.guided_towards.position - self.position).normalized()
        self.position += self.direction * self.speed * time.dt

