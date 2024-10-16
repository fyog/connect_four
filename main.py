from player import * 
from board import *
from window import *
from piece import *
LENGTH = 1200
WIDTH = 800
ROWS = 10
COLS = 12

# main iteration loop for the program
def main():
    player_1 = player('x') # player 1 is X
    player_2 = player('o') # player 2 is O
    my_board = board(ROWS, COLS) # build the initial playing surface
    my_window = window(LENGTH, WIDTH) 
    my_window.buildGrid(my_board) # generate grid corresponding to the playing board
    turn_number = 0
    game_over = False

    # game loop
    while (game_over == False):

        # determine which player's turn it is based on the turn number
        player_tmp = player('tmp')
        if (turn_number % 2 == 0):
            player_tmp = player_1
        else:
            player_tmp = player_2

        # get user input
        (u,v) = player_tmp.getInput(my_window.win.getMouse(), my_window, ROWS, COLS, LENGTH, WIDTH)
        
        # apply the player's move to the board
        flag = my_board.placePiece(u, v, player_tmp.player_type)

        # render the current board
        my_window.render(my_board)

        # check for a win or a game over
        game_over = my_board.logic(ROWS, COLS)
    
        # increase the turn count (so long as the player's move was valid)
        if flag:
            turn_number +=1
        
    my_window.win.getMouse()
main()
