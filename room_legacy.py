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

        #self.objects = []

        self.colliders = []
        
        self.loaded = False
        self.freezed = True
        self.local_id = local_id

        #goto treu-ho
    #    self.spawn_walls_colliders()

        self.triangles = []
        self.lines = []
        self.build()

        self.double_sided = True



    def build_square(self,position,width,height):#en retrospec, perque no he creat dos rectangles i llavors pillat els punts com a punt de mesh i ja? lol.
        x = position[0]
        y = position[1]

        self.triangles.append(Vec3(x,y,0))
        self.triangles.append(Vec3(x + width,y,0))
        self.triangles.append(Vec3(x+width,y + height,0))
            
        self.triangles.append(Vec3(x,y,0))
        self.triangles.append(Vec3(x,y + height,0))
        self.triangles.append(Vec3(x+width,y + height,0))
        


    def build(self):

        #self.extremes = [0]

        width = random.randint(4,23)
        height = random.randint(4,23)

        self.build_square(Vec3(0,0,0),width,height)

        if random.randint(0,2) == 0:
            width_2 = random.randint(4,20)
            height_2= random.randint(4,20)

            self.build_square(Vec3(0+width,0,0), width_2,height_2)

        else:
            width_2 = random.randint(4,20)
            height_2= random.randint(4,20)

            self.build_square(Vec3(0,0+height,0), width_2,height_2)

        #self.extremes.append(max(width,width_2))
        #self.extremes.append(max(height,height_2))

        self.model = Mesh(vertices = self.triangles,mode = "triangle", thickness = 5)
        self.walls()


    #def no_duplicate(self,l):#hi ha una manera mes eficient de fer aixo pero ho fare despres
    #    wo_dup = []
    #    wo_dup.append(l[0])
        
        

        #return wo_dup




'''
    def walls(self):
        
            print("walls?")
            t_distinct = set(self.triangles)
            degrees = [0] * len(t_distinct)
            max_d = 2
            print(t_distinct)
            for i,point in enumerate(t_distinct):
                for j,point2 in enumerate(t_distinct):
                    if i != j and (point[0] == point2[0] or point[1] == point2[1]) and not (point[0] == point2[0] and point[1] == point2[1]):
                        duplicated_line = False
                    
                        for l in self.lines:
                            if (point in l.model.vertices and point2 in l.model.vertices):
                                duplicated_line = True

                        if not duplicated_line:
                            degrees[j] = degrees[j] + 1
                            degrees[i] = degrees[i] + 1
                            
                            continious_line = Entity(position=self.position, model=Mesh(
                                    vertices=(point, point2),
                                    mode='line',
                                    thickness=7,
                                    ), color=color.red)

                            continious_line.z -=.1
                            self.lines.append(continious_line)

            for i,cl in enumerate(self.lines):
                p_a = list(t_distinct).index(cl.model.vertices[0])
                p_b = list(t_distinct).index(cl.model.vertices[1])

                if (degrees[p_a] > max_d and
                    degrees[p_b] > max_d):
                    self.lines.pop(i)
                    destroy(cl)
                    #degrees[p_a] -= 1
                    #degrees[p_b] -= 1
                    
                
            
                        
            print(f"n linies: {len(self.lines)}")
            print(degrees)
'''

'''
    def walls(self):
        
        print("walls?")
        t_distinct = set(self.triangles)
        degrees = [0] * len(t_distinct)
        max_d = 2
        print(t_distinct)
        for i,point in enumerate(t_distinct):
            for j,point2 in enumerate(t_distinct):
                if i != j and (point[0] == point2[0] or point[1] == point2[1]) and not (point[0] == point2[0] and point[1] == point2[1]):
                    duplicated_line = False
                    
                    for l in self.lines:
                        if (point in l.model.vertices and point2 in l.model.vertices):
                            duplicated_line = True

                    if not duplicated_line:
                        degrees[j] = degrees[j] + 1
                        degrees[i] = degrees[i] + 1
                            
                        continious_line = Entity(position=self.position, model=Mesh(
                                vertices=(point, point2),
                                mode='line',
                                thickness=7,
                                ), color=color.red)

                        continious_line.z -=.1
                        self.lines.append(continious_line)

        for i,cl in enumerate(self.lines):
            if (degrees[list(t_distinct).index(cl.model.vertices[0])] > max_d and
                degrees[list(t_distinct).index(cl.model.vertices[1])] > max_d):
                self.lines.pop(i)
                destroy(cl)
                
            
                        
        print(degrees)
'''
                            
'''
    def at_least_one_extreme_per_point(self,point1,point2):
        return (
            (point1[0] in self.extremes or point1[1] in self.extremes) or
            (point2[0] in self.extremes or point2[1] in self.extremes)
            ) 

    def walls(self):
        print("walls?")
        t_distinct = set(self.triangles)
        print(t_distinct)
        for i,point in enumerate(t_distinct):
            for j,point2 in enumerate(t_distinct):
                if (i != j and (point[0] == point2[0] or point[1] == point2[1]) and not (point[0] == point2[0] and point[1] == point2[1])):
                    duplicated_line = False
                    
                    for l in self.lines:
                        if (point in l.model.vertices and point2 in l.model.vertices):
                            duplicated_line = True

                    if not duplicated_line:                            
                        continious_line = Entity(position=self.position, model=Mesh(
                                vertices=(point, point2),
                                mode='line',
                                thickness=7,
                                ), color=color.red)

                        continious_line.z -=.1
                        self.lines.append(continious_line)
'''     

        
        


    #def spawn_walls_colliders(self):
        #en el futur podran ser colliders fets de mesh, perque els terres no seran full cuadrats
    #    upper = WorldElement(position = self.position,scale = (self.scale[0],1,3),model = "cube")
    #    lower = WorldElement(position = self.position,scale = (self.scale[0],1,2),model = "cube")
    #    upper.y+=self.scale[1] / 2
    #    lower.y-=self.scale[1] / 2
    #    upper.collider.visible = True
    #    lower.collider.visible = True
    #    self.colliders.append(upper)
    #    self.colliders.append(lower)



    #def get_possible_next_rooms(self,all_rooms):
        



        

        
        
    
    
        