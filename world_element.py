from ursina import *

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

    def __init__(self,position,parent = scene, scale = 1,element_type = ElementType.STATIC,model = "quad",integrity = 32,hittable = False, interactive = False,hit_animation = None):
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

        
        self.hit_animation = hit_animation

    def decompose(self):
        destroy(self,delay = 1)

    def get_hit(self, damage, push, emitter):
        if self.hittable:#programacio defensiva
            self.integrity -= damage
            if self.element_type == ElementType.MOBILE:
                push_vec = Vec3(self.x-emitter.x,self.y-emitter.y,0)
                self.position += push_vec.normalized()*push*time.dt

            self.animate_color(color.white, duration = .5, curve = curve.in_bounce_boomerang)##puc canviar la corva ngl
   

    def update(self):
        #if WorldElement.game_manager != GameStates.RUN:
        #    return

        if self.integrity <= 0 and self.hittable:
            self.decompose()






