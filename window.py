from graphics import *
from board import *
from piece import *

# represents the window through which the game is viewed
class window:

    # class attributes 
    win = GraphWin

    # constructor
    def __init__(self, length, width):
        self.win.width = int(width) 
        self.win.height = int(length)
        self.win = GraphWin("Connect Four", length, width)     

    # to string method  
    def toString(self):
        print("window length: " + str(self.length) + ", window width: " + str(self.width))
    

    # builds the grid based on window annd board parameters
    def buildGrid(self, board):

        # columnn lines
        for i in range(board.width):
            if i != 0:
                line = Line(Point(self.win.width * i / board.width, 0), Point(self.win.width * i / board.width, self.win.height))
                line.draw(self.win)

        # row lines
        for j in range(board.length):
           if j != 0:
               line = Line(Point(0, self.win.height * j / board.length), Point(self.win.width, self.win.height * j / board.length))
               line.draw(self.win)
    
    # draw an O at the given (x,y) location
    def drawO(self, board, x, y):

        radius = min(0.333 * self.win.width / board.width, 0.333 * self.win.height / board.length)
        offset_x = 0.5 * self.win.width / board.width
        offset_y = 0.5 * self.win.height / board.length

        # draw shape
        circle = Circle(Point((x) * self.win.width / board.width + offset_x, (y) * self.win.height / board.length + offset_y), radius)
        circle.draw(self.win)

    # draw an X at the given (x,y) location
    def drawX(self, board, x, y):

        offset_x = self.win.width / board.width
        offset_y = self.win.height / board.length

        # draw shape
        l1 = Line(Point((x) * self.win.width / board.width, (y) * self.win.height / board.length), Point((x) * self.win.width / board.width + offset_x, (y) * self.win.height / board.length + offset_y))
        l2 = Line(Point((x) * self.win.width / board.width, (y) * self.win.height / board.length + offset_y), Point((x) * self.win.width / board.width + offset_x, (y) * self.win.height / board.length))
        l1.draw(self.win)
        l2.draw(self.win)

    # render the current board, drawing X's and O's where they belong
    def render(self, board):
        k = 0
        for _ in board.board:          
            j = 0
            for i in _:
                if i == 'o':
                    self.drawO(board, k, j)
                if i == 'x':
                    self.drawX(board, k, j)
                j += 1
            k += 1

        
              

 
