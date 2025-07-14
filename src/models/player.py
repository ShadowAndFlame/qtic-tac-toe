"""Model for a player, whether human or computer."""

from enum import IntEnum
from src.models import board

class PlayerSymbol(IntEnum):
    """The symbol the player marks on the board.
    
    Evaluations match those of Square states."""
    X = 1
    O = 2

class Player:
    """A player can make moves on the board."""

    def __init__(self) -> None:
        """Initialize the Player object.
        
        Args:
            symbol (PlayerSymbol): The symbol the player will mark on the board.
        """
        self.symbol = None
        self.robot = False

class Robot(Player):
    """A special player that makes moves without GUI interaction."""
    def __init__(self):
        super().__init__()
        self.robot = True

    def best_move(self, board: 'board.Board') -> tuple[int, int]:
        """Choose the best move to make given the board state.
        
        Args:
            board (Board): The current board state. Need not include self.

        Returns:
            tuple[int, int]: The row and column to make a move in."""
        possible_moves = board.empty_square_coords
        return possible_moves[0]
