from ursina import *
from enemy import Enemy
from game_manager import GameManager
from world_element import WorldElement,ElementType
from player import Player

app = Ursina()

gm = GameManager()
WorldElement.game_manager = gm
Player.game_manager = gm


p = Player(position = (0,0,0))
gm.player = p

#we = WorldElement(position = (3,0,0),hittable = True,element_type=ElementType.MOBILE)
e = Enemy(position = (3,0,0))    
e.color = color.green


app.run()