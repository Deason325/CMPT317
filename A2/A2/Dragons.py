'''
    Class: Dragons.	 Has field x and y, represent the position on the board.
    Id: tell the search function it’s a dragon
    Worth: How much per wight worth, use to calculate the value for minimax
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


class Dragons:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.id='d'
        self.worth = 30

    def dCanUp(dragon, w, d, q):
        piece = findPiece(dragon.x - 1, dragon.y, w, d, q)
        if piece == 0:
            return False
        elif piece == 1:
            return True
        elif piece.id == 'w':
            return True
        else:
            return False

    def dCanDown(dragon, w, d, q):
        piece = findPiece(dragon.x + 1, dragon.y, w, d, q)
        if piece == 0:
            return False
        elif piece == 1:
            return True
        elif piece.id == 'w':
            return True
        else:
            return False

    def dCanLeft(dragon, w, d, q):
        piece = findPiece(dragon.x, dragon.y - 1, w, d, q)
        if piece == 0:
            return False
        elif piece == 1:
            return True
        elif piece.id == 'w':
            return True
        else:
            return False

    def dCanRight(dragon, w, d, q):
        piece = findPiece(dragon.x, dragon.y + 1, w, d, q)
        if piece == 0:
            return False
        elif piece == 1:
            return True
        elif piece.id == 'w':
            return True
        else:
            return False

    def dCanTopLeft(dragon, w, d, q):
        piece = findPiece(dragon.x - 1, dragon.y - 1, w, d, q)
        if piece == 0:
            return False
        elif piece == 1:
            return True
        elif piece.id == 'w':
            return True
        else:
            return False

    def dCanTopRight(dragon, w, d, q):
        piece = findPiece(dragon.x - 1, dragon.y + 1, w, d, q)
        if piece == 0:
            return False
        elif piece == 1:
            return True
        elif piece.id == 'w':
            return True
        else:
            return False

    def dCanBotLeft(dragon, w, d, q):
        piece = findPiece(dragon.x + 1, dragon.y - 1, w, d, q)
        if piece == 0:
            return False
        elif piece == 1:
            return True
        elif piece.id == 'w':
            return True
        else:
            return False

    def dCanBotRight(dragon, w, d, q):
        piece = findPiece(dragon.x + 1, dragon.y + 1, w, d, q)
        if piece == 0:
            return False
        elif piece == 1:
            return True
        elif piece.id == 'w':
            return True
        else:
            return False

    '''
    movement for queen and dragons
    forward and backward if confusing, so I decied to use upward and downward,
    a dragon/queen moves upward by move into the square on top of it on the board,
    moves downward by move into the the square on bottom of it on the board,
    moves left by move into the square on left of it on the board.
    Moves up-left diagonal by move into the square on top left of it.
    '''

    def dUpward(i, j, w, d, q):
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

    def dDownward(i, j, w, d, q):
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

    def dLeft(i, j, w, d, q):
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

    def dRight(i, j, w, d, q):
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

    def dUpLeft(i, j, w, d, q):
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

    def dUpRight(i, j, w, d, q):
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

    def dDownLeft(i, j, w, d, q):
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

def dDownRight(i, j, w, d, q):
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
