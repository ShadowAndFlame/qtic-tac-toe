"""Tests for the square submodule."""

import pytest
from src.models.square import Square, SquareState

def test_square_creation():
    """Test creating a square."""
    square = Square()
    assert square.state == SquareState.Blank

def test_mark_square_x():
    """Test setting a square to the X state"""
    square = Square()
    square.state = SquareState.X
    assert square.state == SquareState.X

def test_mark_square_o():
    """Test setting a square to the O state"""
    square = Square()
    square.state = SquareState.O
    assert square.state == SquareState.O
