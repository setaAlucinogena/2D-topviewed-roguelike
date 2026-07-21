
from enemy import Enemy
from dialogue_scene import DialogueScene
from ursina import *

from game_manager import GameState


class Mosquito(Enemy):
    def __init__(self,position):
        super().__init__(
            position = position,
            integrity = 20, 
            hit_cooldown = 1,
            hit_damage = 2,
            hit_range = 1.5,
            hit_push = 2,
            speed = 2,
            attack_distance = 4,#lo de abaix treureho despres
            dialogue_scene = DialogueScene(animation_texture_name = "test1.png",background="test0.png"),
            dialogable=True

            )
        self.color = color.black
        self.shake_duration = .2
        self.able_to_shake = True
        self.sprint_speed = self.speed * 2
        self.sprint_duration = 1.5
        self.able_to_sprint = True
        self.sprinting = False


    def reload_shake(self):
        self.able_to_shake = True

    def orientate(self):
        
        print("aa?")
        
        if self.able_to_shake:
            self.able_to_shake = False
            invoke(self.reload_shake,delay=self.able_to_shake)
            self.shake(magnitude = 2,direction = self.up,duration = self.shake_duration)

    def stop_sprint(self,tmp):
        self.sprinting = False
        self.speed = tmp


    def attack(self):#ho vull tenir en una funcio apart aixi puc cridar el atac desde fora
        tmp = self.speed
        self.speed = self.sprint_speed
        invoke(self.stop_sprint,tmp,delay = self.sprint_duration)
        super().orientate()



    def update(self):
        if self.game_manager.game_status != GameState.RUN:
            return
        super().update()

        if distance(self,self.game_manager.player) <= self.attack_distance and self.able_to_sprint and not self.sprinting:
            self.attack()

        if self.sprinting:
            
        else:
            self.rotation_z += random.uniform(-10,10)
            #invoke(self.reload_attack(),delay = self.)

        self.follow()