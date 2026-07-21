from turtle import position
from ursina import *
from enemy import Enemy
from game_manager import GameManager, GameState
from world_element import WorldElement,ElementType
from player import Player
from sub_room import SubRoom
from mosquito import Mosquito
from explosion import Explosion
from dialogue_scene import DialogueScene
app = Ursina()

gm = GameManager()

SubRoom.game_manager = gm
WorldElement.game_manager = gm
Player.game_manager = gm
DialogueScene.game_manager = gm


p = Player(position = (0,0,gm.characters_z),integrity = 5, max_integrity = 7)
gm.player = p

r = SubRoom(position = (0,0,gm.ground_z),scale = 10,local_id = 1)
f = Mosquito(position = (5,0,gm.characters_z))
#ds = DialogueScene(animation = Animation(name = "viejo.png"))

gm.game_status = GameState.RUN
print(gm.game_status)
#def input(key):
#    if key == "e":
#        ds.initiate()
#    if key == "t":
#        ds.end()
        #e = Explosion(position = (0,0,0),potency = 4)

#we = WorldElement(position = (3,0,0),hittable = True,element_type=ElementType.MOBILE)
#e = Enemy(position = (3,0,gm.characters_z))    
#e.color = color.green


app.run()