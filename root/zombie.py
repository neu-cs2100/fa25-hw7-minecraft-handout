class Zombie(Mob):
    """
    A zombie mob that uses claws and teeth.
    
    Zombies are melee attackers with high health but lower accuracy.
    They have special regeneration abilities when injured.
    """
    
    def __init__(self, max_health: int = 30, max_strength: int = 4) -> None:
        """
        Initialize a zombie with default or custom stats.
        
        Args:
            max_health: The maximum health points 
            max_strength: The maximum attack strength
        """
        # Call parent constructor with appropriate parameters
        # Hint: Use super() to call the parent constructor
        # Hint: Zombie's name should be "zombie" and weapon should be "claws"
        pass
    
    def take_damage(self, damage: int) -> None:
        """
        Zombie's special damage handling with regeneration.
        
        Zombies have a chance to regenerate 1 health point after taking damage,
        but only if they're still alive and not at maximum health.
        
        Regeneration occurs if the damage taken is odd (damage % 2 == 1).
        
        Args:
            damage: The number of damage points to apply
        """
        # Call parent's take_damage method using super()
        # Check if zombie is still alive after taking damage
        # Check if damage was odd (damage % 2 == 1)
        # Check if zombie is not at maximum health
        # If all conditions met, heal 1 health point
        # Make sure health doesn't exceed max_health
        pass
    
    def __str__(self) -> str:
        """
        Return a string representation of this zombie.
        
        Zombies have a special string format that includes their regeneration status.
        If zombie is injured but not dead, add " (regenerating)" to the status.
        
        Returns:
            A string like "injured zombie (regenerating)" or "healthy zombie"
        """
        return # Make sure to return the actual string and remove this comment