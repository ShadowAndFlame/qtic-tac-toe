"""Widget for the window where the game is played."""

from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QCheckBox,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QWidget,
    QApplication
)
from src.gui.square_button import SquareButton
from src.models.board import Board
from src.models.player import Player, Robot

class MainWindow(QMainWindow):
    """Widget for the window where the game is played.
    
    Attributes:
        board (Board): The model for the board where the game is played.
    """

    def __init__(self):
        """Initialize the MainWindow object."""
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")

        self.board = None
        self._humanX = Player()
        self._robotX = Robot()
        self._humanO = Player()
        self._robotO = Robot()

        main_layout = QVBoxLayout()

        options_layout = QHBoxLayout()

        options_layout.addWidget(QLabel("Player X:"))
        self._playerX_box = QCheckBox()
        self._playerX_box.setChecked(True)
        options_layout.addWidget(self._playerX_box)

        self._play_button = QPushButton("PLAY")
        self._play_button.clicked.connect(self.play)
        options_layout.addWidget(self._play_button)

        options_layout.addWidget(QLabel("Player O:"))
        self._playerO_box = QCheckBox()
        self._playerO_box.setChecked(True)
        options_layout.addWidget(self._playerO_box)
        
        main_layout.addLayout(options_layout)

        self._board_layout = QGridLayout()
        main_layout.addLayout(self._board_layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
    
    def play(self) -> None:
        """Begin a game."""
        self.clear_board()
        self.board = Board(self.playerX, self.playerO)
        for row, row_squares in enumerate(self.board._squares):
            for col, square in enumerate(row_squares):
                square_button = SquareButton(square, row, col)
                self._board_layout.addWidget(square_button, row, col)
    
    def clear_board(self) -> None:
        """Delete all buttons in the board."""
        for i in reversed(range(self._board_layout.count())):
            self._board_layout.itemAt(i).widget().setParent(None)

    @property
    def playerX(self) -> Player:
        """The player taking the first turn."""
        if self._playerX_box.isChecked():
            return self._humanX
        else:
            return self._robotX
    
    @property
    def playerO(self) -> Player:
        """The player taking the second turn."""
        if self._playerO_box.isChecked():
            return self._humanO
        else:
            return self._robotO
