#!/usr/bin/python3
# -*- coding: utf-8 -*-

# do NOT change the next two lines of code...
import sys

assert (
    "linux" in sys.platform
), "This code should be run on Linux, just a reminder to follow instructions..."
import random
from typing import List, Tuple


def draw_board(
    board: List[List[str]], number_of_rows: int, number_of_cols: int
) -> None:
    """Print out updated board."""
    top: str = " "
    for i in range(number_of_cols):
        top = top + " {}".format(i)
    print(top)
    for i in range(number_of_rows):
        print(i, end="")
        for j in range(number_of_cols):
            print("|{}".format(board[i][j]), end="")
        print("|")


def input_player_letter() -> List[str]:
    """
    Determine what letter the player and the computer is.

    Returns a list of [X, O] or [O, X]. First letter in the list is the player.
    """
    player_letter = ""

    while player_letter not in ["X", "O"]:
        player_letter = input("\nDo you want to be X or O?").upper()

    if player_letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]


def who_goes_first() -> str:
    """Randomly return who goes first in a game."""
    random.seed(0)
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "human player"


def make_move(board: List[List[str]], letter: str, row: int, col: int) -> None:
    """Super simple. Replace [row][col] of the board with the letter."""
    board[row][col] = letter


def check_across(
    board: List[List[str]],
    letter: str,
    number_of_rows: int,
    number_of_cols: int,
    number_of_matches: int,
    i: int,
    j: int,
) -> bool:
    """
    Parameters.

    ----------
    board : List[List[str]]
        Current copy of the board
    letter : str
        Either the computer letter or the player letter
    number_of_rows : int
        Number of rows in the board
    number_of_cols : int
        Number of columns in the board
    number_of_matches : int
        How many letters have to be in a row to win
    i : int
        Current row isWinner is checking
    j : int
        Current column isWinner is checking

    Returns
    -------
    bool
        Determines if each space in the board k spaces away to the right from
        the current position contains the checked letter. If so, return True.
    """
    for k in range(number_of_matches):
        try:
            if board[i][j + k] != letter:
                return False
        except IndexError:
            return False
    return True


def check_down(
    board: List[List[str]],
    letter: str,
    number_of_rows: int,
    number_of_cols: int,
    number_of_matches: int,
    i: int,
    j: int,
) -> bool:
    """
    Parameters.

    ----------
    board : List[List[str]]
        Current copy of the board
    letter : str
        Either the computer letter or the player letter
    number_of_rows : int
        Number of rows in the board
    number_of_cols : int
        Number of columns in the board
    number_of_matches : int
        How many letters have to be in a row to win
    i : int
        Current row isWinner is checking
    j : int
        Current column isWinner is checking

    Returns
    -------
    bool
        Determines if each space in the board k spaces away downward from
        the current position contains the checked letter. If so, return True.
    """
    for k in range(number_of_matches):
        try:
            if board[i + k][j] != letter:
                return False
        except IndexError:
            return False
    return True


def check_diagonal_right(
    board: List[List[str]],
    letter: str,
    number_of_rows: int,
    number_of_cols: int,
    number_of_matches: int,
    i: int,
    j: int,
) -> bool:
    """
    Parameters.

    ----------
    board : List[List[str]]
        Current copy of the board
    letter : str
        Either the computer letter or the player letter
    number_of_rows : int
        Number of rows in the board
    number_of_cols : int
        Number of columns in the board
    number_of_matches : int
        How many letters have to be in a row to win
    i : int
        Current row isWinner is checking
    j : int
        Current column isWinner is checking

    Returns
    -------
    bool
        Determines if each space in the board k spaces away to the right and k
        spaces up from the current position contains the checked letter.
        If so, return True.
    """
    for k in range(number_of_matches):
        try:
            if board[i + k][j + k] != letter:
                return False
        except IndexError:
            return False
    return True


def check_diagonal_left(
    board: List[List[str]],
    letter: str,
    number_of_rows: int,
    number_of_cols: int,
    number_of_matches: int,
    i: int,
    j: int,
) -> bool:
    """
    Parameters.

    ----------
    board : List[List[str]]
        Current copy of the board
    letter : str
        Either the computer letter or the player letter
    number_of_rows : int
        Number of rows in the board
    number_of_cols : int
        Number of columns in the board
    number_of_matches : int
        How many letters have to be in a row to win
    i : int
        Current row isWinner is checking
    j : int
        Current column isWinner is checking

    Returns
    -------
    bool
        Determines if each space in the board k spaces away to the left and
        upwards fromthe current position contains the checked letter.
        If so, return True.
    """
    for k in range(number_of_matches):
        try:
            if board[i + k][j - k] != letter:
                return False
        except IndexError:
            return False
    return True


