from tic_tac_toe import *

# WELCOME TO THE GAME
print('WELCOME to TIC-TAC-TOE')
print('-+-+-+-+-+-+-+-+-+-+-+-')

while True:
    # Taking that which player will play by which marker
    player_1_marker, player_2_marker = player_choice_marker()

    # Selecting randomly which player will play first
    turn = choose_first()
    print(f"{turn} will play first!")

    # Asking if ready to play!
    play_game = input('Ready to play game? (Y/N): ').upper()

    if play_game == 'Y':
        game_on = True
    # else: 
    #     game_on = False

    # Starting the main game (loop)
    while game_on:
        
        # PLAYER 1 
        if turn == 'Player 1':
            display_board(board)
            
            # Choosing a position for player 1
            player_1_choice = player_choice(board)
            
            # Placing the marker on that position 
            place_marker(board,player_1_marker,player_1_choice)
            
            # Checking if they won
            if win_check(board,player_1_marker):
                display_board(board)
                print('Congrats to player 1! YOU WON 😀')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'
                    
        # PLAYER 2
        elif turn == 'Player 2':
            display_board(board)
            
            # Choosing a position for player 2
            player_2_choice = player_choice(board)
            
            # Placing the marker on that position 
            place_marker(board,player_2_marker,player_2_choice)
            
            # Checking if they won
            if win_check(board,player_2_marker):
                display_board(board)
                print('Congrats to player 2! YOU WON 😀')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 1'
                
    # Asking if they want to play again or not  
    if not replay():
        break