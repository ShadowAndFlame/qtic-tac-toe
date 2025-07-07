"""Model for the board state."""

from src.models.player import Player, PlayerSymbol
from src.models.square import Square, SquareState

class MoveError(ValueError):
    """Error related to making a move"""
    pass

class Board:
    """Model for the board state.
    
    The Board contains nine Squares in a 3x3 grid. Win condition is
    getting three in a row horizontally, vertically, or diagonally.

    Attributes:
        playerX (Player): The player who goes first.
        playerO (Player): The player who goes second.
        active_player (Player): The player whose turn is next.
    """

    def __init__(self, playerX: Player, playerO: Player) -> None:
        """Initialize the Board object. Supplied players must be a
        
        Args:
            playerX (Player): The player who goes first.
            playerO (Player): The player who goes second.
        """
        self.playerX = playerX
        self.playerX.symbol = PlayerSymbol.X
        self.playerO = playerO
        self.playerO.symbol = PlayerSymbol.O

        self.active_player = self.playerX
    
        self._squares: list[list[Square]] = [[Square() for _ in range(3)] for _ in range(3)]
    
    def square(self, row: int, col: int) -> Square:
        """The Square object in the row and column specified.
        
        Args:
            row (int): The row from which to retrieve the square.
            col (int): The column from which to retrieve the square.
        """
        return self._squares[row][col]

    def mark(self, row: int, col: int) -> None:
        """Active player makes a move in the specified coordinates, turn passes.
        
        Args:
            row (int): The row from which to retrieve the square.
            col (int): The column from which to retrieve the square.
        """
        try:
            self.square(row, col).state = self.active_player.symbol
        except AttributeError:
            raise MoveError("That square is already marked.")
        self.active_player = self.playerX if self.active_player == self.playerO else self.playerO

    @staticmethod
    def three_alike(squares: list[Square]) -> SquareState | None:
        for square in squares:
            if square.state != squares[0].state or square.state == SquareState.Blank:
                return None
        return squares[0].state
    
    @property
    def rows(self) -> list[list[Square]]:
        """The rows of the board, 3 rows of 3 squares."""
        return self._squares
    
    @property
    def columns(self) -> list[list[Square]]:
        """The columns of the board, 3 columns of 3 squares."""
        return [list(l) for l in zip(*self._squares)]
    
    @property
    def diagonals(self) -> list[list[Square]]:
        """The diagonals of the board, 2 diagonals of 3 squares."""
        n = len(self._squares)
        diagonals = [
            [self._squares[i][i] for i in range(n)],
            [self._squares[i][n-i-1] for i in range(n)],
        ]
        return diagonals

    @property
    def winner(self) -> Player | None:
        sets: list[list[Square]] = self._squares
        sets = sets + [list(*l) for l in zip(self._squares)]
        n = len(self._squares)
        sets.append([self._squares[i][i] for i in range(n)])
        sets.append([self._squares[i][n-i-1] for i in range(n)])

        winners = [self.three_alike(set_) for set_ in sets]
        if not any(winners):
            return None
        winners = [winner for winner in winners if winner]
        if len(winners > 1):
            raise MoveError("Something went wrong; there are multiple winners.")
        winning_symbol = winners[0]
        if winning_symbol == SquareState.X:
            return self.playerX
        else:
            return self.playerO
