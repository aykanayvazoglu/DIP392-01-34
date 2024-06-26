import pytest
from OOP_Connect4 import Connect4Game

@pytest.fixture
def new_game():
    return Connect4Game()

def test_initialization(new_game):
    assert new_game.game_board.shape == (6, 7)
    assert (new_game.game_board == 6).all()
    assert new_game.turn == 0
    assert new_game.col_pressed == [0, 0, 0, 0, 0, 0, 0]
    print("test_initialization succeed")

def test_play_move(new_game):
    assert new_game.play_move(0) == True
    assert new_game.game_board[5][0] == 6
    assert new_game.turn == 1
    assert new_game.col_pressed[0] == 1
    print("test_play_move succeed")

def test_win_conditions(new_game):
    # horizontal win
    new_game.game_board[5][0] = 0
    new_game.game_board[5][1] = 0
    new_game.game_board[5][2] = 0
    new_game.game_board[5][3] = 0
    assert new_game.check_win() == (True, 0)
    print("test_win_conditions succeed (horizontal)")

    # vertical win
    new_game.reset()
    new_game.game_board[5][0] = 0
    new_game.game_board[4][0] = 0
    new_game.game_board[3][0] = 0
    new_game.game_board[2][0] = 0
    assert new_game.check_win() == (True, 0)
    print("test_win_conditions succeed (vertical)")

    # diagonal top-left to bottom-right
    new_game.reset()
    new_game.game_board[5][0] = 0
    new_game.game_board[4][1] = 0
    new_game.game_board[3][2] = 0
    new_game.game_board[2][3] = 0
    assert new_game.check_win() == (True, 0)
    print("test_win_conditions succeed (diagonal 1)")

    # diagonal bottom-left to top-right
    new_game.reset()
    new_game.game_board[2][0] = 0
    new_game.game_board[3][1] = 0
    new_game.game_board[4][2] = 0
    new_game.game_board[5][3] = 0
    assert new_game.check_win() == (True, 0)
    print("test_win_conditions succeed (diagonal 2)")

def test_check_all_move_played(new_game):
    for i in range(6):
        for j in range(7):
            new_game.game_board[i][j] = 0
    assert new_game.check_all_move_played() == True
    print("test_check_all_move_played succeed")

def test_invalid_move(new_game):
    for i in range(6):
        new_game.play_move(0)
    assert new_game.play_move(0) == False
    print("test_invalid_move succeed")

def test_restart(new_game):
    new_game.play_move(0)
    new_game.play_move(1)
    new_game.play_move(0)
    new_game.reset()
    assert (new_game.game_board == 6).all()
    assert new_game.turn == 0
    assert new_game.col_pressed == [0, 0, 0, 0, 0, 0, 0]
    print("test_restart succeed")