def is_winner(
    board: List[List[str]],
    letter: str,
    number_of_rows: int,
    number_of_cols: int,
    number_of_matches: int,
) -> bool:
    """
    Parameters.

    ----------
    board : List[List[str]]
        Current copy of the board
    letter : str
        Either the computer letter or the player letter
    number_of_rows : int
        Number of rows in the board
    number_of_cols : int
        Number of columns in the board
    number_of_matches : int
        How many letters have to be in a row to win
    i : int
        Current row isWinner is checking
    j : int
        Current column isWinner is checking

    Returns
    -------
    bool
        Determines if either the player or computer wins based on which letter
        is inputed. It used each check to determine if there are k spaces of
        either letter in a row.
    """
    for i in range(number_of_rows):
        for j in range(number_of_cols):
            if board[i][j] == letter:
                if check_across(
                    board,
                    letter,
                    number_of_rows,
                    number_of_cols,
                    number_of_matches,
                    i,
                    j,
                ):
                    return True
                if check_down(
                    board,
                    letter,
                    number_of_rows,
                    number_of_cols,
                    number_of_matches,
                    i,
                    j,
                ):
                    return True
                if check_diagonal_right(
                    board,
                    letter,
                    number_of_rows,
                    number_of_cols,
                    number_of_matches,
                    i,
                    j,
                ):
                    return True
                if check_diagonal_left(
                    board,
                    letter,
                    number_of_rows,
                    number_of_cols,
                    number_of_matches,
                    i,
                    j,
                ):
                    return True
    return False


def get_board_copy(board: List[List[str]]) -> List[List[str]]:
    """
    Return a copy of the current board.

    Parameters
    ----------
    board : List[List[str]]
        Current copy of the board

    Returns
    -------
    List[List[str]]
        Copy of the current board.
    """
    board_copy: List[List[str]] = [
        [board[i][j] for j in range(len(board[i]))] for i in range(len(board))
    ]
    return board_copy


def is_space_free(board: List[List[str]], row: int, col: int) -> bool:
    """
    Check if current space is clear.

    Parameters
    ----------
    board : List[List[str]]
        Current copy of the board
    row : int
        Desired row
    col : int
        Desired column

    Returns
    -------
    bool
        If the element at the desired row and column is " ", that means it
        is free.
    """
    try:
        if board[row][col] == " ":
            return True
        else:
            return False
    except IndexError:
        return False


def is_move_valid(board: List[List[str]], pos: str) -> bool:
    """
    Return if move is valid.

    Parameters
    ----------
    board : List[List[str]]
        Current copy of the board
    pos : str
        Inputed position from the get_player_move function

    Returns
    -------
    bool
        If the pos input meets all the conditions, then the move is valid
    """
    if not pos.replace(" ", "").isdigit():
        return False
    row: int = int(pos.split()[0])
    col: int = int(pos.split()[1])
    if not is_space_free(board, row, col):
        return False
    if (row < 0) or (col < 0):
        return False
    return True


def get_player_move(
    board: List[List[str]], number_of_rows: int, number_of_cols: int
) -> Tuple[int, int]:
    """
    Return valid player move.

    Parameters
    ----------
    board : List[List[str]]
        Current copy of the board
    number_of_rows : int
        Number of rows in the board
    number_of_cols : int
        Number of columns in the board

    Returns
    -------
    Tuple[int, int]
        Valid player movement in form of a tuple
    """
    pos_input: str = "ugh"
    while not is_move_valid(board, pos_input):
        print(
            "What is your next move? (0-{}, 0-{})\n".format(
                number_of_rows - 1, number_of_cols - 1
            )
        )
        pos_input = input()
    return int(pos_input.split()[0]), int(pos_input.split()[1])


def choose_random_move_from_list(
    board: List[List[str]], moves_list: List[List[int]]
) -> Tuple[int, int]:
    """
    Choose a random element from a list of lists of strings (coordinates).

    Parameters
    ----------
    board : List[List[str]]
        Current copy of the board
    moves_list : List[List[int]]
        List of open spaces

    Returns
    -------
    Tuple[int, int]
        A random coordinate from move_list in form of a tuple
    """
    random.seed(0)
    move = random.choice(moves_list)
    return move[0], move[1]


