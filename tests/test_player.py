"""Tests for the player submodule."""

import pytest
from src.models.player import Player, Robot, PlayerSymbol
from src.models.board import Board

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

def test_robot_choose_move():
    """Test the automatic move selection by a robot."""
    robot = Robot()
    board = Board(robot, Player())
    move = robot.best_move(board)
    assert move in board.empty_square_coords
