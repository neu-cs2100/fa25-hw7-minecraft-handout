from mob import Mob, Behavior

class Chicken(Mob):
    """A chicken, a passive Mob."""
    
    def __init__(self) -> None:
        super().__init__(
            type_name="Chicken",
            max_hearts=5,
            behavior=Behavior.PASSIVE,
            attack_strength=0,
            image_file_name="ChickenOnSand.png",
            sound_file_name="Chicken.mp3",
            subtitle="Chicken clucks"
        )