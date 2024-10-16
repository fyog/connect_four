from piece import *

# board class represents the playing surface on which the game is played
class board:
    length: int
    width: int
    board: list[list[int]]

    # constructor
    def __init__(self, length, width):
        self.length = int(length) 
        self.width = int(width)
        self.board = [['empty' for _ in range(width)] for _ in range(length)] # board is initially empty at every location (uses list comprehension)

    # place the given piece at the given coords
    def placePiece(self, x, y, ch):
        if self.board[x][y] == 'empty':
            if ch == 'x' or ch == 'o':
                self.board[x][y] = ch
                return True
        else:
            print("Piece could not be placed, position is already taken.")
            return False

    # return the contents of the given cell
    def checkCell(self, x, y):
        ch = self.board[x, y]
        return ch
    
    # render the current board
    def renderBoard(self):
        # check every cell
        print("render board")

    def game_over(self):
        goal_count = self.length * self.width
        count = 0
        for i in range(self.length):
            for j in range (self.width):
                if (self.board[i][j] != 'empty'):
                    count += 1

        if (count == goal_count):
            return 0

        else:
            return 1

    # check the current board for a winner or draw
    def logic(self, cols, rows):
        game_over = False

        # check for vertical win
        for i in range(cols):
            for j in range(rows-3):
                if self.board[i][j] == 'x':
                    if self.board[i][j+1] == 'x' and self.board[i][j+2] == 'x' and self.board[i][j+3] == 'x':
                        print('vertical winner is player X.')
                        game_over = True
                if self.board[i][j] == 'o':
                    if self.board[i][j+1] == 'o' and self.board[i][j+2] == 'o' and self.board[i][j+3] == 'o':
                        print('vertical winner is player O.')
                        game_over = True

        # check for horizontal win
        for i in range(cols-3):
            for j in range(rows):
                if self.board[i][j] == 'x':
                    if self.board[i+1][j] == 'x' and self.board[i+2][j] == 'x' and self.board[i+3][j] == 'x':
                        print('horizontal winner is player X.')
                        game_over = True 
                if self.board[i][j] == 'o':
                    if self.board[i+1][j] == 'o' and self.board[i+2][j] == 'o' and self.board[i+3][j] == 'o':
                        print('horizontal winner is player O.')
                        game_over = True
                       
        
        #check for diagonal win
        for i in range(cols-3):
            for j in range(rows-3):
                if self.board[i][j] == 'x':
                    if self.board[i+1][j+1] == 'x' and self.board[i+2][j+2] == 'x' and self.board[i+3][j+3] == 'x':
                        print('diagonal winner is player X.')
                        game_over = True
                if self.board[i][j] == 'o':
                    if self.board[i+1][j+1] == 'o' and self.board[i+2][j+2] == 'o' and self.board[i+3][j+3] == 'o':
                        print('diagonal winner is player O.')
                        game_over = True
        for i in range(0, cols-3):
            for j in range(0, rows-3):
                if self.board[i][j] == 'x':
                    if self.board[i+1][j-1] == 'x' and self.board[i+2][j-2] == 'x' and self.board[i+3][j-3] == 'x':
                        print('diagonal winner is player X.')
                        game_over = True
                if self.board[i][j] == 'o':
                    if self.board[i+1][j-1] == 'o' and self.board[i+2][j-2] == 'o' and self.board[i+3][j-3] == 'o':
                        print('diagonal winner is player O.')
                        game_over = True

        if (self.game_over() == 0):
            print('Board is full. Game is a draw.')
            game_over = True
        
        if game_over:
            print('Game over.')

        return game_over
    

