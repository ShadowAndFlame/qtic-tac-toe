"""Tests for the board submodule."""

import pytest

from src.models.board import Board
from src.models.player import Player, PlayerSymbol
from src.models.square import SquareState

def test_board_creation():
    """Test creating a board."""
    playerX = Player()
    playerO = Player()
    board = Board(playerX, playerO)
    assert board.playerX == playerX
    assert board.playerX.symbol == PlayerSymbol.X
    assert board.playerO == playerO
    assert board.playerO.symbol == PlayerSymbol.O
    for row in range(3):
        for col in range(3):
            assert board.square(row, col).state == SquareState.Blank
