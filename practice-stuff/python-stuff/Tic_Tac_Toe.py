import random
the_board = [' '] * 10
def display_board(board):
    
def display_board(a,b):
    print(f'Available   TIC-TAC-TOE\n  moves\n\n  {a[7]}|{a[8]}|{a[9]}        {b[7]}|{b[8]}|{b[9]}\n  -----        -----\n  {a[4]}|{a[5]}|{a[6]}        {b[4]}|{b[5]}|{b[6]}\n  -----        -----\n  {a[1]}|{a[2]}|{a[3]}        {b[1]}|{b[2]}|{b[3]}\n')
    display_board(available,theBoard)
def player_input():
    marker =''
    #Keep asking to choose X or O
    #assign vtoriot na sprotivnoto
    while not(marker == 'X' or marker == 'O'):
        marker=input('Player1 choose X or O').upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    board[position]==' '

def full_board_check (board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=(input('Choose position 1-9'))
    return position

def replay():
   return input('play again? yes/no').lower().startswith('y')

print('Welcome to Tic tac Toe!')

test_board=['#','X','O','X','O','X','X','O','X','O','X']
display_board(test_board)
while True:
    #   Set the game up here
    the_board=[' ']*10
    player1_marker,player2_marker = player_input()
    turn=choose_first()
    print(turn+ ' will go first ')
    play_game=input('Ready to play? y or n?')
    if play_game.lower()[0] == 'y':
        game_on= True
    else:   
        game_on= False

    while game_on:
        if turn == 'Player 1':
            #show position
            display_board(the_board)

            position=player_choice(the_board)

            place_marker(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player1 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    break
                else:
                    turn='Player 2'
        else:
            display_board(the_board)

            position=player_choice(the_board)

            place_marker(the_board,player2_marker,position)

            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player2 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    break
                else:
                    turn='Player1'

#   while game_on:
#   player1's turn


#   player2's turn.
#       pass

    if not reply():
        break
