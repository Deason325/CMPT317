'''
    Class: Wights. Has field x and y, represent the position on the board.
    Id: tell the search function it’s a wights
    Worth: How much per wight worth, use to calculate the value for minimax
    up,down,left,right: the coordinate of these direction
'''

def findPiece(x, y, wights, dragons, queen):
    piece = 1
    if (x < 0 or x > 4 or y < 0 or y > 4):
        piece = 0
    for w in wights:
        if w.x == x and w.y == y:
            piece = w
    for q in queen:
        if q.x == x and q.y == y:
            piece = q
    for d in dragons:
        if d.x == x and d.y == y:
            piece = d
    return piece


class Wights:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.id = 'w'
        self.worth=20
        self.up = self.x-1
        self.down = self.x+1
        self.left = self.y-1
        self.right = self.y+1



