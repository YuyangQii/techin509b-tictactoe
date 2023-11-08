# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player

def print_board(board):
    for row in board:
        print(" | ".join([' ' if cell is None else cell for cell in row]))
        print("-" * 5)

def take_turn(player, board):
    print(f"\n{player}'s turn.")
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
     # Check if the selected cell is empty
    if board[row][col] is None:
        board[row][col] = player
        return True
    else:
        print("Invalid move! Cell already taken.")
        return False
    

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player = 'X'
    
    while winner == None:
        print_board(board)
        if take_turn(current_player, board):
            winner = get_winner(board)
            if winner is None:
                current_player = other_player(current_player)
    print_board(board)
    print(f"\n{winner} wins!")

# Reminder to check all the tests
