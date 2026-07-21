from sub_room import SubRoom


#mhe de pensar bé el algoritme de generacio d'aixo

class Room:
    def __init__(self,id,sub_rooms):
        self.id = id

        self.to_assemble = sub_rooms
        self.assembled = []
        
    def get_candidates(self):
        pass

    #def assemble_room(self):
        # = self.to_assemble[0] 

        #while(len(self.to_assemble != 0)):
        #    candidate_rooms = self.get_candidates(last_room) #llista de [[room,index]]
        #    for 