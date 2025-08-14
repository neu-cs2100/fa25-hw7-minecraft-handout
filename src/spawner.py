from typing import TypeVar, Generic, Callable
from entity import Entity

# Define a type variable bound to Entity
T = TypeVar('T', bound='Entity')

class Spawner(Entity, Generic[T]):
    """A spawner of any type of Entity."""
    
    def __init__(self, spawn_type: str, spawn: Callable[[], T]) -> None:
        super().__init__(
            type_name=f"{spawn_type} Spawner",
            image_file_name="SpawnerOnSand.png"
        )
        self._spawn_type: str = spawn_type
        self._spawn: Callable[[], T] = spawn
    
    def tick(self) -> None:
        """Spawner doesn't do anything on tick."""
        pass