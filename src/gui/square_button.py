"""View/controller widget of an individual square."""

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal
from src.models.square import Square

ICONS = [
    QIcon(),
    QIcon('src/gui/cross_button.png'),
    QIcon('src/gui/tick_button.png')
]
"""Icons to display the state of a square. Indices match SquareState."""

class SquareButton(QPushButton):
    """View/controller widget of an individual square."""

    clicked_coord = pyqtSignal(int, int)
    """Emitted when clicked, carries coordinates of self on the board."""

    def __init__(self, square: Square, row: int, col: int):
        """Initialize the SqaureButton widget.
        
        Args:
            square (Square): The model for the square.
            row (int): The row of the square on the board.
            col (int): The column of the square on the board.
        """
        super().__init__()
        self.square = square
        self.update_state()
        self.clicked.connect(lambda: self.clicked_coord.emit(row, col))
    
    def update_state(self):
        """Match state with that of the model."""
        self.setIcon(ICONS[self.square.state])
        self.blockSignals(self.square.state)
