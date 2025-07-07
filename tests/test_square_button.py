"""Tests for the square_button submodule."""

import pytest
from PyQt5.QtWidgets import QApplication
from src.gui.square_button import SquareButton
from src.models.square import Square

def setup_module():
    """Setup QApplication for all tests"""
    global app
    if not QApplication.instance():
        app = QApplication([])

def test_square_button_creation():
    """Test the creation of a SquareButton."""
    square = Square()
    square_button = SquareButton(square)
    assert square_button.square == square

