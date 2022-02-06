# Imports
import os
import random

# Functions
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def display_board(board):
    clearConsole()
    disboard=''
    for row in [7,4,1]:
        disboard+= ' | '.join(board[row:row+3])+ '\n'

    print(disboard)
    
def player_input():
    choice=['X','O']
    while True:
        player = input('Please choose X or O: ').upper()
        if player in choice:
            if player=='X':
                firstplayermarker='X'
                secondplayermarker='O'
            elif player=='O':
                firstplayermarker='O'
                secondplayermarker='X'
            return (firstplayermarker,secondplayermarker)
        else:
            print('Sorry! Please choose either X or O')    

def place_marker(board, marker, position):
    if position in range(1,10):
        board[position]=marker
    return board

def win_check(board, mark):
    #horizonal
    if all(m == mark for m in board[1:4] ) or all(m == mark for m in board[4:7]) or all(m == mark for m in board[7:10]):
        print(f'Player {mark} wins the game')
        return True
    #vertical
    elif all(m == mark for m in board[1:8:3]) or all(m == mark for m in board[2:9:3]) or all(m == mark for m in board[3:10:3] ):
        print(f'Player {mark} wins the game')
        return True   
    #diagonal
    elif all(m == mark for m in board[1:10:4] ) or all(m == mark for m in board[3:8:2]):
        print(f'Player {mark} wins the game')
        return True
    else:
        return False
    
def choose_first():
    first = random.randint(1,2)
    if first==1:
        print('Player 1 goes first.')
    else:
        print('Player 2 goes first.')

def space_check(board, position):
    if board[position]=='' or board[position]==' ':
        freespace= True
        return freespace
    else:
        freespace= False
        return freespace

def full_board_check(board):
    for fullboard in board[1:10]:
        if fullboard==' ':
            return False
    print('Game is a Tie!')
    return True           
        
def player_choice(board):
    positionchoice=False
    while positionchoice==False:
        position=input('Choose position [1,9]: ')
        if position.isdigit():
            position=int(position)
        else:
            print('This is not a digit, try again.')
            continue
        if position in range(1,10) :
            positionchoice=space_check(board,position)
        else:
            print('Please choose a valid position [1,9].')
    return position

def replay():
    inputcheck=False
    while inputcheck==False:
        playagainchoice = input('Do you want to play again? Y or N. ').upper()
        if playagainchoice== 'Y' or playagainchoice=='N':
            if playagainchoice=='Y':
                playchoice = True
            else:
                playchoice = False
            inputcheck=True
        else:
            print('Please choose a valid answer, Y or N.\n')
            inputcheck=False

    return playchoice

# Game Code
print('Welcome to Tic Tac Toe!')
row1 = ' 1 | 2 | 3 '
row2 = ' 4 | 5 | 6 '
row3 = ' 7 | 8 | 9 '
print(row3)
print(row2)
print(row1)

playagain = True
while playagain == True:
    # Set the game up here
    choose_first()
    (firstplayermarker, secondplayermarker) = player_input()
    game_off = False
    board = ['#', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ']
    while game_off == False:
        #Player 1 Turn
        position = player_choice(board)
        place_marker(board, firstplayermarker, position)
        display_board(board)
        game_off = win_check(board, firstplayermarker)
        if game_off:
            break
        game_off = full_board_check(board)
        if game_off:
            break
        print(f"{secondplayermarker}'s Turn")

        # Player2's turn.
        position = player_choice(board)
        place_marker(board, secondplayermarker, position)
        display_board(board)
        game_off = win_check(board, secondplayermarker)
        if game_off:
            break
        game_off = full_board_check(board)
        if game_off:
            break
        print(f"{firstplayermarker}'s Turn")

    playagain = replay()
        