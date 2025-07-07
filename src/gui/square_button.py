"""View/controller widget of an individual square."""

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from src.models.square import Square

ICONS = [
    QIcon(),
    QIcon('src/gui/cross_button.png'),
    QIcon('src/gui/tick_button.png')
]
"""Icons to display the state of a square. Indices match SquareState."""

class SquareButton(QPushButton):
    """View/controller widget of an individual square."""

    def __init__(self, square: Square):
        super().__init__()
        self.square = square
        self.update_state()
    
    def update_state(self):
        self.setIcon(ICONS[self.square.state])
