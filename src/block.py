from abc import ABC
from entity import Entity

class Block(Entity, ABC):
    """An inanimate object in the game, such as Sand."""
    
    def __init__(self, type_name: str, image_file_name: str) -> None:
        super().__init__(type_name, image_file_name)
    
    def tick(self) -> None:
        """Blocks don't do anything."""
        pass
