from abc import ABC
from enum import Enum
import random

from entity import Entity
from game import Game
from status import Status

FIGHTING_RANGE: float = 3.0  # Distance within which entities can fight

class LivingEntity(Entity, ABC):
    """A living entity, such as a Mob or Player in the game."""
    
    def __init__(
        self,
        type_name: str,
        image_file_name: str,
        max_hearts: int,
        attack_strength: int
    ) -> None:
        super().__init__(type_name, image_file_name)
        self._max_hearts: int = max_hearts
        self._attack_strength: int = attack_strength
        self._num_hearts: int = max_hearts
    
    @property
    def status(self) -> Status:
        """Get the current status based on health."""
        if self._num_hearts == self._max_hearts:
            return Status.HEALTHY
        elif self._num_hearts == 0:
            return Status.DEAD
        else:
            return Status.INJURED
    
    @property
    def is_alive(self) -> bool:
        """Check if the entity is alive."""
        return self.status != Status.DEAD
    
    def take_damage(self, damage: int) -> None:
        """
        Takes up to damage hearts of damage, to a maximum of num_hearts,
        printing a message with the amount of damage taken and the
        resulting status.
        """
        actual_damage = min(damage, self._num_hearts)
        self._num_hearts -= actual_damage
        text = "heart" if actual_damage == 1 else "hearts"
        Game.GAME.add_text(f"{self.type} took {actual_damage} {text} of damage and is now {self.status}.")
        if self.status == Status.DEAD:
            self.exit()
    
    def attack(self, victim: 'LivingEntity') -> None:
        """Attacks victim, doing attack_strength hearts of damage."""
        Game.GAME.add_text(f"{self.type} attacked {victim.type}.")
        victim.take_damage(self._attack_strength)
    
    def _move(self, delta_x: int, delta_y: int) -> None:
        """Private method to handle movement logic."""
        position = Game.GAME.get_position(self)
        if position is None:
            raise ValueError("Entity must be on the board to move")
        
        new_x = position.x + delta_x
        new_y = position.y + delta_y
        
        if Game.GAME.is_in_bounds(new_x, new_y) and Game.GAME.is_empty(new_x, new_y):
            Game.GAME.place(self, new_x, new_y)
    
    def move_right(self) -> None:
        """
        Moves right one cell, or stays in the same place, if that cell is
        occupied by a LivingEntity or out of bounds. This should raise
        ValueError if this living entity is not on the board.
        """
        self._move(1, 0)
    
    def move_left(self) -> None:
        """
        Moves left one cell, or stays in the same place, if that cell is
        occupied by a LivingEntity or out of bounds.
        """
        self._move(-1, 0)
    
    def move_up(self) -> None:
        """
        Moves up one cell, or stays in the same place, if that cell is
        occupied by a LivingEntity or out of bounds.
        """
        self._move(0, -1)
    
    def move_down(self) -> None:
        """
        Moves down one cell, or stays in the same place, if that cell is
        occupied by a LivingEntity or out of bounds.
        """
        self._move(0, 1)
    
    def move_randomly(self) -> None:
        """
        Moves randomly to an adjacent unoccupied cell. Cells
        are considered adjacent if they are to the right, left, up,
        or down (i.e., changing by 1 either the x-coordinate or the
        y-coordinate but not both).
        """
        old_position = Game.GAME.get_position(self)
        if old_position is None:
            raise ValueError("Entity must be on the board to move")
        
        remaining_directions = [0, 1, 2, 3]
        
        while Game.GAME.get_position(self) == old_position and remaining_directions:
            direction = random.choice(remaining_directions)
            remaining_directions.remove(direction)
            
            if direction == 0:
                self.move_up()
            elif direction == 1:
                self.move_down()
            elif direction == 2:
                self.move_left()
            else:
                self.move_right()
    
    def move_towards(self, player: 'Player') -> None:
        """
        Tries to move to an adjacent cell closer to player. Cells
        are considered adjacent if they are to the right, left, up,
        or down (i.e., changing by 1 either the x-coordinate or the
        y-coordinate but not both). If all closer adjacent cells are
        occupied, no movement will occur. This should raise
        ValueError if this living entity or player is not on the board.
        """
        original_position = Game.GAME.get_position(self)
        if original_position is None:
            raise ValueError("Entity must be on the board to move")
        
        player_position = Game.GAME.get_position(player)
        if player_position is None:
            raise ValueError("Player must be on the board")
        
        # Try to move horizontally first
        if original_position.x > player_position.x:
            self.move_left()
        elif original_position.x < player_position.x:
            self.move_right()
        
        # If we didn't move horizontally, try vertically
        if original_position == Game.GAME.get_position(self):
            if original_position.y > player_position.y:
                self.move_up()
            elif original_position.y < player_position.y:
                self.move_down()