"""Model for an individual square on the board."""

from enum import IntEnum

class SquareState(IntEnum):
    Blank = 0
    X = 1
    O = 2

class SquareStateError(ValueError):
    pass

class Square:
    """Model for an individual square on the board."""

    def __init__(self, state: SquareState = SquareState.Blank) -> None:
        """Initialize the Square object.

        Args:
            state (SquareState): 
        """
        self._state = state

    @property
    def state(self) -> SquareState:
        """Whether the square contains an X, an O, or is empty.
        
        State cannot be changed once marked."""
        return self._state
    
    @state.setter
    def state(self, state: SquareState) -> None:
        if self.state != SquareState.Blank and self.state != state:
            raise SquareStateError("Cannot overwrite marked square.")
        self._state = state
