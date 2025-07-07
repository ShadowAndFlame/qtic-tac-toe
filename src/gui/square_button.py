"""View/controller widget of an individual square."""

from PyQt5.QtWidgets import QPushButton
from src.models.square import Square

class SquareButton(QPushButton):
    """View/controller widget of an individual square."""
    
    def __init__(self, square: Square):
        super().__init__()
        self.square = square
