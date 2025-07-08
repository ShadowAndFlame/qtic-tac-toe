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
