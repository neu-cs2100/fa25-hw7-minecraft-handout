from mob import Mob, Behavior

class Sheep(Mob):
    """A sheep, a passive Mob."""
    
    def __init__(self) -> None:
        super().__init__(
            type_name="Sheep",
            max_hearts=8,
            behavior=Behavior.PASSIVE,
            attack_strength=0,
            image_file_name="Sheep.png",
            sound_file_name="sheep.mp3",
            subtitle="Sheep baahs"
        )