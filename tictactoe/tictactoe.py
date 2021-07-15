"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Initialize x's and o's counter
    x_counter = 0
    o_counter = 0

    # Check the board and count x's and o's
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_counter += 1
            elif board[i][j] == O:
                o_counter += 1

    # Return whose turn it is
    if x_counter > o_counter:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Create empty set of possible actions
    possible_actions = set()

    # Fill the set with possible actions
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    # Return the result
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check if move is valid
    if action not in actions(board):
        raise Exception("Invalid move")

    # Copy board and update the copy with the action
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontally
    for i in range(3):
        x_counter = 0
        o_counter = 0
        for j in range(3):
            if board[i][j] == X:
                x_counter += 1
            elif board[i][j] == O:
                o_counter += 1
        if x_counter == 3:
            return X
        elif o_counter == 3:
            return O

    # Vertically
    for i in range(3):
        x_counter = 0
        o_counter = 0
        for j in range(3):
            if board[j][i] == X:
                x_counter += 1
            elif board[j][i] == O:
                o_counter += 1
        if x_counter == 3:
            return X
        elif o_counter == 3:
            return O

    # Diagonally
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == X:
            return X
        elif board[0][2] == O:
            return O

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is None:
        return 0
    elif winner(board) == X:
        return 1
    else:
        return -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    output = None
    if player(board) == X:
        v = -math.inf

        for action in actions(board):
            if min_value(result(board, action)) > v:
                v = min_value(result(board, action))
                output = action
        return output

    else:
        v = math.inf

        for action in actions(board):
            if max_value(result(board, action)) < v:
                v = max_value(result(board, action))
                output = action
        return output


def max_value(board):

    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):

    if terminal(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
