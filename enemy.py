import game_manager
from world_element import WorldElement, ElementType
from ursina import *
from projectile import Projectile

class Enemy(WorldElement):
    
    def __init__(self, position,integrity,hit_cooldown,hit_damage,hit_range,hit_push,speed,attack_distance,dialogable = False,dialogue_scene = None,stunneable = False):
        super().__init__(
            position = position,
            hittable = True,
            scale = .75,
            element_type = ElementType.MOBILE,
            integrity = integrity,
            dialogable = dialogable,
            dialogue_scene = dialogue_scene
            )

        self.speed = speed
        self.attack_distance = attack_distance

        #flags:
        self.stunned = False
        self.stunneable = stunneable
        self.able_to_throw = True

        self.de_stun_delay = 2#corregir magic numbers després
        self.throwing_delay = 1

        self.projectiles = []

        self.hit_cooldown = hit_cooldown
        self.hit_damage = hit_damage
        self.able_to_hit = True
        self.hit_range = hit_range

        self.hit_push = hit_push


    def stun(self):
        self.stunned = True
        invoke(self.de_stun,delay = self.de_stun_delay)

    def de_stun(self):
        self.stunned = False

    def get_hit(self, damage, push, emitter):
        super().get_hit(damage, push, emitter)
        if self.stunneable:
            self.stun()

    

    def throw_one_projectile(self,target):
        direction = Vec3(target.x-self.x,target.y-self.y,0).normalized()

        self.projectiles.append(Projectile(position = self.position,damage = 3,push = 4,direction = direction,speed = 20,dont_hurt = [self]))
        #self.projectiles.append(Projectile(position = self.position,damage = 3,push = 4,direction = direction,speed = 16,dont_hurt = [self]))
        #self.projectiles.append(Projectile(position = self.position,damage = 3,push = 4,direction = direction,speed = 12,dont_hurt = [self]))
        #self.projectiles[-2].x-=1.5
        #self.projectiles[-1].x-=3

    def throw_projectiles_process(self,target):
        if self.able_to_throw:
            self.able_to_throw = False
            self.throw_one_projectile(target)
            invoke(self.reload_throwing,delay = self.throwing_delay)
        
    def reload_throwing(self):
        self.able_to_throw = True


    def orientate(self):
        self.look_at_xy(self.game_manager.player)

    def follow(self):
        if not self.stunned:
            self.position += self.up*self.speed*time.dt
            
    def reload_hit(self):
        self.able_to_hit = True

    def hit(self):
        self.able_to_hit = False
        invoke(self.reload_hit,delay = self.hit_cooldown)
        
        hit_ray = boxcast(self.position,direction = self.forward,thickness = (self.hit_range,self.hit_range),distance = self.hit_range,ignore = [self],debug = True)
        if hit_ray.hit:
            for entity in hit_ray.entities:
                if entity.hittable == True:
                    entity.get_hit(self.hit_damage,self.hit_push,self)

    

    def update(self):
        super().update()
        #self.follow()
        #if not self.stunned:
        #    self.throw_projectiles_process(target = self.game_manager.player)