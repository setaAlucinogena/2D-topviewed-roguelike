from world_element import WorldElement, ElementType
from ursina import invoke,time,Entity

class Sword(WorldElement):
    def __init__(self,
                 scale,
                 parrying_time,
                 parry_cooldown,
                 rotation_increment,
                 parry_level,
                 carrier
                 ):
        super().__init__(position = carrier.position, 
                         scale = scale,
                         element_type = ElementType.IGNORE)

        self.pivot = Entity()
        self.parrying_time = parrying_time
        self.parry_cooldown = parry_cooldown
        self.rotation_increment = rotation_increment
        self.parry_level = parry_level
        
        self.carrier = carrier 

        self.parrying = False
        self.able_to_parry_again= True

        self.pivot.position = self.carrier.position
        self.parent = self.pivot
        self.x+=1.4


    def parry(self):
        if self.able_to_parry_again:
            self.able_to_parry_again = False
            self.parrying = True
            invoke(self.reload_parry,delay = self.parry_cooldown)
            invoke(self.stop_parrying,delay = self.parrying_time)

            self.rotation_increment = -self.rotation_increment
            self.pivot.rotation_z += 2*self.rotation_increment*time.dt

    def reload_parry(self):
        self.able_to_parry_again = True

    def stop_parrying(self):
        self.parrying = False

    def update_sword(self):
        self.pivot.x = self.carrier.x
        self.pivot.y = self.carrier.y
        self.pivot.rotation_z += self.rotation_increment*time.dt
        
        victims = self.intersects(ignore = [self])
        if victims.hit:
            for entity in victims.entities:
                if entity.parryable == True:
                    if self.parrying:
                        if entity.last_parried_by != self:
                            entity.get_parried(self,parry_level = 1)

                if entity.hittable == True:
                    entity.get_hit(damage = .1,push = 100, emitter = self)