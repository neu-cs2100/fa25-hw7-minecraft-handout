from abc import ABC, abstractmethod
from typing import Any, Optional

from position import Position

class Entity(ABC):
    """
    An animate or inanimate object in the game.
    
    Args:
        type_name: The type/name of the entity
        image_file_name: The filename of the image to load
    """
    
    def __init__(self, type_name: str, image_file_name: str) -> None:
        self.type: str = type_name
        # Load image - using Any type since we don't know the exact image library type
        self.image: Any = self._load_image(f"data/images/{image_file_name}")
    
    def _load_image(self, path: str) -> Any:
        """
        Load an image from the given path.
        This would need to be implemented based on your graphics library.
        For example, using PIL: from PIL import Image; return Image.open(path)
        """
        # Placeholder implementation - replace with actual image loading
        # Examples for different libraries:
        # PIL: return Image.open(path)
        # pygame: return pygame.image.load(path)
        # tkinter: return PhotoImage(file=path)
        try:
            # This is a placeholder - implement based on your graphics library
            return path  # Temporary placeholder
        except Exception as e:
            raise FileNotFoundError(f"Could not load image: {path}") from e
    
    @abstractmethod
    def tick(self) -> None:
        """Takes an action during its turn."""
        pass
    
    def exit(self) -> None:
        """
        Removes this entity from the game. It will no longer appear
        on the screen, and its tick method will no longer be called.
        """
        from game import Game  # Import here to avoid circular imports
        Game.GAME.remove(self)
    
    def __str__(self) -> str:
        """String representation of the entity."""
        return self.type
    
    def select_adjacent_empty_cell(self) -> Optional[Position]:
        """
        Returns the position of an empty cell adjacent to this entity or
        None if no adjacent empty cell exists or if this entity is not on
        the board.
        """
        from game import Game
        position = Game.GAME.get_position(self)
        return None
    