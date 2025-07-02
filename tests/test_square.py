"""Tests for the square submodule."""

import pytest
from src.models.square import Square, SquareState

def test_square_creation():
    """Test creating a square."""
    square = Square()
    assert square.state == SquareState.Blank
