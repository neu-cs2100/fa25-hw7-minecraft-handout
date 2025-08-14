from mob import Mob, Behavior

class Zombie(Mob):
    """A zombie, a hostile Mob."""
    
    def __init__(self) -> None:
        super().__init__(
            type_name="Zombie",
            max_hearts=20,
            behavior=Behavior.HOSTILE,
            attack_strength=5,
            image_file_name="Zombie.png",
            sound_file_name="zombie.mp3",
            subtitle="Zombie groans"
        )