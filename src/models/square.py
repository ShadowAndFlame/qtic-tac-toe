"""Model for an individual square on the board."""

from enum import IntEnum

class SquareState(IntEnum):
    Blank = 0
    X = 1
    O = 2

class Square:
    """Model for an individual square on the board.
    
    Attributes:
        state (SquareState): Whether the square contains an X, an O, or is empty.
    """

    def __init__(self, state: SquareState = SquareState.Blank) -> None:
        """Initialize the Square object.

        Args:
            state (SquareState): Whether the square contains an X, an O, or is empty.
        """
        self.state = state
