from enum import Enum
class ItemType(Enum):
    SWORD = 0
    FLYING_WEAPON = 1
    CONSUMIBLE = 2
    UNUSABLE = 3

class Item:
    def __init__(self,name,custom_type,texture,custom_object): #type determinates wich actions are available for the item
        name = name
        custom_type = custom_type
        texture = texture
        custom_object = custom_object



        