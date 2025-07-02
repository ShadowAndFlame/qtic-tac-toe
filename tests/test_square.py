"""Tests for the square submodule."""

import pytest
from src.models.square import Square, SquareState, SquareStateError

def test_square_creation():
    """Test creating a square."""
    square = Square()
    assert square.state == SquareState.Blank
    assert square.marked == False
    with pytest.raises(AttributeError):
        square.marked = True # ty: ignore

def test_mark_square_x():
    """Test setting a square to the X state."""
    square = Square()
    square.state = SquareState.X
    assert square.state == SquareState.X
    assert square.marked == True

    square_alt = Square()
    square_alt.mark_x()
    assert square.state == SquareState.X
    assert square.marked == True

def test_mark_square_o():
    """Test setting a square to the O state."""
    square = Square()
    square.state = SquareState.O
    assert square.state == SquareState.O
    assert square.marked == True

    square_alt = Square()
    square_alt.mark_o()
    assert square.state == SquareState.O
    assert square.marked == True

def test_remark_marked_square():
    """Test setting a marked square (forbidden if different)."""
    square = Square()
    square.state = SquareState.Blank
    square.state = SquareState.X
    square.state = SquareState.X
    with pytest.raises(SquareStateError):
        square.state = SquareState.O
    
    square_alt = Square()
    square_alt.mark_o()
    square_alt.mark_o()
    with pytest.raises(SquareStateError):
        square_alt.mark_x()
