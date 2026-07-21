from enum import Enum
from gun import Gun

from ursina import Entity,Vec3

class Guns(Enum):
    REVOLVER = Gun(
                   carrier=Entity(),
                   capacity = 6,
                   period = .65,
                   reload_time = .7,
                   bullet_damage=1,
                   bullet_speed=20,
                   bullet_push=200,
                   shooting_sound_name="revolver_shoot.mp3",
                   reloading_sound_name="revolver_reload.mp3",
                   empty_sound_name="empty_gun.mp3"
                   )

    JERICHO = Gun(
                   carrier=Entity(),
                   capacity = 10,
                   period = .1,
                   reload_time = .15,
                   bullet_damage=2,
                   bullet_speed=27,
                   bullet_push=200,
                   shooting_sound_name="revolver_shoot.mp3",
                   reloading_sound_name="revolver_reload.mp3",
                   empty_sound_name="empty_gun.mp3"
                   )
