from world_element import WorldElement,ElementType
from ursina import time

class Projectile(WorldElement):
    def __init__(self, position,damage,push,direction,speed):
        super().__init__(
            position = position,
            scale = .5
            )

        self.damage = damage
        self.push = push
        self.direction = direction
        self.speed = speed

    def get_parried(self):
        self.direction = -self.direction

    def check_collisions(self):
        
        collisions_info = self.intersects(ignore = [self])
        if collisions_info.hit:
            for entity in collisions_info.entities:
                if entity.element_type != ElementType.IGNORE or entity.element_type != ElementType.TRIGGER:
                    if entity.hittable:
                        entity.get_hit(damage = self.damage, push = self.push, emitter = self)



    def update(self):
        self.check_collisions()
        self.position += self.direction * self.speed * time.dt

