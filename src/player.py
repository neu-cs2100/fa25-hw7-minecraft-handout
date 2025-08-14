import sys
from typing import Optional

from entity import Entity
from living_entity import LivingEntity, FIGHTING_RANGE

class Player(LivingEntity):
    """The player, who is controlled by key presses."""
    
    def __init__(self) -> None:
        super().__init__(
            type_name="Steve",
            image_file_name="Steve.png", 
            max_hearts=20,
            attack_strength=6
        )
        self.last_key_pressed: Optional[str] = None
    
    def _is_in_fighting_range(self, entity: 'Entity') -> bool:
        """
        Checks whether entity is within fighting range of this living entity.
        This raises ValueError if either does not have a position.
        """
        from game import Game
        
        this_pos = Game.GAME.get_position(self)
        entity_pos = Game.GAME.get_position(entity)
        
        if this_pos is None or entity_pos is None:
            raise ValueError("Both entities must have positions on the board")
        
        return Game.GAME.calculate_distance(self, entity) < FIGHTING_RANGE
    
    def _attack_nearby_threats(self) -> None:
        """Attack any nearby aggressive mobs."""
        from game import Game
        from mob import Mob
        
        made_attack = False
        entities = Game.placed_entities
        
        for entity in entities:
            if (self._is_in_fighting_range(entity) and 
                isinstance(entity, Mob) and 
                entity.is_aggressive):
                self.attack(entity)
                made_attack = True
        
        if not made_attack:
            Game.GAME.add_text(f"There were no nearby threats for {self.type} to attack.")
    
    def tick(self) -> None:
        """Handle player input and update state."""
        from game import Game
        
        if self.last_key_pressed in ["arrow-right", "s"]:
            self.move_right()
        elif self.last_key_pressed in ["arrow-left", "a"]:
            self.move_left()
        elif self.last_key_pressed in ["arrow-up", "w"]:
            self.move_up()
        elif self.last_key_pressed in ["arrow-down", "z"]:
            self.move_down()
        elif self.last_key_pressed == "/":
            self._attack_nearby_threats()
        elif self.last_key_pressed in ["space", None]:
            pass  # Do nothing
        else:
            Game.GAME.add_text(f"I don't know how to handle {self.last_key_pressed}")
        
        # Finally, set last_key_pressed to None
        self.last_key_pressed = None
    
    def exit(self) -> None:
        """Exit the game when player dies."""
        super().exit()
        sys.exit(0)