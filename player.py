from piece import *
from window import *

class player:
    
    player_type: str

    def __init__(self, type):
        self.player_type = type
        
    # get user input as to where they want to place their piece
    def getInput(self, p, window, rows, cols, length, width):
        if (p.x < length and p.x > 0 and p.y < width and p.y > 0):

            # find move col
            u = 0
            for i in range(0, cols):
                if (p.x > i * length / cols and p.x < (i+1) * length / cols):
                    u = i

            # find move row
            v = 0
            for j in range(0, rows):
                if (p.y > j * width / rows and p.y < (j+1) * width / rows):
                    v = j
        
        return (u,v)
