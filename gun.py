from multiprocessing import parent_process
from projectile import Projectile
from ursina import *
from math import atan2

class Gun(Entity):
    def __init__(self,
                 carrier,
                 period,
                 reload_time,
                 bullet_damage,
                 bullet_speed,
                 bullet_push,
                 capacity,
                 empty_sound_name,
                 shooting_sound_name,
                 reloading_sound_name,
                 n_bullets = 10
                 
                 ):
        super().__init__(position = carrier.position,
                         model = "quad",
                         scale = .3)
        #
        self.color = color.orange
        #
        
        self.carrier = carrier
        
        self.period = period
        self.reload_time = reload_time
        self.bullet_damage = bullet_damage
        self.bullet_push = bullet_push
        self.bullet_speed = bullet_speed

        self.pivot = Entity(position = self.carrier.position)
        self.parent = self.pivot

        self.able_to_shoot = True
        self.reloading = False

        self.n_bullets = n_bullets

        self.bullets_in_chamber = 0
        self.capacity = capacity
        
        self.empty_sound_name = empty_sound_name
        self.shooting_sound_name = shooting_sound_name
        self.reloading_sound_name = reloading_sound_name


    def reload(self):
        if not self.reloading:
            self.reloading=True
            invoke(self.effective_reload,delay = self.reload_time)

    def effective_reload(self):
        

        if self.bullets_in_chamber < self.capacity and self.n_bullets > 0:
            Audio(self.reloading_sound_name,autoplay = True, loop = False,pitch = 3.5)
            self.n_bullets -= 1
            self.bullets_in_chamber += 1
        self.reloading = False
            

    def reload_shooting(self):
        self.able_to_shoot = True

    def use(self):
        if self.able_to_shoot and not self.reloading:
            if self.bullets_in_chamber>0:

                self.able_to_shoot = False
                self.bullets_in_chamber-=1
                invoke(self.reload_shooting,delay = self.period)

                Audio(self.shooting_sound_name,autoplay = True, loop = False)
                Projectile(position = self.world_position,damage = self.bullet_damage,push = self.bullet_push,direction = self.position.normalized(),speed = self.bullet_speed,dont_hurt = [self,self.carrier])
            else:
                Audio(self.empty_sound_name,autoplay = True,loop = False)

    def update_flying(self):
        self.pivot.x = self.carrier.x
        self.pivot.y = self.carrier.y

        #

        self.position = (mouse.position - self.carrier.screen_position).normalized()*1.2
        
        



        