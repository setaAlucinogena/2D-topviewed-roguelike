from tkinter import CURRENT
from xml.dom.minidom import Element
from matplotlib.image import NEAREST
from ursina import *
from custom_keys import CustomKeys
from game_manager import GameManager,GameState
from world_element import ElementType, WorldElement

from time import perf_counter

from projectile import Projectile

from swords_enum import Swords
#from guns_manager import Guns

from counter_bar import CounterBar

#borrar despres:
from magnet import Magnet

class Player(WorldElement):
    game_manager = None
    def __init__(self,position,integrity, max_integrity):
        super().__init__(
            position = position,
            scale = .75,
            hittable = True,
            integrity = integrity, #treure
            element_type=ElementType.MOBILE
            )
        self.speed = 12#4#3
        self.movement_vector = Vec3(0,0,0)
        #self.current_speed = self.speed

        self.max_integrity = max_integrity


        
        #camera
        self.camera_pivot = Entity(position = self.position)
        self.camera_pivot.z-=5
        camera.parent = self.camera_pivot
        #end camera

        #sword
        self.sword = Swords.DEFAULT_SWORD.value
        self.sword.carrier = self

        #end sword


        #self.secondary_item = Entity(model = "quad", scale = .3,parent = self.secondary_item_pivot)
        
        #self.secondary_item = Guns.JERICHO.value #Guns.REVOLVER.value
        #self.secondary_item = Guns.NAIL_GUN.value #Guns.REVOLVER.value
        #self.secondary_item = Magnet(name = "magnet",carrier = self)
        #self.secondary_item = Guns.NAIL_GUN.value
        self.secondary_item = self.game_manager.guns_manager.nail_gun()
        self.secondary_item.carrier = self
        #goto treure
        self.secondary_item.bullets_in_chamber=5
        #

        self.secondary_item.x += 1.2

        #
        self.color = color.blue



        #bars:
        self.max_integrity = max_integrity

        self.health_bar = CounterBar(position = (-.8,.4,0))

        self.health_bar.update_bar(active = self.integrity, updated_max = self.max_integrity)

    def update_camera_pivot(self):
        sp = world_position_to_screen_position(self.position)

        if abs(sp.x) > 0.65 or abs(sp.y) > 0.3: #out of 
            self.camera_pivot.position += self.movement_vector * time.dt

    def parry(self):
        self.sword.parry()


    def interact(self):
        interaction_body = WorldElement(model = "cube", element_type = ElementType.IGNORE,scale = (2,2,2),position = self.position)
        interaction_body.color = color.yellow
        info = interaction_body.intersects(ignore = [self])
        
        min_distance = 1000
        nearest_entity = None

        if info.hit:
            for entity in info.entities:
                if entity.interactive == True or entity.dialogable == True:
                    current_d = distance(self,entity)
                    if current_d < min_distance:
                        min_distance = current_d
                        nearest_entity = entity

        if nearest_entity != None:
            if nearest_entity.interactive:
                nearest_entity.get_interacted()
            elif nearest_entity.dialogable:
                nearest_entity.get_dialogued()
        destroy(interaction_body,delay = 0)



    def input(self,key):
        if key == CustomKeys.PAUSE:
            self.game_manager.pause()

        if key == CustomKeys.GO_BACK and self.game_manager.game_status == GameState.PAUSE:
            self.game_manager.end_pause()

        if self.game_manager.game_status != GameState.RUN:
            return

        if key == CustomKeys.PARRY:
            self.parry()
        if key == CustomKeys.USE_SECONDARY_ITEM:
            self.secondary_item.use()

        if key == CustomKeys.STOP_USING_SECONDARY_ITEM:
            self.secondary_item.stop_using()

        if key == CustomKeys.RELOAD:
            self.secondary_item.reload()

        if key == CustomKeys.INTERACT:
            self.interact()


        if key == CustomKeys.CHANGE_SECONDARY_ITEM:
            destroy(self.secondary_item,delay = 0)

            self.secondary_item = Magnet(name = "magnet",carrier = self)

       
        if key == "x":
            self.get_hit(1,0,self)
       

    ####deixo aquesta funcio aqui provisionalment. mes endavant creare la classe pistola
    def get_hit(self,damage,push,emitter):
        super().get_hit(damage,push,emitter)
        camera.shake()
        self.health_bar.update_bar(active = self.integrity)

    def die(self):
        pass


    def update(self):
        if self.game_manager.game_status != GameState.RUN:
            return


        if self.integrity <= 0:
            self.die()
            invoke(self.game_manager.game_over,delay = 0) #el delay sera lo q trigui en morirse


        self.update_camera_pivot()
        self.sword.update_sword()
        self.secondary_item.update_flying()

        #self.position += (Vec3(0,1,0)*held_keys[CustomKeys.UP] + Vec3(0,-1,0)*held_keys[CustomKeys.DOWN] + Vec3(-1,0,0)*held_keys[CustomKeys.LEFT] + Vec3(1,0,0)*held_keys[CustomKeys.RIGHT])*time.dt*self.speed

        #desplaçament:::
        d_vec = Vec3(0,0,0)
        if held_keys[CustomKeys.UP]:
            d_vec[1] += 1
        if held_keys[CustomKeys.DOWN]:
            d_vec[1] -= 1
        if held_keys[CustomKeys.LEFT]:
            d_vec[0] -= 1
        if held_keys[CustomKeys.RIGHT]:
            d_vec[0] += 1
        
        self.movement_vector = d_vec.normalized() * self.speed

        self.position += d_vec.normalized() * self.speed * time.dt


