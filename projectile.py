from world_element import WorldElement,ElementType
from ursina import time

class Projectile(WorldElement):
    def __init__(self, position,damage,push,direction,speed,ignore):
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
        self.ignore = ignore


    def get_parried(self, emitter):
        self.last_parried_by = emitter
        self.direction = -self.direction


    def check_collisions(self):
        collisions_info = self.intersects(ignore = [self])
        if collisions_info.hit:
            for entity in collisions_info.entities:
                if entity not in self.ignore and entity.element_type != ElementType.IGNORE or entity.element_type != ElementType.TRIGGER:#per algun motiu no va quan el projectil no fa mal al enemic
                    if entity.hittable:
                        entity.get_hit(damage = self.damage, push = self.push, emitter = self)



    def update(self):
        self.check_collisions()
        self.position += self.direction * self.speed * time.dt

