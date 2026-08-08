from ursina import *

from game_manager import GameState
#from ursina.prefabs.trail_renderer import TrailRenderer

#import game_manager
#from game_states import GameStates
#from game_manager import GameManager


class ElementType:
    STATIC = 0
    MOBILE = 1
    IGNORE = 2
    TRIGGER = 3



class WorldElement(Entity):
    game_manager = None # s'haura d'inicialitzar a l'inici de tot

    def __init__(self,position,parent = scene, scale = 1,element_type = ElementType.STATIC,model = "quad",integrity = 32,hittable = False, interactive = False, parryable = False,hit_animation = None,dialogable = False, dialogue_scene = None,magnetic = False):
        super().__init__(
            model = model,
            position = position,
            scale = scale,
            collider = "box",
            parent = parent
            )


        self.double_sided = True
        self.element_type = element_type
        self.integrity = integrity

        self.hittable = hittable
        self.interactive = interactive
        self.parryable = parryable

        self.magnetic = magnetic
        self.dragged = False
        self.hit_while_dragged = []

        
        self.hit_animation = hit_animation
        self.dialogable = dialogable
        self.dialogue_scene = dialogue_scene


        #self.tr = TrailRenderer(size=(1,1), segments=8, min_spacing=.05, fade_speed=0, parent=self, color = color.black)
        #self.tr.disable()

    def decompose(self):
        self.stop_being_dragged()
        destroy(self,delay = .75)
        self.disable()

    def temporal_non_hittable(self,time):
        self.hittable = False
        invoke(self.make_hittable_again,delay = time)
        self.alpha = 175
    def make_hittable_again(self):
        self.hittable = True
        self.alpha = 255

    def get_hit(self, damage, push, emitter):
        if self.hittable:#programacio defensiva
            self.integrity -= damage
            #if self.element_type == ElementType.MOBILE:
            #    push_vec = Vec3(self.x-emitter.x,self.y-emitter.y,0)
            #    throw_back_vec = self.position + push_vec.normalized()*push*time.dt
            #    self.animate_position(throw_back_vec, duration=.25)
            self.animate_color(color.red, duration = .5, curve = curve.in_bounce_boomerang)##puc canviar la corva ngl


    def get_dialogued(self):
        self.dialogue_scene.initiate()
    
    def must_not_update(self):
        return(self.game_manager.game_states != GameState.RUN)


    def get_attracted_by_magnet(self,strength,emitter,ignore_list):
        tmp = Vec3(emitter.world_position[0]-self.x, emitter.world_position[1]-self.y, 0)

        self.being_dragged(tmp,strength,ignore_list)

    def being_dragged(self,direction,strength,ignore_list):
        #self.tr.enable()
        #tmp = Vec3(self.world_position[0]-self.x, self.world_position[1]-self.y,0)
        

        self.position += direction.normalized() * strength * time.dt

        self.dragged = True
        hit_info = self.intersects(ignore = [self] + ignore_list)
        if hit_info.hit:
            for entity in hit_info.entities:
                if entity.hittable == True:
                    if entity not in self.hit_while_dragged:
                        self.hit_while_dragged.append(entity)
                        entity.get_hit(damage = 2, push = 2, emitter = self)

    def stop_being_dragged(self):
        self.position = self.world_position

        self.dragged = False
        self.hit_while_dragged = []
        #destroy(self.tr)
        #self.tr = TrailRenderer(size=(1,1), segments=8, min_spacing=.05, fade_speed=0, parent=self, color = color.black)
        
        #self.tr.disable()

    def update(self):
        #if WorldElement.game_manager != GameStates.RUN:
        #    return
        
        #if self.must_not_update():
            
            

        if self.integrity <= 0 and self.hittable:
            self.decompose()






