from graphics import *

# a piece represents either an 'x' or an 'o' on the playing board
class piece:
    type: str
    postion: tuple[int, int]

    # constructor
    def __init__(self, type, position):
        if type == 'x' or type == 'o' or type == 'empty':                       # can either be an 'x', an 'o', or 'empty'
            self.type = type
        (x,y) = position                                                        # unpacking position into (x, y)
        self.position = (int(x), int(y))                                        # make sure (x, y) are both ints
    
    # to string method
    def to_string(self):
        print("piece type: " + self.type + ", position: " + str(self.position))
