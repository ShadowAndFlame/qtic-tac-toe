"""Tests for the board submodule."""

import pytest

from src.models.board import Board, MoveError
from src.models.player import Player, Robot, PlayerSymbol
from src.models.square import SquareState

def test_board_creation():
    """Test creating a board."""
    playerX = Player()
    playerO = Robot()
    board = Board(playerX, playerO)
    assert board.playerX == playerX
    assert board.playerX.symbol == PlayerSymbol.X
    assert board.playerO == playerO
    assert board.playerO.symbol == PlayerSymbol.O
    assert board.active_player == playerX
    for row in range(3):
        for col in range(3):
            assert board.square(row, col).state == SquareState.Blank

def test_board_rows():
    """Test the rows property."""
    board = Board(Player(), Player())
    rows_coords: list[list[tuple[int, int]]] = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
    ]
    rows = board.rows
    assert len(rows) == len(rows_coords)
    for row, row_coords in zip(rows, rows_coords):
        assert len(row) == len(row_coords)
        for square, coords in zip(row, row_coords):
            assert square is board.square(*coords) # ty: ignore

def test_board_columns():
    """Test the columns property."""
    board = Board(Player(), Player())
    columns_coords: list[list[tuple[int, int]]] = [
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
    ]
    columns = board.columns
    assert len(columns) == len(columns_coords)
    for column, column_coords in zip(columns, columns_coords):
        assert len(column) == len(column_coords)
        for square, coords in zip(column, column_coords):
            assert square is board.square(*coords) # ty: ignore

def test_board_diagonals():
    """Test the diagonals property."""
    board = Board(Player(), Player())
    diagonals_coords: list[list[tuple[int, int]]] = [
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)],
    ]
    diagonals = board.diagonals
    assert len(diagonals) == len(diagonals_coords)
    for diagonal, diagonal_coords in zip(diagonals, diagonals_coords):
        assert len(diagonal) == len(diagonal_coords)
        for square, coords in zip(diagonal, diagonal_coords):
            assert square is board.square(*coords) # ty: ignore

def test_board_squares_flat():
    """Test getting a flat list of squares."""
    board = Board(Player(), Player())
    flat_list = board.squares_flat
    assert len(flat_list) == 9

def test_make_move():
    """Test marking a square on a board."""
    board = Board(Player(), Player())
    board.mark(0,0)
    assert board.square(0,0).state == SquareState.X
    assert (0,0) not in board.empty_square_coords
    board.mark(0,1)
    assert board.square(0,1).state == SquareState.O
    assert (0,1) not in board.empty_square_coords
    board.mark(0,2)
    assert board.square(0,2).state == SquareState.X
    assert (0,2) not in board.empty_square_coords
    with pytest.raises(MoveError):
        board.mark(0,0)

def test_board_winner():
    """Test whether the board can identify a winner by board state."""
    winner = Player()
    board = Board(winner, Player())
    for row in range(3):
        assert not board.winner
        board.mark(row, 0)
        if row < 2:
            assert not board.winner
            board.mark(row, 1)
    assert board.winner == winner

def test_board_tie():
    """Test whether the board can identify a tie."""
    board = Board(Player(),Player())
    movelist = [
        (0,0),
        (1,1),
        (2,0),
        (1,0),
        (1,2),
        (0,1),
        (2,1),
        (2,2),
        (0,2),
    ]
    for row, col in movelist:
        assert not board.tie
        board.mark(row, col)
    assert board.tie
