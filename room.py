from ursina import *

from world_element import WorldElement




class Room(Entity):
    game_controller = None
    def __init__(self,position,scale,local_id):
        super().__init__(
            scale = scale,
            color = color.cyan, 
            position = position
            
            )
        self.triangles = []
        self.lines = []
        #self.build()
    def walls(self,triangles):
        
            t_distinct = set(triangles)
            local_lines = []
            for i,point in enumerate(t_distinct):
                for j,point2 in enumerate(t_distinct):
                    if i != j and (point[0] == point2[0] or point[1] == point2[1]) and not (point[0] == point2[0] and point[1] == point2[1]):
                        duplicated_line = False
                    
                        for l in local_lines:
                            if (point in l.model.vertices and point2 in l.model.vertices):
                                duplicated_line = True

                        if not duplicated_line:
                            
                            continious_line = Entity(position=self.position, model=Mesh(
                                    vertices=(point, point2),
                                    mode='line',
                                    thickness=7,
                                    ), color=color.red)

                            continious_line.z -=.1
                            local_lines.append(continious_line)
            return local_lines

    def build_square(self,position,width,height):#en retrospec, perque no he creat dos rectangles i llavors pillat els punts com a punt de mesh i ja? lol.
        x = position[0]
        y = position[1]

        local_triangles = []
        local_triangles.append(Vec3(x,y,0))
        local_triangles.append(Vec3(x + width,y,0))
        local_triangles.append(Vec3(x+width,y + height,0))
            
        local_triangles.append(Vec3(x,y,0))
        local_triangles.append(Vec3(x,y + height,0))
        local_triangles.append(Vec3(x+width,y + height,0))

        self.triangles.append(local_triangles)#no, no vull concatenar, vull afegir una llista a una llista
        ll = self.walls(local_triangles)
        self.lines.append(ll)
'''
    def coincidents(self,l1,l2):
        d1 = l1.vertices[1] / l1.vertices[0] 
        d2 = l2.vertices[1] / l2.vertices[0] 

        
    def merge(self,l1,l2):
        pass

    def build(self):
        width = random.randint(4,23)
        height = random.randint(4,23)

        #q1:
        self.build_square(Vec3(0,0,0),width,height)

        if random.randint(0,2) == 0:

            #q2:
            self.build_square(Vec3(0+width,0,0), random.randint(4,20),random.randint(4,20))

        else:
            #q2
            self.build_square(Vec3(0,0+height,0), random.randint(4,20),random.randint(4,20))
            
        for l1 in self.lines[0]:
            for l2 in self.lines[1]:
                if self.coincidents(l1,l2):
                    self.clean_merge(l1,l2)
'''