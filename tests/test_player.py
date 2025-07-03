"""Tests for the player submodule."""

import pytest
from src.models.player import Player, Robot, PlayerSymbol

def test_player_creation():
    """Test the creation of a player."""
    player = Player()
    assert player.symbol == None
    assert player.robot == False

def test_robot_creation():
    """Test the creation of a robot."""
    player = Robot()
    assert player.symbol == None
    assert player.robot == True

def test_player_symbol_assignment():
    """Test assigning a symbol to a player."""
    player = Player()
    player.symbol = PlayerSymbol.X
    assert player.symbol == PlayerSymbol.X

def test_player_invalid_assignments():
    """Test illegally assigning attributes to a player."""
    player = Player()
    player.symbol = PlayerSymbol.X
    with pytest.raises(AttributeError):
        player.symbol = PlayerSymbol.O
        player.robot = True # ty: ignore
