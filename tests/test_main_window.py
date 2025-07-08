"""Tests for the main_window module."""

import pytest
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from src.gui.main_window import MainWindow
from src.models.player import Player
from src.models.board import Board

def setup_module():
    """Setup QApplication for all tests"""
    global app
    if not QApplication.instance():
        app = QApplication([])

def test_main_window_creation():
    """Test creating a main window."""
    window = MainWindow()
    assert window.windowTitle() == "Tic-Tac-Toe"
    assert window.board is None
    assert isinstance(window.playerX, Player)
    assert isinstance(window.playerO, Player)

def test_main_window_players():
    """Test switching between human and robot players."""
    window = MainWindow()
    
    assert not window.playerX.robot
    window._playerX_box.click()
    assert window.playerX.robot
    window._playerX_box.click()
    assert not window.playerX.robot

    assert not window.playerO.robot
    window._playerO_box.click()
    assert window.playerO.robot
    window._playerO_box.click()
    assert not window.playerO.robot

def test_main_window_play():
    """Test starting a game."""
    window = MainWindow()
    assert not window._play_button.isChecked()
    assert window._play_button.text() == "PLAY"
    assert window._playerX_box.isEnabled()
    assert window._playerO_box.isEnabled()
    assert not window.board
    assert window._board_layout.count() == 0
    
    QTest.mouseClick(window._play_button, Qt.LeftButton) # ty: ignore
    assert window._play_button.isChecked()
    assert window._play_button.text() == "RESET"
    assert not window._playerX_box.isEnabled()
    assert not window._playerO_box.isEnabled()
    assert window.board
    assert window._board_layout.count() == 9

    QTest.mouseClick(window._play_button, Qt.LeftButton) # ty: ignore
    assert not window._play_button.isChecked()
    assert window._play_button.text() == "PLAY"
    assert window._playerX_box.isEnabled()
    assert window._playerO_box.isEnabled()
    assert not window.board
    assert window._board_layout.count() == 0
