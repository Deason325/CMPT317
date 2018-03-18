'''
    Class: Queen: Same as Dragons, only different is id, which tell the function it’s a queen.

'''

def findPiece(x, y, wights, queens, queen):
    piece = 1
    if (x < 0 or x > 4 or y < 0 or y > 4):
        piece = 0
    for w in wights:
        if w.x == x and w.y == y:
            piece = w
    for q in queen:
        if q.x == x and q.y == y:
            piece = q
    for d in queens:
        if d.x == x and d.y == y:
            piece = d
    return piece


class Queen:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.id='q'
        self.worth = 300

    def setWorth(self):
        self.worth = 300
    def qCanUp(queen, w, d, q):
        piece = findPiece(queen.x - 1, queen.y, w, d, q)
        if piece == 0:
            return False
        elif piece == 1:
            return True
        elif piece.id == 'w':
            return True
        else:
            return False

    def qCanDown(queen, w, d, q):
        piece = findPiece(queen.x + 1, queen.y, w, d, q)
        if piece == 0:
            return False
        elif piece == 1:
            return True
        elif piece.id == 'w':
            return True
        else:
            return False

    def qCanLeft(queen, w, d, q):
        piece = findPiece(queen.x, queen.y - 1, w, d, q)
        if piece == 0:
            return False
        elif piece == 1:
            return True
        elif piece.id == 'w':
            return True
        else:
            return False

    def qCanRight(queen, w, d, q):
        piece = findPiece(queen.x, queen.y + 1, w, d, q)
        if piece == 0:
            return False
        elif piece == 1:
            return True
        elif piece.id == 'w':
            return True
        else:
            return False

    def qCanTopLeft(queen, w, d, q):
        piece = findPiece(queen.x - 1, queen.y - 1, w, d, q)
        if piece == 0:
            return False
        elif piece == 1:
            return True
        elif piece.id == 'w':
            return True
        else:
            return False

    def qCanTopRight(queen, w, d, q):
        piece = findPiece(queen.x - 1, queen.y + 1, w, d, q)
        if piece == 0:
            return False
        elif piece == 1:
            return True
        elif piece.id == 'w':
            return True
        else:
            return False

    def qCanBotLeft(queen, w, d, q):
        piece = findPiece(queen.x + 1, queen.y - 1, w, d, q)
        if piece == 0:
            return False
        elif piece == 1:
            return True
        elif piece.id == 'w':
            return True
        else:
            return False

    def qCanBotRight(queen, w, d, q):
        piece = findPiece(queen.x + 1, queen.y + 1, w, d, q)
        if piece == 0:
            return False
        elif piece == 1:
            return True
        elif piece.id == 'w':
            return True
        else:
            return False

    '''
    movement for dragon and queens
    forward and backward if confusing, so I decied to use upward and downward,
    a dragon/queen moves upward by move into the square on top of it on the board,
    moves downward by move into the the square on bottom of it on the board,
    moves left by move into the square on left of it on the board.
    Moves up-left diagonal by move into the square on top left of it.
    '''

    def qUpward(i, j, w, d, q):
        i = i - 1
        j = j - 1
        global moved
        if i <= 0:
            print("Can not move forward.")
            moved = False
            return
        piece = findPiece(i, j, w, d, q)
        nextP = findPiece(i - 1, j, w, d, q)
        if piece == 1 or piece.id == 'w':
            print("No dragon/queen on", i + 1, ",", j + 1)
            moved = False
        elif (piece.id == 'd' or piece.id == 'q'):
            if nextP == 1:
                piece.x -= 1
                moved = True
            elif nextP.id == 'd' or nextP.id == 'q':
                print("Blocked by", nextP.id)
                moved = False
            elif nextP.id == 'w':
                w.remove(nextP)
                piece.x -= 1
                moved = True
        q.setWorth()

    def qDownward(i, j, w, d, q):
        i = i - 1
        j = j - 1
        global moved
        if i >= 4:
            print("Can not move backward.")
            moved = False
            return
        piece = findPiece(i, j, w, d, q)
        nextP = findPiece(i + 1, j, w, d, q)
        if piece == 1 or piece.id == 'w':
            print("No dragon/queen on", i + 1, ",", j + 1)
            moved = False
        elif (piece.id == 'd' or piece.id == 'q'):
            if nextP == 1:
                piece.x += 1
                moved = True
            elif nextP.id == 'd' or nextP.id == 'q':
                print("Blocked by", nextP.id)
                moved = False
            elif nextP.id == 'w':
                w.remove(nextP)
                piece.x += 1
                moved = True
        q.setWorth()

    def qLeft(i, j, w, d, q):
        i = i - 1
        j = j - 1
        global moved
        if j <= 0:
            print("Can not move left.")
            moved = False
            return
        piece = findPiece(i, j, w, d, q)
        nextP = findPiece(i, j - 1, w, d, q)
        if piece == 1 or piece.id == 'w':
            print("No dragon/queen on", i + 1, ",", j + 1)
            moved = False
        elif (piece.id == 'd' or piece.id == 'q'):
            if nextP == 1:
                piece.y -= 1
                moved = True
            elif nextP.id == 'd' or nextP.id == 'q':
                print("Blocked by", nextP.id)
                moved = False
            elif nextP.id == 'w':
                w.remove(nextP)
                piece.y -= 1
                moved = True
        q.setWorth()
    def qRight(i, j, w, d, q):
        i = i - 1
        j = j - 1
        global moved
        if j >= 4:
            print("Can not move right.")
            moved = False
            return
        piece = findPiece(i, j, w, d, q)
        nextP = findPiece(i, j + 1, w, d, q)
        if piece == 1 or piece.id == 'w':
            print("No dragon/queen on", i + 1, ",", j + 1)
            moved = False
        elif (piece.id == 'd' or piece.id == 'q'):
            if nextP == 1:
                piece.y += 1
                moved = True
            elif nextP.id == 'd' or nextP.id == 'q':
                print("Blocked by", nextP.id)
                moved = False
            elif nextP.id == 'w':
                w.remove(nextP)
                piece.y += 1
                moved = True
        q.setWorth()
    def qUpLeft(i, j, w, d, q):
        i = i - 1
        j = j - 1
        global moved
        if j >= 4:
            print("Can not move right.")
            moved = False
            return
        piece = findPiece(i, j, w, d, q)
        nextP = findPiece(i - 1, j - 1, w, d, q)
        if piece == 1 or piece.id == 'w':
            print("No dragon/queen on", i + 1, ",", j + 1)
            moved = False
        elif (piece.id == 'd' or piece.id == 'q'):
            if nextP == 1:
                piece.x -= 1
                piece.y -= 1
                moved = True
            elif nextP.id == 'd' or nextP.id == 'q':
                print("Blocked by", nextP.id)
                moved = False
            elif nextP.id == 'w':
                w.remove(nextP)
                piece.x -= 1
                piece.y -= 1
                moved = True
        q.setWorth()
    def qUpRight(i, j, w, d, q):
        i = i - 1
        j = j - 1
        global moved
        if j >= 4:
            print("Can not move right.")
            moved = False
            return
        piece = findPiece(i, j, w, d, q)
        nextP = findPiece(i - 1, j + 1, w, d, q)
        if piece == 1 or piece.id == 'w':
            print("No dragon/queen on", i + 1, ",", j + 1)
            moved = False
        elif (piece.id == 'd' or piece.id == 'q'):
            if nextP == 1:
                piece.x -= 1
                piece.y += 1
                moved = True
            elif nextP.id == 'd' or nextP.id == 'q':
                print("Blocked by", nextP.id)
                moved = False
            elif nextP.id == 'w':
                w.remove(nextP)
                piece.x -= 1
                piece.y += 1
                moved = True
        q.setWorth()
    def qDownLeft(i, j, w, d, q):
        i = i - 1
        j = j - 1
        global moved
        if j >= 4:
            print("Can not move right.")
            moved = False
            return
        piece = findPiece(i, j, w, d, q)
        nextP = findPiece(i + 1, j - 1, w, d, q)
        if piece == 1 or piece.id == 'w':
            print("No dragon/queen on", i + 1, ",", j + 1)
            moved = False
        elif (piece.id == 'd' or piece.id == 'q'):
            if nextP == 1:
                piece.x += 1
                piece.y -= 1
                moved = True
            elif nextP.id == 'd' or nextP.id == 'q':
                print("Blocked by", nextP.id)
                moved = False
            elif nextP.id == 'w':
                w.remove(nextP)
                piece.x += 1
                piece.y -= 1
                moved = True
        q.setWorth()
    def qDownRight(i, j, w, d, q):
        i = i - 1
        j = j - 1
        global moved
        if j >= 4:
            print("Can not move right.")
            moved = False
            return
        piece = findPiece(i, j, w, d, q)
        nextP = findPiece(i + 1, j + 1, w, d, q)
        if piece == 1 or piece.id == 'w':
            print("No dragon/queen on", i + 1, ",", j + 1)
            moved = False
        elif (piece.id == 'd' or piece.id == 'q'):
            if nextP == 1:
                piece.x += 1
                piece.y += 1
                moved = True
            elif nextP.id == 'd' or nextP.id == 'q':
                print("Blocked by", nextP.id)
                moved = False
            elif nextP.id == 'w':
                w.remove(nextP)
                piece.x += 1
                piece.y += 1
                moved = True
        q.setWorth()
