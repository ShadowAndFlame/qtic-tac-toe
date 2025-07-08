"""View/controller widget of an individual square."""

from PyQt5.QtWidgets import QPushButton, QStyle
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal, QObject, QEvent
from src.models.square import Square

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
        
        self.icons = [
            QIcon(),
            self.style().standardIcon(QStyle.SP_DialogCancelButton), # ty: ignore
            self.style().standardIcon(QStyle.SP_DialogNoButton), # ty: ignore
        ]
        
        self.square = square
        self.update_state()
        self.clicked.connect(lambda: self.clicked_coord.emit(row, col))
        self.setFixedHeight(60)
        self.setFixedWidth(60)
    
    def update_state(self):
        """Match state with that of the model."""
        self.setIcon(self.icons[self.square.state])
        self.blockSignals(self.square.state)
