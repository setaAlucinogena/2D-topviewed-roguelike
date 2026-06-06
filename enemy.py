import game_manager
from world_element import WorldElement, ElementType
from ursina import *
from projectile import Projectile

class Enemy(WorldElement):
    
    def __init__(self, position):
        super().__init__(
            position = position,
            hittable = True,
            scale = 1,
            element_type = ElementType.MOBILE,
            integrity = 60
            )
        self.speed = 4

        #flags:
        self.stunned = False
        self.able_to_throw = True

        self.de_stun_delay = 2#corregir magic numbers després
        self.throwing_delay = 3

    def stun(self):
        self.stunned = True
        invoke(self.de_stun,delay = self.de_stun_delay)

    def de_stun(self):
        self.stunned = False

    def get_hit(self, damage, push, emitter):
        super().get_hit(damage, push, emitter)
        self.stun()


    def throw_one_projectile(self,target):
        direction = Vec3(target.x-self.x,target.y-self.y,0)
        Projectile(position = self.position,damage = 3,push = 4,direction = direction,speed = 1)

    def throw_projectiles_process(self,target):
        if self.able_to_throw:
            self.able_to_throw = False
            self.throw_one_projectile(target)
            invoke(self.reload_throwing,delay = self.throwing_delay)
        
    def reload_throwing(self):
        self.able_to_throw = True

    def follow(self):
        
        self.look_at_xy(self.game_manager.player)
        if not self.stunned:
            self.position += self.up*self.speed*time.dt
            self.throw_projectiles_process(target = self.game_manager.player)


    def update(self):
        super().update()
        self.follow()