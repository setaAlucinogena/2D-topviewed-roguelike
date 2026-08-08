from ursina import *
from enemy import Enemy
from game_manager import GameManager, GameState
from world_element import WorldElement,ElementType
from player import Player
from room import Room
from mosquito import Mosquito
from explosion import Explosion
from dialogue_scene import DialogueScene

from guns_manager import GunsManager
#from sword_manager import SwordManager

from ursina import Shader

pixelation_shader = Shader(
fragment='''
#version 150

uniform sampler2D tex;
in vec2 window_size;
in vec2 uv;
out vec4 color;


void main() {
    float Pixels = 1600.0;
    float dx = 9.0 * (1.0 / Pixels);
    float dy = 16.0 * (1.0 / Pixels);
    vec2 new_uv = vec2(dx * floor(uv.x / dx), dy * floor(uv.y / dy));
    color = texture(tex, new_uv);
}
''')

app = Ursina()

gm = GameManager()

gm.guns_manager_setter(GunsManager())

Room.game_manager = gm
WorldElement.game_manager = gm
Player.game_manager = gm
DialogueScene.game_manager = gm


p = Player(position = (0,0,gm.characters_z),integrity = 5, max_integrity = 7)
gm.player = p

r = Room(position = (0,0,gm.ground_z),scale = 1,local_id = 1)
f = Mosquito(position = (5,0,gm.characters_z))
#ds = DialogueScene(animation = Animation(name = "viejo.png"))

gm.game_status = GameState.RUN



#def input(key):
#    if key == "e":
#        ds.initiate()
#    if key == "t":
#        ds.end()
        #e = Explosion(position = (0,0,0),potency = 4)

#we = WorldElement(position = (3,0,0),hittable = True,element_type=ElementType.MOBILE)
#e = Enemy(position = (3,0,gm.characters_z))    
#e.color = color.green

#camera.shader = pixelation_shader
#EditorCamera()
app.run()