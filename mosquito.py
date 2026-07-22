
from enemy import Enemy
from dialogue_scene import DialogueScene
from ursina import *

from game_manager import GameState
from ursina.prefabs.trail_renderer import TrailRenderer


class Mosquito(Enemy):
    def __init__(self,position):
        super().__init__(
            position = position,
            integrity = 3, 
            hit_cooldown = 1,
            hit_damage = 1,
            hit_range = 1,#realment no es fa servir en aquest enemic pero bno
            hit_push = 2,
            speed = 2,
            #attack_distance = 4,#lo de abaix treureho despres
            attack_distance = 30,#lo de abaix treureho despres
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

        self.tr = TrailRenderer(size=(.2,.2), segments=8, min_spacing=.05, fade_speed=0, parent=self, color = color.black)


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

    def reload_sprint(self):
        self.able_to_sprint = True

    def attack(self):#ho vull tenir en una funcio apart aixi puc cridar el atac desde fora
        tmp = self.speed
        self.speed = self.sprint_speed
        self.able_to_sprint = False
        invoke(self.reload_sprint,delay = 5)
        invoke(self.stop_sprint,tmp,delay = self.sprint_duration)
        self.sprinting = True
        super().orientate()
        

    def go_back(self):
        new_pos = Vec3(self.position[0]+self.back[0],self.position[1]+self.back[1],0)*3.5
        self.animate_position(new_pos, duration = .75)
        self.temporal_non_hittable(time = 1.2)


    def update(self):
        if self.game_manager.game_status != GameState.RUN:
            return
        super().update()

        if distance(self,self.game_manager.player) <= self.attack_distance and self.able_to_sprint and not self.sprinting:
            self.attack()

        if self.sprinting:
            print("YES")
            
            hit_info = raycast(self.position,direction = (self.game_manager.player.position - self.position),distance = self.hit_range,ignore = [self])
            if hit_info.hit:
                
                for entity in hit_info.entities:
                    
                    #if entity.hittable == True and entity == self.game_manager.player:
                    if entity.hittable == True:
                        print("Hitting smth")
                        hit_info.entity.get_hit(self.hit_damage, self.hit_push, self)
                        self.stop_sprint(2) #solucionar despres aixo, crear variables de current speed i walk speed i sprint speed i tal
                        self.go_back()
        else:
            print("NO")
            self.rotation_z += random.uniform(-10,10)
            #invoke(self.reload_attack(),delay = self.)

        self.follow()