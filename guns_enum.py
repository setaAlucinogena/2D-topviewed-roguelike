from enum import Enum
from gun import Gun

from ursina import Entity,Vec3

class Guns(Enum):
    REVOLVER = Gun(
                   carrier=Entity(),
                   capacity = 6,
                   period = .65,
                   reload_time = .45,
                   bullet_force=1,
                   bullet_speed=10,
                   bullet_push=6,
                   shooting_sound_name="revolver_shoot.mp3",
                   reloading_sound_name="revolver_reload.mp3",
                   empty_sound_name="empty_gun.mp3"
                   )