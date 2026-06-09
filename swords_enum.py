from enum import Enum
from sword import Sword
from ursina import Entity

class Swords(Enum):
    DEFAULT_SWORD = Sword(
        scale = (1.5,.45),
        carrier = Entity(),
        parrying_time = .5,
        parry_cooldown = .4,
        rotation_increment = 300,
        parry_level = 1
        )