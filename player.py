from ursina import *
from custom_keys import CustomKeys
import game_manager
from world_element import ElementType, WorldElement

from time import perf_counter


class Player(WorldElement):
    game_manager = None
    def __init__(self,position):
        super().__init__(
            position = position,
            scale = 1,
            hittable = True,
            integrity = 20 #treure
            )
        self.speed = 3
        self.max_integrity = 32


        
        #camera
        self.camera_pivot = Entity(position = self.position)
        self.camera_pivot.z-=5
        camera.parent = self.camera_pivot
        #end camera

        #sword
        self.sword = WorldElement(position = self.position,scale = (1.5,.12),element_type=ElementType.IGNORE)
        self.sword_rotation_pivot = Entity(position = self.position)
        self.sword.parent = self.sword_rotation_pivot
        self.sword.x += 1.4
        self.sword_rotation_increment = 300

        self.parrying = False
        self.parrying_time = 1.12
        

        #end sword


    def update_camera_pivot(self):
        sp = world_position_to_screen_position(self.position)
        if abs(sp.x) > 0.65:
            self.camera_pivot.x += (sp.x / abs(sp.x)) * self.speed*time.dt


        if abs(sp.y) > 0.3:
            self.camera_pivot.y += (sp.y / abs(sp.y)) * self.speed*time.dt


    def update_sword(self):
        self.sword_rotation_pivot.x = self.x
        self.sword_rotation_pivot.y = self.y
        self.sword_rotation_pivot.rotation_z += self.sword_rotation_increment*time.dt
        
        #sword_cast = raycast(origin = self.position, direction = self.sword_angle,distance = 1,debug = True)

        sword_victims = self.sword.intersects(ignore = [self])
        if sword_victims.hit:
            for entity in sword_victims.entities:
                if entity.parryable == True:
                    if self.parrying:
                        if entity.last_parried_by != self:
                            entity.get_parried(self)

                if entity.hittable == True:
                    entity.get_hit(damage = .1,push = 100, emitter = self)


    def parry(self):
        self.parrying = True
        invoke(self.stop_parrying,delay = self.parrying_time)

        self.sword_rotation_increment = -self.sword_rotation_increment
        self.sword_rotation_pivot.rotation_z += 2*self.sword_rotation_increment*time.dt
        #i si poso que a cada parry exitos vagi algo mes rapid ??? 

    def stop_parrying(self):
        self.parrying = False

    def input(self,key):
        if key == CustomKeys.PARRY:
            self.parry()

    def update(self):
        self.update_camera_pivot()
        self.update_sword()

        self.position += (Vec3(0,1,0)*held_keys[CustomKeys.UP] + Vec3(0,-1,0)*held_keys[CustomKeys.DOWN] + Vec3(-1,0,0)*held_keys[CustomKeys.LEFT] + Vec3(1,0,0)*held_keys[CustomKeys.RIGHT])*time.dt*self.speed