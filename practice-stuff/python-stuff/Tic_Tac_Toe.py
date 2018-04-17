def display_board(board):
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-------------------------------')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-------------------------------')
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    marker =''
    #Keep asking to choose X or O
    #assign vtoriot na sprotivnoto
    while marker != 'X' and marker != 'O':
        marker=input('Player1 choose X or O')
    player1=marker
    if player1 == 'X':
        player2 =='O'
    else:
        player1=='O'
        player2=='X'

def place_marker(board, marker, position):
    pass

def win_check(board, mark):
    pass

def choose_first():
    pass

def space_check(board, position):
    pass

def full_board_check (board):
    pass

def player_choice(board):
    pass

def replay():
    pass

print('Welcome to Tic tac Toe!')

test_board=['#','X','O','X','O','X','X','O','X','O','X']
display_board(test_board)
# while True:
#   Set the game up here
#   pass

#   while game_on:
#   player1's turn


#   player2's turn.
#       pass

#   if not reply():
#       break
