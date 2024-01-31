"""
Tic Tac Toe Player
"""

import math

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
    x_count = 0
    o_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count+=1
            elif board[i][j] == O:
                o_count+=1
    
    if x_count == o_count:
        return X
    else:
        return O

    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i,j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [[EMPTY for _ in range(3)] for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            new_board[i][j] = board[i][j]

    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid Move")
    else:
        new_board[action[0]][action[1]] = player(board)
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check horizontally and vertically
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]

    # Check diagonally
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    # No winner found
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    for row in board:
        if EMPTY in row:
            return False
        
    return True




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
def min_value(board):
    if terminal(board):
        return utility(board), None
    
    value = math.inf
    best_action = None
    for action in actions(board):
        temp_value,_ = max_value(result(board, action))
        if value > temp_value:
            value = temp_value
            best_action = action
    
    return value, best_action
    

def max_value(board):
    if terminal(board):
        return utility(board), None
    
    value = -math.inf
    best_action = None
    for action in actions(board):
        temp_value,_ = min_value(result(board, action))
        if value < temp_value:
            value = temp_value
            best_action = action
    
    return value, best_action


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == X:
        _, action = max_value(board)
    elif player(board) == O:
         _, action = min_value(board)

    return action

