from mob_base import Mob


class Skeleton(Mob):
    """
    A skeleton mob that uses a bow and arrow.
    
    Skeletons are ranged attackers with moderate health but high accuracy.
    They have special behavior when attacking at low health.
    """
    
    def __init__(self, max_health: int = 20, max_strength: int = 6) -> None:
        """
        Initialize a skeleton with default or custom stats.
        
        Args:
            max_health: The maximum health points (default: 20)
            max_strength: The maximum attack strength (default: 6)
        """
        # Call parent constructor with appropriate parameters
        # Hint: Use super() to call the parent constructor
        # Hint: Skeleton's name should be "skeleton" and weapon should be "bow"
        pass
    
    def attack(self, target: 'Mob') -> str:
        """
        Skeleton's special attack with ranged capabilities.
        
        Skeletons get a damage bonus when their health is low (below 25% of max).
        Low health skeletons deal +2 extra damage due to desperation.
        
        Args:
            target: The mob being attacked
            
        Returns:
            A string describing the attack outcome
        """
        # Check if skeleton is at low health (< 25% of max_health)
        # If low health, temporarily increase max_strength by 2
        # Call parent's attack method using super()
        # If damage was increased, restore original max_strength
        # Return the result from parent's attack method
        
        return # Make sure to return the actual string and remove this comment