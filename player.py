from ursina import *
from custom_keys import CustomKeys
import game_manager
from world_element import ElementType, WorldElement

from time import perf_counter

from projectile import Projectile

from swords_enum import Swords
from guns_enum import Guns

class Player(WorldElement):
    game_manager = None
    def __init__(self,position):
        super().__init__(
            position = position,
            scale = .75,
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
        self.sword = Swords.DEFAULT_SWORD.value
        self.sword.carrier = self

        #end sword


        #self.flying_item = Entity(model = "quad", scale = .3,parent = self.flying_item_pivot)
        
        self.flying_item = Guns.REVOLVER.value
        self.flying_item.carrier = self

        self.flying_item.x += 1.2

        #
        self.color = color.blue


    def update_camera_pivot(self):
        sp = world_position_to_screen_position(self.position)
        if abs(sp.x) > 0.65:
            self.camera_pivot.x += (sp.x / abs(sp.x)) * self.speed*time.dt


        if abs(sp.y) > 0.3:
            self.camera_pivot.y += (sp.y / abs(sp.y)) * self.speed*time.dt


    def parry(self):
        self.sword.parry()

    def input(self,key):
        if key == CustomKeys.PARRY:
            self.parry()
        if key == CustomKeys.USE_FLYING_ITEM:
            self.flying_item.use()

        if key == CustomKeys.RELOAD:
            self.flying_item.reload()

    ####deixo aquesta funcio aqui provisionalment. mes endavant creare la classe pistola
        
        


    def update(self):
        self.update_camera_pivot()
        self.sword.update_sword()
        self.flying_item.update_flying()

        self.position += (Vec3(0,1,0)*held_keys[CustomKeys.UP] + Vec3(0,-1,0)*held_keys[CustomKeys.DOWN] + Vec3(-1,0,0)*held_keys[CustomKeys.LEFT] + Vec3(1,0,0)*held_keys[CustomKeys.RIGHT])*time.dt*self.speed