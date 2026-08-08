from projectile import Projectile
from ursina import color,destroy,Vec3,distance
from world_element import WorldElement,ElementType

class Nail(Projectile):
    def __init__(self,position,direction, dont_hurt,guided_towards = None):
        super().__init__(
            position = position,
            damage = 1,
            push = 0,
            direction = direction,
            speed = 12,
            dont_hurt = dont_hurt,
            guided_towards=guided_towards
            )
        self.dragged_entity = None

    def check_collisions(self):
        collisions_info = self.intersects(ignore = [self])
        if collisions_info.hit:
            for entity in collisions_info.entities:
                if entity not in self.dont_hurt and (entity.element_type != ElementType.IGNORE and entity.element_type != ElementType.TRIGGER):#per algun motiu no va quan el projectil no fa mal al enemic
                    print(entity.element_type)

                    if entity.element_type == ElementType.STATIC:
                        self.speed = 0
                        self.tr.disable()


                        self.position -= self.direction *1
                        

                        if self.dragged_entity != None:
                            self.dragged_entity.tr.disable()
                            
                            
                            self.dragged_entity.position -= self.direction * 1
                        else:
                            self.magnetic = True



                    if entity.hittable:
                        entity.get_hit(damage = self.damage, push = 0, emitter = self)

                        self.dont_hurt.append(entity)
                        #if not self.dragged:
                        entity.dragged = True
                        self.dragged_entity = entity
                        #entity.being_dragged(self.forward,self.speed,[self])

                    self.parryable = False
                    self.color = color.gray

    def update(self):
        if not self.magnetic and self.speed != 0:#millorar el control dels estats del clau perque aixo es can pixa i rellisca
                                                   #el trailrenderer se li queda pillat al clau que mata l'entiat. o sigui fatal
            super().update()
        else:
            if distance(self,self.game_manager.player) < 1.2:#canviar el magic number
                
                print("augmentar el n de claus del inventari, aixo ho fare quan tingui inventari")
                destroy(self)
            
        

        if self.dragged_entity != None and self.dragged_entity != 0:
            self.tr.disable()
            if self.dragged_entity.integrity <= 0:  
                self.dragged_entity = 0
                self.magnetic = True
            else:
                self.dragged_entity.being_dragged(self.direction,self.speed,[self])

        #if self.dragged_entity == 0: #si esta morta
        #    self.magnetic = True

