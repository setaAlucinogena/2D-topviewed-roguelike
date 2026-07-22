from enum import Enum
from gun import Gun

from ursina import Entity,Vec3

class Guns(Enum):
    REVOLVER = Gun(
                   carrier=Entity(),
                   name = "revolver",
                   capacity = 6,
                   period = .65,
                   reload_time = .7,
                   bullet_damage=3,
                   bullet_speed=20,
                   bullet_push=200,
                   shooting_sound_name="revolver_shoot.mp3",
                   reloading_sound_name="revolver_reload.mp3",
                   empty_sound_name="empty_gun.mp3"
                   )

    JERICHO = Gun(
                   carrier=Entity(),
                   name = "jericho handgun",
                   capacity = 10,
                   period = .1,
                   reload_time = .15,
                   bullet_damage=3,
                   bullet_speed=27,
                   bullet_push=200,
                   shooting_sound_name="revolver_shoot.mp3",
                   reloading_sound_name="revolver_reload.mp3",
                   empty_sound_name="empty_gun.mp3"
                   )
    
    NAIL_GUN = Gun(
        carrier = Entity(),
        name = "nail_gun",
        capacity = 20,
        period = .2,
        reload_time = .7,
        bullet_damage = 2,
        bullet_speed = 20,
        bullet_push = 0,
        shooting_sound_name="",
        reloading_sound_name="",
        empty_sound_name="empty_gun.mp3"
        
        )