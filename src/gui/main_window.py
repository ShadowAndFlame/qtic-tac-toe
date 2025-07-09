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
    QMessageBox,
)
from src.gui.square_button import SquareButton
from src.models.board import Board
from src.models.player import Player, Robot

class MainWindow(QMainWindow):
    """Widget for the window where the game is played.
    
    Attributes:
        board (Board): The model for the board where the game is played.
        board_layout (QGridLayout): The layout containing SquareButtons.
        play_button (QPushButton): The button that begins/resets a game.
        playerX_box (QCheckBox): The checkbox determining if a human player goes first.
        playerO_box (QCheckBox): The checkbox determining if a human player goes second.
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
        self.playerX_box = QCheckBox()
        self.playerX_box.setChecked(True)
        options_layout.addWidget(self.playerX_box)

        self.play_button = QPushButton("PLAY")
        self.play_button.clicked.connect(self.play)
        self.play_button.setCheckable(True)
        options_layout.addWidget(self.play_button)

        options_layout.addWidget(QLabel("Player O:"))
        self.playerO_box = QCheckBox()
        self.playerO_box.setChecked(True)
        options_layout.addWidget(self.playerO_box)
        
        main_layout.addLayout(options_layout)

        self.board_layout = QGridLayout()
        main_layout.addLayout(self.board_layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
    
    def play(self, checked: bool) -> None:
        """Begin a game."""
        if checked:
            self.play_button.setText("RESET")
            self.board = Board(self.playerX, self.playerO)
            for row, row_squares in enumerate(self.board._squares):
                for col, square in enumerate(row_squares):
                    square_button = SquareButton(square, row, col)
                    square_button.clicked_coord.connect(self.take_turn)
                    self.board_layout.addWidget(square_button, row, col)
        else:
            self.clear_board()
            self.board = None
            self.play_button.setText("PLAY")
        self.playerX_box.setEnabled(not checked)
        self.playerO_box.setEnabled(not checked)
    
    def take_turn(self, row: int, col: int):
        """Take a turn at the specified coordinates"""
        self.board.mark(row, col)
        square_button: SquareButton = self.board_layout.itemAtPosition(row, col).widget()
        square_button.update_state()
        self.check_winner()
    
    def clear_board(self) -> None:
        """Delete all buttons in the board."""
        for i in reversed(range(self.board_layout.count())):
            self.board_layout.itemAt(i).widget().setParent(None)
    
    def check_winner(self) -> None:
        winner = self.board.winner
        if winner:
            winner_str = "Player X" if winner == self.playerX else "Player O"
            QMessageBox.information(self, "Congratulations!", f"{winner_str} has won the game!")
            self.play(False)

    @property
    def playerX(self) -> Player:
        """The player taking the first turn."""
        if self.playerX_box.isChecked():
            return self._humanX
        else:
            return self._robotX
    
    @property
    def playerO(self) -> Player:
        """The player taking the second turn."""
        if self.playerO_box.isChecked():
            return self._humanO
        else:
            return self._robotO
