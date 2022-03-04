import os

from numpy import full
# Created the main game board
board = [' '] * 10

# board = ['#','X','O','X','O','X','O','X','O','X'] # => Test case board

# Displaying the main board
def display_board(board):
    os.system('cls')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
# display_board(board)

# Taking player input as "X" or "O"
def player_choice_marker():
    
    player_1 = ''
    while player_1 != 'X' and player_1 != 'O':
        player_1 = input("Player 1, Select 'X' or 'O': ").upper()
    
    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'
    
    return (player_1, player_2)

# Placing marks on the main board
def place_marker(board,marker,position):
    
    board[position] = marker
    # display_board(board)
# place_marker(board,'$',9)

# Checking if any player won or not
def win_check(board,mark):
    
    """
    Function that checks win condition. (Returns bool)
    """
    # Rows
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    
    # Column
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    
    # Diagonal
    if board[3] == board[5] == board[7] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    
    return False
# print(win_check(board,'X'))

# Creating a function to choose which player to go first
import random
def choose_first():
    key = random.randint(1,2)
    if key == 1:
        return 'Player 1'
    return 'Player 2'

# Checking if any FREE SPACE is available at a particular position in board
def space_check(board, position):
    if board[position] == ' ':
        return True
    return False

# Checking the full board for any free space available (T if full else F)
def full_board_check(board):
    key = 1
    for key in range(1,10):
        if space_check(board,key):
            return False
    return True

# Creating a function that asks for a number within a range and returns
def player_choice(board):
    choice = None
    while choice not in range(1,10) or not space_check(board,choice): # Re-check !!!
        choice = int(input("Enter a number between (1-9): "))
    
    return choice

# Asking the user(s) if they want to play again or not 
def replay():
    play_again = input('Do you want to play again? (Y/N): ').upper()
    if play_again == 'Y':
        return True
    return False