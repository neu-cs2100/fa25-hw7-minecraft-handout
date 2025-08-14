import random
import math
from typing import Optional, List, Dict, Any

from entity import Entity
from block import Block
from position import Position
from main import NUM_COLS, NUM_ROWS, NUM_TEXT_LINES


class Game:
    """
    A singleton class encapsulating the game state.
    """

    GAME: Optional["Game"] = None
    
    def __init__(self) -> None:
        if Game.GAME is not None:
            raise RuntimeError("There can only be one Game instance.")

        from sand import Sand
        from player import Player
        from spider import Spider
        from sheep import Sheep
        from chicken import Chicken

        # Initialize block grid with Sand blocks
        self._block_grid: List[List[Block]] = [
            [Sand() for _ in range(NUM_ROWS)] 
            for _ in range(NUM_COLS)
        ]
        
        # Initialize entity grid with None values
        self._entity_grid: List[List[Optional[Entity]]] = [
            [None for _ in range(NUM_ROWS)] 
            for _ in range(NUM_COLS)
        ]
        
        # The player of the game
        self.player = Player()
        
        # Text storage for bottom panel
        self._text: List[str] = []
        
        # Position tracking for entities
        self._positions: Dict[Entity, Position] = {}
        
        # Initialize entities
        self.place_at_random(self.player)
        self.place_at_random(Spider())
        self.place_at_random(Sheep())
        self.place_at_random(Chicken())

        Game.GAME = self
    
    @property
    def text_to_print(self) -> List[str]:
        """Text to print at the bottom of the game screen."""
        return self._text.copy()  # Return a copy to prevent external modification
    
    @property
    def placed_entities(self) -> List[Entity]:
        """All entities that have been placed on the grid."""
        return list(self._positions.keys())
    
    def add_text(self, string: str) -> None:
        """Adds string to appear in the panel at the bottom of the game window."""
        self._text.append(string)
        print(string)  # Also display in console
        if len(self._text) > NUM_TEXT_LINES:
            self._text.pop(0)
    
    def clear_text(self) -> None:
        """Clears the text in the panel at the bottom of the game window."""
        self._text.clear()
    
    def is_in_bounds(self, x: int, y: int) -> bool:
        """Tests whether the given x and y coordinates are in bounds."""
        return 0 <= x and x < NUM_COLS and 0 <= y and y < NUM_ROWS
    
    def is_occupied(self, x: int, y: int) -> bool:
        """
        Returns whether the cell with the specified x and y coordinates is
        occupied by an Entity in the game. It is illegal to try to move
        another Entity into an occupied cell. This returns False if
        the coordinates are out of bounds.
        """
        return self.is_in_bounds(x, y) and self._entity_grid[x][y] is not None
    
    def is_empty(self, x: int, y: int) -> bool:
        """
        Returns whether the cell with the specified x and y coordinates is
        unoccupied. See is_occupied. This returns False if the coordinates
        are out of bounds.
        """
        return self.is_in_bounds(x, y) and not self.is_occupied(x, y)
    
    def place(self, entity: Entity, x: int, y: int) -> None:
        """
        Places the entity at the specified x and y coordinates, raising ValueError
        if that position is_occupied or out of bounds.
        """
        if not self.is_empty(x, y):
            existing_entity = self.get_entity(x, y)
            raise ValueError(
                f"You cannot place the {entity} at ({x}, {y}), "
                f"which is already occupied by a {existing_entity}."
            )
        
        if not self.is_in_bounds(x, y):
            raise ValueError(f"The location ({x}, {y}) is out of bounds.")
        
        # Remove entity from previous position if it exists
        if entity in self._positions:
            self.remove(entity)
        
        self._entity_grid[x][y] = entity
        self._positions[entity] = Position(x, y)
    
    def place_at_random(self, entity: Entity) -> None:
        """Places the entity at a random position that is_empty."""
        while True:
            x = random.randint(0, NUM_COLS - 1)
            y = random.randint(0, NUM_ROWS - 1)
            if not self.is_occupied(x, y):
                self.place(entity, x, y)
                break
    
    def remove(self, entity: Entity) -> None:
        """
        Removes the entity from the game, so it no longer appears on
        the grid and its tick method is no longer called.
        This raises ValueError if it had not been on the grid.
        """
        if entity not in self._positions:
            raise ValueError(f"The {entity} was not on the grid.")
        
        position = self._positions[entity]
        self._entity_grid[position.x][position.y] = None
        del self._positions[entity]
    
    def get_entity(self, x: int, y: int) -> Optional[Entity]:
        """
        Gets whatever entity is at the specified x and y coordinates,
        or None if it is unoccupied or the position is out of bounds.
        """
        if self.is_in_bounds(x, y):
            return self._entity_grid[x][y]
        return None
    
    def get_block(self, x: int, y: int) -> Optional[Block]:
        """
        Gets whatever block is at the specified x and y coordinates
        or None if the position is out of bounds.
        """
        if self.is_in_bounds(x, y):
            return self._block_grid[x][y]
        return None
    
    def get_image(self, x: int, y: int) -> Optional[Any]:
        """
        Gets the image at the specified x and y coordinates or
        None if the position is out of bounds.
        """
        if not self.is_in_bounds(x, y):
            return None
        
        entity = self._entity_grid[x][y]
        if entity is not None:
            return entity.image
        
        return self._block_grid[x][y].image
    
    def calculate_distance(self, entity1: Entity, entity2: Entity) -> float:
        """
        Calculates the Euclidean distance between entity1 and entity2,
        raising ValueError if either has not been placed.
        """
        position1 = self.get_position(entity1)
        position2 = self.get_position(entity2)
        
        if position1 is None or position2 is None:
            raise ValueError("Both entities must be placed on the grid")
        
        distance = math.sqrt(
            (position1.x - position2.x) ** 2 + 
            (position1.y - position2.y) ** 2
        )
        return distance
    
    def get_position(self, entity: Entity) -> Optional[Position]:
        """
        Returns the position of the given entity, or None if it has
        not been placed.
        """
        return self._positions.get(entity)
    
    def tick(self) -> None:
        """
        Calls the tick method of all entities on the board,
        starting with the Player.
        """
        from player import Player
        self.player.tick()
        for entity in self.placed_entities:
            if not isinstance(entity, Player) and self.player.is_alive:
                entity.tick()