def get_empty_spaces(
    board: List[List[str]], number_of_rows: int, number_of_cols: int
) -> List[List[int]]:
    """
    Return all available spaces.

    Parameters
    ----------
    board : List[List[str]]
        Current copy of the board
    number_of_rows : int
        Number of rows in board
    number_of_cols : int
        Number of columns in board

    Returns
    -------
    List[List[int]]
        A list of available coordinates
    """
    empty_spaces: List[List[int]] = []
    for i in range(number_of_rows):
        for j in range(number_of_cols):
            if board[i][j] == " ":
                empty_spaces.append([i, j])
    return empty_spaces


def get_computer_move(
    board: List[List[str]],
    computer_letter: str,
    human_letter: str,
    number_of_rows: int,
    number_of_cols: int,
    number_of_matches: int,
) -> Tuple[int, int]:
    """
    Return a near-sighted move from the computer.

    First, the computer checks if
    it can win. Next, it checks if the player can win. If either is True, it
    acts accordingly. Else, it chooses a random move.

    Parameters
    ----------
    board : List[List[str]]
        Current copy of the board
    computer_letter : str
        Letter given to the computer at the start of the game
    human_letter : str
        Letter given to the computer at the start of the game
    number_of_rows : int
        Number of rows in board
    number_of_cols : int
        Number of columns in board
    number_of_matches : int
        How many letters need to be in a row to win

    Returns
    -------
    Tuple[int, int]
        Computer move returned after determining aforementioned conditions
    """
    board_copy = get_board_copy(board)
    possible_moves: List[List[int]] = get_empty_spaces(
        board, number_of_rows, number_of_cols
    )
    for moves in possible_moves:
        make_move(board_copy, computer_letter, moves[0], moves[1])
        test = is_winner(
            board_copy,
            computer_letter,
            number_of_rows,
            number_of_cols,
            number_of_matches,
        )
        if test:
            return int(moves[0]), int(moves[1])
        make_move(board_copy, human_letter, moves[0], moves[1])
        test = is_winner(
            board_copy, human_letter, number_of_rows, number_of_cols, number_of_matches
        )
        if test:
            return int(moves[0]), int(moves[1])
        make_move(board_copy, " ", moves[0], moves[1])
    return choose_random_move_from_list(board, possible_moves)


def is_board_full(
    board: List[List[str]], number_of_rows: int, number_of_cols: int
) -> bool:
    """
    Check if all spaces are not " " (empty).

    Parameters
    ----------
    board : List[List[str]]
        Current copy of the board
    number_of_rows : int
        Number of rows in board
    number_of_cols : int
        Number of columns in board

    Returns
    -------
    bool
        If any space is empty, return False. Otherwise, return True
    """
    for row in board:
        if " " in row:
            return False
    return True


def main() -> None:
    """Run the game."""
    print("Welcome to m-n-k game!")

    while True:
        m: int = int(input("\nEnter number of rows, m: "))
        n: int = int(input("\nEnter number of columns, n: "))
        k: int = 0
        print(
            "\nWhere k should be greater than 2 and should not be greater than m or n,"
        )
        while k <= 2 or k > m or k > n:
            k = int(input("enter run length to win, k: "))
        the_board: List[List[str]] = [[" "] * n for i in range(m)]
        player_letter, computer_letter = input_player_letter()
        turn: str = who_goes_first()
        print("\nThe " + turn + " will go first.\n")
        game_is_playing: bool = True

        while game_is_playing:
            if turn == "human player":
                draw_board(the_board, m, n)
                row: int
                col: int
                row, col = get_player_move(the_board, m, n)
                make_move(the_board, player_letter, row, col)
                if is_winner(the_board, player_letter, m, n, k):
                    draw_board(the_board, m, n)
                    print("Hooray! You have won the game!\n")
                    game_is_playing = False
                else:
                    if is_board_full(the_board, m, n):
                        draw_board(the_board, m, n)
                        print("The game is a tie!\n")
                        break
                    else:
                        turn = "computer"
            else:
                row, col = get_computer_move(
                    the_board, computer_letter, player_letter, m, n, k
                )
                make_move(the_board, computer_letter, row, col)

                if is_winner(the_board, computer_letter, m, n, k):
                    draw_board(the_board, m, n)
                    print("The computer has beaten you! You lose.")
                    game_is_playing = False
                else:
                    if is_board_full(the_board, m, n):
                        draw_board(the_board, m, n)
                        print("The game is a tie!")
                        break
                    else:
                        turn = "human player"

        print("Do you want to play again? (y or n)")
        if not input().lower().startswith("y"):
            break


if __name__ == "__main__":
    main()
