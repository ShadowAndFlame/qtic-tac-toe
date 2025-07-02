"""Model for the board state."""

from src.models.player import Player, PlayerSymbol
from src.models.square import Square

class Board:
    """Model for the board state.
    
    The Board contains nine Squares in a 3x3 grid. Win condition is
    getting three in a row horizontally, vertically, or diagonally.
    """

    def __init__(self, playerX: Player, playerO: Player) -> None:
        """Initialize the Board object. Supplied players must be a
        
        Args:
            playerX (Player): The player who goes first.
            playerO (Player): The player who goes second.
        """
        self.playerX = playerX
        self.playerO = playerO
    
        self._squares = [[Square() for _ in range(3)] for _ in range(3)]
    
    def square(self, row: int, col: int) -> Square:
        """The Square object in the row and column specified.
        
        Args:
            row (int): The row from which to retrieve the square.
            col (int): The column from which to retrieve the square.
        """
        return self._squares[row][col]
