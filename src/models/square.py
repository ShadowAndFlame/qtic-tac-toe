"""Model for an individual square on the board."""

from enum import IntEnum

class SquareState(IntEnum):
    """Namespace for state of Square."""
    Blank = 0
    X = 1
    O = 2

class Square:
    """Model for an individual square on the board."""

    def __init__(self, state: SquareState = SquareState.Blank) -> None:
        """Initialize the Square object.

        Args:
            state (SquareState): Whether the initialized Square should contain an X, an O, or be empty.
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
            raise AttributeError("Cannot overwrite marked square.")
        self._state = state

    @property
    def marked(self) -> bool:
        """Whether the state has been changed from Blank."""
        return self.state != SquareState.Blank

    def mark_x(self) -> None:
        """Set state to X."""
        self.state = SquareState.X
    
    def mark_o(self) -> None:
        """Set state to O."""
        self.state = SquareState.O
