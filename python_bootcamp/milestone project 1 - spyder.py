# -*- coding: utf-8 -*-
"""
Created on Fri May 12 16:32:19 2017

@author: rburnsid
"""

def print_board(board):
    clear_output()
    horizontal = '----------------'
    print('\n\nTIC TAC TOE\n\n')
    print('   | 1 | 2 | 3 |')
    print(horizontal)
    print(' A |',board['A1'],'|',board['A2'],'|',board['A3'],'|')
    print(horizontal)
    print(' B |',board['B1'],'|',board['B2'],'|',board['B3'],'|')
    print(horizontal)
    print(' C |',board['C1'],'|',board['C2'],'|',board['C3'],'|')
    print(horizontal)
    sleep(.1)
   
    return


def input_verification(location):
    #strip it of white spaces
    location = location.replace(" ", "")
    if len(location) != 3:
        print('invalid input - more than 2 characters')
    pass


def check_for_win(board):
    #horizontal winning combinations
    if board['A1'] == board['A2'] and board['A2'] == board['A3'] and board['A1'] != ' ' and board['A2'] != ' ' and board['A3'] != ' ':
        return 1
    elif board['B1'] == board['B2'] and board['B2'] == board['B3'] and board['B1'] != ' ' and board['B2'] != ' ' and board['B3'] != ' ':
        return 1
    elif board['C1'] == board['C2'] and board['C2'] == board['C3'] and board['C1'] != ' ' and board['C2'] != ' ' and board['C3'] != ' ':
        return 1

    #vertical winning combinations
    elif board['A1'] == board['B1'] and board['B1'] == board['C1'] and board['A1'] != ' ' and board['B1'] != ' ' and board['C1'] != ' ':
        return 1
    elif board['A2'] == board['B2'] and board['B2'] == board['C2'] and board['A2'] != ' ' and board['B2'] != ' ' and board['C2'] != ' ':
        return 1
    elif board['A3'] == board['B3'] and board['B3'] == board['C3'] and board['A3'] != ' ' and board['B3'] != ' ' and board['C3'] != ' ':
        return 1

    #diagnol winning combinations
    elif board['A1'] == board['B2'] and board['B2'] == board['C3'] and board['A1'] != ' ' and board['B2'] != ' ' and board['C3'] != ' ':
        return 1
    elif board['C1'] == board['B2'] and board['B2'] == board['A3'] and board['C1'] != ' ' and board['B2'] != ' ' and board['A3'] != ' ':
        return 1

    #no winners found
    else:
        return 0


def location_x_o(board, turn_x):
    if turn_x == 1:
        player = 'X'
    else:
        player = 'O'
        
    location = input('\n\nPlayer %s - select a location (i.e. C2 or \"quit\" to exit): ' %(player))
    if location == 'quit':
        return 0
    for i in board:
        if str(i) == location:
            board[i] = player
    return board
    
       
def quit_playing(turn_x):
    if turn_x == 1:
        player = 'X'
    else:
        player = 'O'
    
    print('\n\nCongratulations player %s! You Won!\n\n' %(player))
    quit = input('Quit playing? (Y/N): ')

    if quit == 'Y':
        return 1
    else:
        return 0      


# ---MAIN BODY OF THE GAME---
from IPython.display import clear_output
from time import sleep

# board = {'key1':'value1','key2':'value2'}
board = {'A1':' ','A2':' ','A3':' ','B1':' ','B2':' ','B3':' ','C1':' ','C2':' ','C3':' '}
turn_x = 0
quit = 'N'

while quit == 'N':
    turn_x = not turn_x
    print_board(board)
    board = location_x_o(board, turn_x)
    if board == 0:
        break

    if check_for_win(board) == 1:
        print_board(board)
        if quit_playing(turn_x) == 1:
            break
        else:
            # reinitialize the board
            board = {'A1':' ','A2':' ','A3':' ','B1':' ','B2':' ','B3':' ','C1':' ','C2':' ','C3':' '}
            continue