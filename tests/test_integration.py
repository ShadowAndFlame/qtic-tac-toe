"""Tests for gameplay."""

import pytest
from unittest.mock import patch
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from src.gui.main_window import MainWindow

def setup_module():
    """Setup QApplication for all tests"""
    global app
    if not QApplication.instance():
        app = QApplication([])

@patch('PyQt5.QtWidgets.QMessageBox.information')
def test_full_gameplay_pvp_x_winner(mock_infobox):
    """Test a game between two humans where player X wins."""
    window = MainWindow()
    QTest.mouseClick(window.play_button, Qt.LeftButton) # ty: ignore

    movelist = [
        (0,0),
        (2,2),
        (2,0),
        (1,0),
        (0,2),
        (1,1),
        (0,1),
    ]
    for row, col in movelist:
        square_button = window.board_layout.itemAtPosition(row, col).widget()
        QTest.mouseClick(square_button, Qt.LeftButton) # ty: ignore
    mock_infobox.assert_called_with(
        window,
        "Congratulations!",
        "Player X has won the game!"
    )
    assert not window.board

@patch('PyQt5.QtWidgets.QMessageBox.information')
def test_full_gameplay_pvp_o_winner(mock_infobox):
    """Test a game between two humans where player O wins."""
    window = MainWindow()
    QTest.mouseClick(window.play_button, Qt.LeftButton) # ty: ignore

    movelist = [
        (1,0),
        (1,1),
        (2,0),
        (0,0),
        (0,2),
        (2,2),
    ]
    for row, col in movelist:
        square_button = window.board_layout.itemAtPosition(row, col).widget()
        QTest.mouseClick(square_button, Qt.LeftButton) # ty: ignore
    mock_infobox.assert_called_with(
        window,
        "Congratulations!",
        "Player O has won the game!"
    )
    assert not window.board
