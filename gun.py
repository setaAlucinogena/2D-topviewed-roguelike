from multiprocessing import parent_process
from projectile import Projectile
from ursina import *
from math import atan2
from secondary_item import SecondaryItem


from nail import Nail

#que gun sigui herencia de la classe "flying item" 
#de aquesta classe fare lupa (per veure i detectar coses), mirall (per deflectir rajos laser), imant (per atreure metall)

class Gun(SecondaryItem):
    def __init__(self,
                 name,
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
                 n_bullets = 10,
                 projectile = None
                 ):

        super().__init__(
            name,
            carrier = carrier)
        
        self.color = color.orange
        #
        
        
        self.period = period
        self.reload_time = reload_time
        self.bullet_damage = bullet_damage
        self.bullet_push = bullet_push
        self.bullet_speed = bullet_speed

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

                if self.name == "nail gun":
                    Nail(position = self.world_position, direction = self.position.normalized(),dont_hurt=[self.carrier])
                else:
                    Projectile(position = self.world_position,damage = self.bullet_damage,push = self.bullet_push,direction = self.position.normalized(),speed = self.bullet_speed,dont_hurt = [self,self.carrier])
                
            else:
                Audio(self.empty_sound_name,autoplay = True,loop = False)        
        



        