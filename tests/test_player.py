"""Tests for the player submodule."""

import pytest
from src.models.player import Player, Robot, PlayerSymbol

def test_player_creation():
    """Test the creation of a player."""
    player = Player(PlayerSymbol.X)
    assert player.symbol == PlayerSymbol.X
    assert player.robot == False
    with pytest.raises(AttributeError):
        player.symbol = PlayerSymbol.O # ty: ignore
        player.robot = True # ty: ignore

def test_robot_creation():
    """Test the creation of a robot."""
    robot = Robot(PlayerSymbol.O)
    assert robot.symbol == PlayerSymbol.O
    assert robot.robot == True
    with pytest.raises(AttributeError):
        robot.symbol = PlayerSymbol.X # ty: ignore
        robot.robot = False # ty: ignore
