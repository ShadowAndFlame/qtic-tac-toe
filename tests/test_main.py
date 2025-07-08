"""Tests for the main script."""

import pytest
from unittest.mock import patch, MagicMock
from main import main

def test_main_function():
    """Test the application launch script."""
    with patch('main.QApplication') as mock_app_class, \
         patch('main.MainWindow') as mock_window_class:
        
        mock_app = MagicMock()
        mock_app_class.return_value = mock_app
        mock_window = MagicMock()
        mock_window_class.return_value = mock_window

        main()

        mock_app_class.assert_called_once()
        mock_window_class.assert_called_once()
        mock_window.show.assert_called_once()
        mock_app.exec.assert_called_once()
