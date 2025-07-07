"""Tests for the square_button submodule."""

import pytest
from PyQt5.QtWidgets import QApplication
from src.gui.square_button import SquareButton
from src.models.square import Square, SquareState

def setup_module():
    """Setup QApplication for all tests"""
    global app
    if not QApplication.instance():
        app = QApplication([])

def test_square_button_creation():
    """Test the creation of a SquareButton."""
    square = Square()
    square_button = SquareButton(square, 0, 0)
    assert square_button.square == square

def test_square_button_state_change():
    """Test to make sure the buttons shows the state of the square."""
    square = Square()
    square_button = SquareButton(square, 0, 0)
    assert square_button.icon().isNull()
    assert square_button.isEnabled()
    square_button.square.mark_x()
    square_button.update_state()
    assert not square_button.icon().isNull()
    assert not square_button.isEnabled()
