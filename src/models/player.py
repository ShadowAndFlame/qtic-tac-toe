"""Model for a player, whether human or computer."""

from enum import IntEnum

class PlayerSymbol(IntEnum):
    """The symbol the player marks on the board.
    
    Evaluations match those of Square states."""
    X = 1
    O = 2

class Player:
    """A player can make moves on the board."""

    def __init__(self, symbol: PlayerSymbol) -> None:
        """Initialize the Player object.
        
        Args:
            symbol (PlayerSymbol): The symbol the player will mark on the board.
        """
        self._symbol = symbol
        self._robot = False

    @property
    def symbol(self) -> PlayerSymbol:
        """The symbol the player will mark on the board."""
        return self._symbol
    
    @property
    def robot(self) -> bool:
        """Whether the player is computer controlled."""
        return self._robot

class Robot(Player):
    """A special player that makes moves without GUI interaction."""
    def __init__(self, symbol: PlayerSymbol):
        super().__init__(symbol)
        self._robot = True
