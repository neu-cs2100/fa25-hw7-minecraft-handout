from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    """A board position."""
    x: int
    y: int