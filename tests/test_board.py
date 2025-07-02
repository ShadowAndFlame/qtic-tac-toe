"""Tests for the board submodule."""

import pytest

from src.models.board import Board
from src.models.player import Player, PlayerSymbol
from src.models.square import SquareState

def test_board_creation():
    """Test creating a board."""
    playerX = Player(PlayerSymbol.X)
    playerO = Player(PlayerSymbol.O)
    board = Board(playerX, playerO)
    assert board.playerX == playerX
    assert board.playerO == playerO
    for row in range(3):
        for col in range(3):
            assert board.square(row, col).state == SquareState.Blank
