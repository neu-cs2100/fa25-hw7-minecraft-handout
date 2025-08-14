import random
from enum import Enum
from typing import Optional, ClassVar, Any

from game import Game
from living_entity import LivingEntity
from status import Status

NOISINESS: float = 0.1

class Behavior(Enum):
    PASSIVE = "Passive"
    HOSTILE = "Hostile"
    NEUTRAL = "Neutral"
    BOSS = "Boss"

class Mob(LivingEntity):
    """A Minecraft mob."""
    
    minim: ClassVar[Optional[Any]] = None
    
    def __init__(
        self, 
        type_name: str, 
        max_hearts: int, 
        behavior: Behavior, 
        attack_strength: int, 
        image_file_name: str, 
        sound_file_name: Optional[str] = None, 
        subtitle: Optional[str] = None
    ) -> None:
        super().__init__(type_name, image_file_name, max_hearts, attack_strength)
        self.behavior: Behavior = behavior
        self.subtitle: Optional[str] = subtitle
        
        # Load sound file if provided
        if sound_file_name is None:
            self.sound: Optional[Any] = None
        else:
            # Assuming minim has a load_file method
            self.sound = None if Mob.minim is None else Mob.minim.load_file(f"data/sounds/{sound_file_name}")
    
    @property
    def is_aggressive(self) -> bool:
        """Determines if the mob is currently aggressive."""
        if not self.is_alive:
            return False
        
        if self.behavior == Behavior.PASSIVE:
            return False
        elif self.behavior in [Behavior.BOSS, Behavior.HOSTILE]:
            return True
        elif self.behavior == Behavior.NEUTRAL:
            # Assuming Status is an enum with INJURED value
            return self.status == Status.INJURED
        
        return False
    
    def attack(self, victim: 'LivingEntity') -> None:
        """
        Attacks victim, doing attack_strength hearts of damage.
        Raises ValueError unless is_aggressive is True.
        """
        if not self.is_aggressive:
            raise ValueError("Mob must be aggressive to attack")
        super().attack(victim)
    
    def _make_noise(self) -> None:
        """Private method to make mob sounds."""
        if self.subtitle is not None:
            Game.GAME.add_text(self.subtitle)
        
        if self.sound is not None:
            self.sound.play()
            self.sound.rewind()
    
    def tick(self) -> None:
        """Update the mob's behavior each game tick."""
        # Once in a while, have the mob make a noise
        if random.random() < NOISINESS:
            self._make_noise()
        
        if self.is_aggressive:
            from living_entity import FIGHTING_RANGE
            if Game.GAME.calculate_distance(self, Game.GAME.player) <= FIGHTING_RANGE:
                self.attack(Game.GAME.player)
            else:
                self.move_towards(Game.GAME.player)
        else:
            self.move_randomly()