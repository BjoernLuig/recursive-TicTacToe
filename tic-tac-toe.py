# -*- coding: utf-8 -*-
"""
@author: Björn Luig
"""

import numpy as np

def check(field): # check rows, columns and diagonals
    for character in ['X','O']:
        equals = (field == character)
        if np.count_nonzero(equals) == 5: return('draw') # draw
        if np.any(np.all(equals,axis=0)) or np.any(np.all(equals,axis=1)): return(character) # rows and columns
        if np.all(equals[[0,1,2],[0,1,2]]) or np.all(equals[[0,1,2],[2,1,0]]): return(character) # diagonal
    return(None)

def think(field,character): # choose best move with recursion (yes, this is very slow)
    result = check(field)
    if result: return(None,None,result) # end of recursion
    # try to win obviously
    for i in range(3):
        for j in range(3):
            if field[i][j] not in ['X','O']:
                field[i][j],character = character,field[i][j]
                result = check(field)
                field[i][j],character = character,field[i][j]
                if result == character: return(i,j,result)
    # try to win with recursion
    opposite = 'X' if character == 'O' else 'O'
    for i in range(3):
        for j in range(3):
            if field[i][j] not in ['X','O']:
                field[i][j],character = character,field[i][j]
                _,_,result = think(field,opposite) # recursion
                field[i][j],character = character,field[i][j]
                if result == character: return(i,j,result)
    # prevent losing with recursion
    for i in range(3):
        for j in range(3):
            if field[i][j] not in ['X','O']:
                field[i][j],character = character,field[i][j]
                _,_,result = think(field,opposite) # recursion
                field[i][j],character = character,field[i][j]
                if result == 'draw': return(i,j,result)
    # losing (this should be impossible)
    for i in range(3):
        for j in range(3):
            if field[i][j] not in ['X','O']: return(i,j,opposite)

def show(): # show the field in the consol
    print('\n-------------\n'.join(['']+['| '+' | '.join(field[i])+' |' for i in range(3)]+['']))
    if   winner == player: print('you won!')
    elif winner == bot: print('you lost!')
    elif winner == 'draw': print('it\'s a draw!')
    else: print('it\'s your turn')

# start game and enter settings
print('TIC TAC TOE')
field = np.array(['₁','₂','₃','₄','₅','₆','₇','₈','₉']).reshape(3,3)
loop = True
while loop:
    player = input('choose your Character (X or O): ')
    if player in ['X','O']: loop = False
    else: print('unvalid character!')
bot = 'O' if player == 'X' else 'X'
loop = True
while loop:
    first = input('who is first? (X or O): ')
    if first in ['X','O']: loop = False
    else: print('unvalid character!')
winner = None
    
# play game
if first == bot:
    print('thinking...')
    i,j,_ = think(field,bot)
    field[i][j] = bot
show()
while not winner:
    text = input('your move? (1,...,9): ')
    if text in '123456789':
        n = int(text)
        j = (n-1)%3
        i = (n-1-j)//3
        if field[i,j] not in ['X','O']:
            # move by player
            field[i][j] = player
            winner = check(field)
            if not winner:
                # move by bot
                print('thinking...')
                i,j,_ = think(field,bot)
                field[i][j] = bot
                winner = check(field)
            show()
        else: print('unvalid move!')
    else: print('unvalid move!')

# end
input('press enter to exit')