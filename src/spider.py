from mob import Mob, Behavior


class Spider(Mob):
    """A spider, a hostile Mob."""
    
    def __init__(self) -> None:
        super().__init__(
            type_name="Spider",
            max_hearts=20,
            behavior=Behavior.HOSTILE,
            attack_strength=3,
            image_file_name="Spider.png",
            sound_file_name="spider.mp3",
            subtitle="Spider hisses"
        )