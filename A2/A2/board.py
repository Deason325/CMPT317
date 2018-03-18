import random
from Wights import Wights
from Dragons import Dragons
from Queen import Queen
from State import State
import copy
from tree import Node

import sys

''''
Change the value of depth to change the hardness
'''''

'''Class: Board.
    CreateBoard() 	create board with initial pieces
    printBoard(state)	display the board of given state
    getPos(board)	return the positions of wights,dragons,queen on the board
    findpiece(x,y,wights,dragons,queen)	return the piece on location x,y
    moveW(x,y,d,state) give the coordinate of piece and direction, move wights on the coordinate
    d can be1,2,3,4,5,6,7,8, represent 8 different directions
    '''

def createBoard():
    board = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    for i in range(0,5):
        for j in range(0,5):
            board[i][j]='.'
    board[0][2]='Q'
    for i in range(1,2):
        for j in range(1,4):
            board[i][j]='D'
    for i in range(0,5):
        board[4][i]='W'
    return board

def printBoard(state):
    w=state.wights
    d=state.dragons
    q=state.queen
    board = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    for i in range(0,5):
        for j in range(0,5):
            board[i][j]='.'
    for wi in w:
        x=wi.x
        y=wi.y
        board[x][y]='W'
    for di in d:
        x=di.x
        y=di.y
        board[x][y]='D'
    for qi in q:
        x=qi.x
        y=qi.y
        board[x][y]='Q'
    count=0
    for i in range(0,5):
        for j in range(0,5):
            if count<4:
                count+=1
                print(board[i][j],end=" ")
            else:
                count=0
                print(board[i][j],end="\n")

def getPos(board):
    wights = []
    dragons = []
    queenT = []
    for i in range(0,5):
        for j in range(0,5):
            if board[i][j]=='D':
                dragon = Dragons()
                dragon.x=i
                dragon.y=j
                dragons.append(dragon)
            elif board[i][j]=='W':
                wight = Wights()
                wight.x=i
                wight.y=j
                wights.append(wight)
            elif board[i][j]=='Q':
                queen = Queen()
                queen.x=i
                queen.y=j
                queenT.append(queen)
    return wights,dragons,queenT

def findPiece(x,y,wights,dragons,queen):
    piece = 1
    if(x<0 or x>4 or y<0 or y>4):
        piece =  0
    for w in wights:
        if w.x==x and w.y==y:
            piece = w
    for q in queen:
        if q.x==x and q.y==y:
            piece = q
    for d in dragons:
        if d.x==x and d.y==y:
            piece = d
    return piece



'''
    moveD(x,y,d,state) move dragon or queen
    wTurn()	when player controlling wights, it ask for input and check if
    it’s legal to move, if true, move, if false, ask again
    qTurn()	when player controlling queen, it ask for input and check if it’s legal to move
    possibleMoves(state,player)	return a list of all possible moves of player side in current state, return three values, wights,dragons,queen
    printPossibleMoves(): print board of possible moves
    wCanUp,wCanDown…. check if a wight is able to move up/down…
    wCanTopLeft,wCanTopRight…… check if there is a dragon or queen on its top left… if there is, return true, else false
    wForward,wBackward… move the wight
    wForwardLeft…. capture the dragon/queen on its top left, then move to there
    dCanUp,dCanDown…same a wCanUp…
    dUpWard,dDownward…. move the dragon/queen
    searchBestMoveW(states) from a list of state, return the state with highest value for wights
'''

'''
moving wights
'''
def moveW(x,y,d,state):
    wights=state.wights
    dragons=state.dragons
    queen=state.queen
    if d==1:
        wForward(x,y,wights,dragons,queen)
    elif d==2:
        wBackward(x,y,wights,dragons,queen)
    elif d==3:
        wLeft(x,y,wights,dragons,queen)
    elif d==4:
        wRight(x,y,wights,dragons,queen)
    elif d==5:
        wForLeft(x,y,wights,dragons,queen)
    elif d==6:
        wForRight(x,y,wights,dragons,queen)
    elif d==7:
        wBackLeft(x,y,wights,dragons,queen)
    elif d==8:
        wBackRight(x,y,wights,dragons,queen)

    printBoard(state)
'''
moving dragons/queen
'''
def moveD(x,y,d,state):
    wights=state.wights
    dragons=state.dragons
    queen=state.queen
    if d==1:
        dUpward(x,y,wights,dragons,queen)
    elif d==2:
        dDownward(x,y,wights,dragons,queen)
    elif d==3:
        dLeft(x,y,wights,dragons,queen)
    elif d==4:
        dRight(x,y,wights,dragons,queen)
    elif d==5:
        dUpLeft(x,y,wights,dragons,queen)
    elif d==6:
        dUpRight(x,y,wights,dragons,queen)
    elif d==7:
        dDownLeft(x,y,wights,dragons,queen)
    elif d==8:
        dDownRight(x,y,wights,dragons,queen)

    printBoard(state)

'''
turns
'''

'''
    searchBestMoveQ(states) from a list of state, return the state with highest value for queen
    transStates(possibleMoves) combine every three wights,dragons,queen to a state
    getScore() compute the total score of pieces current on board for wights side
    getScoreQ() compute the total score of pieces current on board for queen side
    makeTree() construct the search tree
    search()	search the best move
    recurSearch()	recursively search
    

'''
def wTurn(state):
    wights=state.wights
    print("Wights' turn:")
    while True:
        x = int(input("X coord: "))
        if (x < 1 or x > 5):
            print("X and Y coordinates must between 1 to 5")
            continue
        else:
            break
    while True:
        y = int(input("Y coord: "))
        if (y < 1 or y > 5):
            print("X and Y coordinates must between 1 to 5")
            continue
        else:
            break
    has = False
    for wi in wights:
        if wi.x==x-1 and wi.y==y-1:
            has=True
    if has:
        while True:
            direct = int(input("Direction:"))
            if (direct < 1 or direct > 8):
                print("Direction must be an integer from 1-8:")
                continue
            else:
                break
        moveW(x, y, direct,state)
    else:
        print("No wight on",x,y,"\nPlease enter again.")
        wTurn(state)
    if moved:
        return True
    else:
        wTurn(state)

def qTurn(state):
    dragons=state.dragons
    queen=state.queen
    print("Queen's turn:")
    while True:
        x = int(input("X coord: "))
        if (x < 1 or x > 5):
            print("X and Y coordinates must between 1 to 5")
            continue
        else:
            break
    while True:
        y = int(input("Y coord: "))
        if (y < 1 or y > 5):
            print("X and Y coordinates must between 1 to 5")
            continue
        else:
            break
    has = False
    for di in dragons:
        if di.x==x-1 and di.y==y-1:
            has=True
    for q in queen:
        if q.x==x-1 and q.y==y-1:
            has=True
    if has:
        while True:
            direct = int(input("Direction:"))
            if (direct < 1 or direct > 8):
                print("Direction must be an integer from 1-8:")
                continue
            else:
                break
        moveD(x, y, direct,state)
    else:
        print("No dragon/queen on",x,y,"\nPlease enter again.")
        qTurn(state)
    if moved:
        return True
    else:
        qTurn(state)





'''
find possible moves of a piece
'''
def possibleMoves(state,player):
    wights=state.wights
    dragons=state.dragons
    queen=state.queen
    current = getScore(state)
    possible = []
    if player==1:
        for wi in wights:
            if wCanUp(wi,wights,dragons,queen):
                x=wi.x+1
                y=wi.y+1
                s=str(x)+','+str(y)+"->Forward"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for w in wightsC:
                    if w.x==wi.x and w.y==wi.y:
                        wForward(w.x+1,w.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for wi in wights:
            if wCanDown(wi,wights,dragons,queen):
                x=wi.x+1
                y=wi.y+1
                s=str(x)+','+str(y)+"->Backward"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for w in wightsC:
                    if w.x==wi.x and w.y==wi.y:
                        wBackward(w.x+1,w.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)


        for wi in wights:
            if wCanLeft(wi,wights,dragons,queen):
                x=wi.x+1
                y=wi.y+1
                s=str(x)+','+str(y)+"->Left"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for w in wightsC:
                    if w.x==wi.x and w.y==wi.y:
                        wLeft(w.x+1,w.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)

        for wi in wights:
            if wCanRight(wi,wights,dragons,queen):
                x=wi.x+1
                y=wi.y+1
                s=str(x)+','+str(y)+"->Right"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for w in wightsC:
                    if w.x==wi.x and w.y==wi.y:
                        wRight(w.x+1,w.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)

        for wi in wights:
            if wCanTopLeft(wi,wights,dragons,queen):
                x=wi.x+1
                y=wi.y+1
                s=str(x)+','+str(y)+"->TopLeft"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for w in wightsC:
                    if w.x==wi.x and w.y==wi.y:
                        wForLeft(w.x+1,w.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)

        for wi in wights:
            if wCanTopRight(wi,wights,dragons,queen):
                x=wi.x+1
                y=wi.y+1
                s=str(x)+','+str(y)+"->TopRight"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for w in wightsC:
                    if w.x==wi.x and w.y==wi.y:
                        wForRight(w.x+1,w.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)

        for wi in wights:
            if wCanBotLeft(wi,wights,dragons,queen):
                x=wi.x+1
                y=wi.y+1
                s=str(x)+','+str(y)+"->BotLeft"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for w in wightsC:
                    if w.x==wi.x and w.y==wi.y:
                        wBackLeft(w.x+1,w.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for wi in wights:
            if wCanBotRight(wi,wights,dragons,queen):
                x=wi.x+1
                y=wi.y+1
                s=str(x)+','+str(y)+"->BotRight"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for w in wightsC:
                    if w.x==wi.x and w.y==wi.y:
                        wBackRight(w.x+1,w.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
    elif player==2:

        for di in dragons:
            if dCanDown(di,wights,dragons,queen):
                x=di.x+1
                y=di.y+1
                s=str(x)+','+str(y)+"->Down"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for d in dragonsC:
                    if d.x==di.x and d.y==di.y:
                        dDownward(d.x+1,d.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for di in dragons:
            if dCanBotLeft(di,wights,dragons,queen):
                x=di.x+1
                y=di.y+1
                s=str(x)+','+str(y)+"->BotLeft"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for d in dragonsC:
                    if d.x==di.x and d.y==di.y:
                        dDownLeft(d.x+1,d.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for di in dragons:
            if dCanBotRight(di,wights,dragons,queen):
                x=di.x+1
                y=di.y+1
                s=str(x)+','+str(y)+"->BotRight"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for d in dragonsC:
                    if d.x==di.x and d.y==di.y:
                        dDownRight(d.x+1,d.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for di in dragons:
            if dCanLeft(di,wights,dragons,queen):
                x=di.x+1
                y=di.y+1
                s=str(x)+','+str(y)+"->Left"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for d in dragonsC:
                    if d.x==di.x and d.y==di.y:
                        dLeft(d.x+1,d.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for di in dragons:
            if dCanRight(di,wights,dragons,queen):
                x=di.x+1
                y=di.y+1
                s=str(x)+','+str(y)+"->Right"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for d in dragonsC:
                    if d.x==di.x and d.y==di.y:
                        dRight(d.x+1,d.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for di in dragons:
            if dCanUp(di,wights,dragons,queen):
                x=di.x+1
                y=di.y+1
                s=str(x)+','+str(y)+"->Up"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for d in dragonsC:
                    if d.x==di.x and d.y==di.y:
                        dUpward(d.x+1,d.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for di in dragons:
            if dCanTopLeft(di,wights,dragons,queen):
                x=di.x+1
                y=di.y+1
                s=str(x)+','+str(y)+"->TopLeft"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for d in dragonsC:
                    if d.x==di.x and d.y==di.y:
                        dUpLeft(d.x+1,d.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for di in dragons:
            if dCanTopRight(di,wights,dragons,queen):
                x=di.x+1
                y=di.y+1
                s=str(x)+','+str(y)+"->TopRight"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for d in dragonsC:
                    if d.x==di.x and d.y==di.y:
                        dUpRight(d.x+1,d.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for qi in queen:
            if dCanDown(qi,wights,dragons,queen):

                x=qi.x+1
                y=qi.y+1
                s=str(x)+','+str(y)+"->Down"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for q in queenC:
                    if q.x==qi.x and q.y==qi.y:
                        dDownward(q.x+1,q.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for qi in queen:
            if dCanBotLeft(qi,wights,dragons,queen):
                x=qi.x+1
                y=qi.y+1
                s=str(x)+','+str(y)+"->BotLeft"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for q in queenC:
                    if q.x==qi.x and q.y==qi.y:
                        dDownLeft(q.x+1,q.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for qi in queen:
            if dCanBotRight(qi,wights,dragons,queen):
                x=qi.x+1
                y=qi.y+1
                s=str(x)+','+str(y)+"->BotRight"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for q in queenC:
                    if q.x==qi.x and q.y==qi.y:
                        dDownRight(q.x+1,q.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for qi in queen:
            if dCanLeft(qi,wights,dragons,queen):
                x=qi.x+1
                y=qi.y+1
                s=str(x)+','+str(y)+"->Left"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for q in queenC:
                    if q.x==qi.x and q.y==qi.y:
                        dLeft(q.x+1,q.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for qi in queen:
            if dCanRight(qi,wights,dragons,queen):
                x=qi.x+1
                y=qi.y+1
                s=str(x)+','+str(y)+"->Right"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for q in queenC:
                    if q.x==qi.x and q.y==qi.y:
                        dRight(q.x+1,q.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for qi in queen:
            if dCanUp(qi,wights,dragons,queen):
                x=qi.x+1
                y=qi.y+1
                s=str(x)+','+str(y)+"->Up"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for q in queenC:
                    if q.x==qi.x and q.y==qi.y:
                        dUpward(q.x+1,q.y+1,wightsC,dragonsC,queenC)

                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for qi in queen:
            if dCanTopLeft(qi,wights,dragons,queen):
                x=qi.x+1
                y=qi.y+1
                s=str(x)+','+str(y)+"->TopLeft"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for q in queenC:
                    if q.x==qi.x and q.y==qi.y:
                        dUpLeft(q.x+1,q.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)
        for qi in queen:
            if dCanTopRight(qi,wights,dragons,queen):
                x=qi.x+1
                y=qi.y+1
                s=str(x)+','+str(y)+"->TopRight"
                wightsC = copy.deepcopy(wights)
                dragonsC = copy.deepcopy(dragons)
                queenC = copy.deepcopy(queen)
                for q in queenC:
                    if q.x==qi.x and q.y==qi.y:
                        dUpRight(q.x+1,q.y+1,wightsC,dragonsC,queenC)
                possible.append(wightsC)
                possible.append(dragonsC)
                possible.append(queenC)
                possible.append(s)

    return possible


def printPossibleMoves(possible):
    for i in range(0, len(possible), 4):
        state=State()
        state.wights=possible[i]
        state.dragons=possible[i+1]
        state.queen=possible[i+2]
        printBoard(state)


def wCanUp(wight, w, d, q):
    piece = findPiece(wight.x - 1, wight.y, w, d, q)
    if piece == 1:
        return True
    else:
        return False

def wCanDown(wight, w, d, q):
    piece = findPiece(wight.x + 1, wight.y, w, d, q)
    if piece == 1:
        return True
    else:
        return False

def wCanLeft(wight, w, d, q):
    piece = findPiece(wight.x, wight.y - 1, w, d, q)
    if piece == 1:
        return True
    else:
        return False

def wCanRight(wight, w, d, q):
    piece = findPiece(wight.x, wight.y + 1, w, d, q)
    if piece == 1:
        return True
    else:
        return False

def wCanTopLeft(wight, w, d, q):
    piece = findPiece(wight.x - 1, wight.y - 1, w, d, q)
    if piece == 1 or piece == 0:
        return False
    elif piece.id == 'q' or piece.id == 'd':
        return True

def wCanTopRight(wight, w, d, q):
    piece = findPiece(wight.x - 1, wight.y + 1, w, d, q)
    if piece == 1 or piece == 0:
        return False
    elif piece.id == 'q' or piece.id == 'd':
            return True

def wCanBotLeft(wight, w, d, q):
    piece = findPiece(wight.x + 1, wight.y - 1, w, d, q)
    if piece == 1 or piece == 0:
        return False
    elif piece.id == 'q' or piece.id == 'd':
        return True

def wCanBotRight(wight, w, d, q):
    piece = findPiece(wight.x + 1, wight.y + 1, w, d, q)
    if piece == 1 or piece == 0:
        return False
    elif piece.id == 'q' or piece.id == 'd':
        return True

    '''
    movement for wights
    wights moving forward by move into the square on top of it
    '''

def wForward(i, j, w, d, q):
    global moved
    i = i - 1
    j = j - 1
    if i <= 0:
        print("W Can not move forward.")
        moved = False
        return
    if findPiece(i, j, w, d, q).id == 'w' and findPiece(i - 1, j, w, d, q) == 1:
        wight = findPiece(i, j, w, d, q)
        wight.x -= 1
        moved = True
    elif findPiece(i, j, w, d, q).id != 'w':
        print("No wight on", i + 1, ",", j + 1)
        moved = False
    elif findPiece(i - 1, j, w, d, q) != 1:
        print("Blocked by", findPiece(i - 1, j).id)
        moved = False

def wBackward(i, j, w, d, q):
    i = i - 1
    j = j - 1
    global moved
    if i >= 4:
        print("W Can not move backward.")
        moved = False
        return
    if findPiece(i, j, w, d, q).id == 'w' and findPiece(i + 1, j, w, d, q) == 1:
        wight = findPiece(i, j, w, d, q)
        wight.x += 1
        moved = True
    elif findPiece(i, j, w, d, q, ).id != 'w':
        print("No wight on", i + 1, ",", j + 1)
        moved = False
    elif findPiece(i + 1, j, w, d, q) != 1:
        print("Blocked by", findPiece(i + 1, j, w, d, q).id)
        moved = False

def wLeft(i, j, w, d, q):
    i = i - 1
    j = j - 1
    global moved
    if j <= 0:
        print("W Can not move left.")
        moved = False
        return
    if findPiece(i,j,w,d,q)==1 or findPiece(i,j,w,d,q)==0:
        print("No wights on", i,j)
        moved=False
    if findPiece(i, j, w, d, q).id == 'w' and findPiece(i, j - 1, w, d, q) == 1:
        wight = findPiece(i, j, w, d, q)
        wight.y -= 1
        moved = True
    elif findPiece(i, j, w, d, q).id != 'w':
        print("No wight on", i + 1, ",", j + 1)
        moved = False
    elif findPiece(i, j - 1, w, d, q) != 1:
        print("Blocked by", findPiece(i, j - 1, w, d, q).id)
        moved = False

def wRight(i, j, w, d, q):
    i = i - 1
    j = j - 1
    global moved
    if j >= 4:
        print("W Can not move right.")
        moved = False
        return
    if findPiece(i, j, w, d, q).id == 'w' and findPiece(i, j + 1, w, d, q) == 1:
        wight = findPiece(i, j, w, d, q)
        wight.y += 1
        moved = True
    elif findPiece(i, j, w, d, q).id != 'w':
        print("No wight on", i + 1, ",", j + 1)
        moved = False
    elif findPiece(i, j + 1, w, d, q) != 1:
        print("Blocked by", findPiece(i, j + 1, w, d, q).id)
        moved = False

def wForLeft(i, j, w, d, q):
    i = i - 1
    j = j - 1
    global moved
    if j<=0 or i <=0:
        print("W cannot move up left.")
        moved = False
        return
    if findPiece(i - 1, j - 1, w, d, q) == 1 or findPiece(i - 1, j - 1, w, d, q).id == 'w':
        print("Nothing to capture, move failed.")
        moved = False
    else:
        piece = findPiece(i - 1, j - 1, w, d, q)
        if piece.id == 'd':
            for da in d:
                if da.x == piece.x and da.y == piece.y:
                    d.remove(da)
        if piece.id == 'q':
            for qq in q:
                if qq.x == piece.x and qq.y == piece.y:
                    q.remove(qq)
        wight = findPiece(i, j, w, d, q)
        wight.x -= 1
        wight.y -= 1
        moved = True

def wForRight(i, j, w, d, q):
    i = i - 1
    j = j - 1
    global moved
    if j>=4 or i <=0:
        print("W cannot move up left.")
        moved = False
        return
    if findPiece(i - 1, j + 1, w, d, q) == 1 or findPiece(i-1,j+1,w,d,q)==0 or findPiece(i - 1, j + 1, w, d, q).id == 'w':
        print("Nothing to capture, move failed.")
        moved = False
    else:
        piece = findPiece(i - 1, j + 1, w, d, q)
        if piece.id == 'd':
            for da in d:
                if da.x == piece.x and da.y == piece.y:
                    d.remove(da)
        if piece.id == 'q':
            for qi in q:
                if qi.x == piece.x and qi.y == piece.y:
                    q.remove(qi)
        wight = findPiece(i, j, w, d, q)
        wight.x -= 1
        wight.y += 1
        moved = True

def wBackLeft(i, j, w, d, q):
    i = i - 1
    j = j - 1
    global moved
    if j<=0 or i >=4:
        print("W cannot move up left.")
        moved = False
        return
    if findPiece(i + 1, j - 1, w, d, q) == 1 or findPiece(i + 1, j - 1, w, d, q).id == 'w':
        print("Nothing to capture, move failed.")
        moved = False
    else:
        piece = findPiece(i + 1, j - 1, w, d, q)
        if piece.id == 'd':
            for da in d:
                if da.x == piece.x and da.y == piece.y:
                    d.remove(da)
        if piece.id == 'q':
            for qi in q:
                if qi.x == piece.x and qi.y == piece.y:
                    q.remove(qi)
        wight = findPiece(i, j, w, d, q)
        wight.x += 1
        wight.y -= 1
        moved = True

def wBackRight(i, j, w, d, q):
    i = i - 1
    j = j - 1
    global moved
    if j>=4 or i >=4:
        print("W cannot move up left.")
        moved = False
        return
    if findPiece(i + 1, j + 1, w, d, q) == 1 or findPiece(i + 1, j + 1, w, d, q).id == 'w':
        print("Nothing to capture, move failed.")
        moved = False
    else:
        piece = findPiece(i + 1, j + 1, w, d, q)
        if piece.id == 'd':
            for da in d:
                if da.x == piece.x and da.y == piece.y:
                    d.remove(da)
        if piece.id == 'q':
            for qi in q:
                if qi.x == piece.x and qi.y == piece.y:
                     q.remove(qi)
        wight = findPiece(i, j, w, d, q)
        wight.x += 1
        wight.y += 1
        moved = True

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
            if piece.id=='q':
                piece.setWorth()
        elif nextP.id == 'd' or nextP.id == 'q':
            print("Blocked by 1", nextP.id)
            moved = False
        elif nextP.id == 'w':
            w.remove(nextP)
            piece.x -= 1
            moved = True
            if piece.id=='q':
                piece.setWorth()

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
    if piece == 1 or piece == 0 or piece.id == 'w':
        print("No dragon/queen on", i + 1, ",", j + 1)
        moved = False
    elif (piece.id == 'd' or piece.id == 'q'):
        if nextP == 1:
            piece.x += 1
            moved = True
            if piece.id=='q':
                piece.setWorth()
        elif nextP.id == 'd' or nextP.id == 'q':
            print("Blocked by 2", nextP.id)
            moved = False
        elif nextP.id == 'w':
            w.remove(nextP)
            piece.x += 1
            moved = True
            if piece.id=='q':
                piece.setWorth()


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
            if piece.id=='q':
                piece.setWorth()
        elif nextP.id == 'd' or nextP.id == 'q':
            print("Blocked by 3", nextP.id)
            moved = False
        elif nextP.id == 'w':
            w.remove(nextP)
            piece.y -= 1
            moved = True
            if piece.id=='q':
                piece.setWorth()

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
            if piece.id=='q':
                piece.setWorth()
        elif nextP.id == 'd' or nextP.id == 'q':
            print("Blocked by 4", nextP.id)
            moved = False
        elif nextP.id == 'w':
            w.remove(nextP)
            piece.y += 1
            moved = True
            if piece.id=='q':
                piece.setWorth()

def dUpLeft(i, j, w, d, q):
    i = i - 1
    j = j - 1
    global moved
    if j <=0 or i<=0:
        print("Can not move up left.")
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
            if piece.id=='q':
                piece.setWorth()
        elif nextP == 0:
            print("Cannot move")
            moved=False
        elif nextP.id == 'd' or nextP.id == 'q':
            print("Blocked by5 ", nextP.id)
            moved = False
        elif nextP.id == 'w':
            w.remove(nextP)
            piece.x -= 1
            piece.y -= 1
            moved = True
            if piece.id=='q':
                piece.setWorth()

def dUpRight(i, j, w, d, q):
    i = i - 1
    j = j - 1
    global moved
    if j >= 4 or i<=0:
        print("Can not move up right.")
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
            if piece.id=='q':
                piece.setWorth()
        elif nextP.id == 'd' or nextP.id == 'q':
            print("Blocked by 6", nextP.id)
            moved = False
        elif nextP.id == 'w':
            w.remove(nextP)
            piece.x -= 1
            piece.y += 1
            moved = True
            if piece.id=='q':
                piece.setWorth()


def dDownLeft(i, j, w, d, q):
    i = i - 1
    j = j - 1
    global moved
    if j <= 0 or i >=4 :
        print("Can not move down left.")
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

            if piece.id=='q':
                piece.setWorth()
        elif nextP.id == 'd' or nextP.id == 'q':
            print("Blocked by 7", nextP.id)
            moved = False
        elif nextP.id == 'w':
            for wa in w:
                if wa.x == nextP.x and wa.y==nextP.y:
                    w.remove(wa)
            piece.x += 1
            piece.y -= 1
            moved = True
            if piece.id=='q':
                piece.setWorth()

def dDownRight(i, j, w, d, q):
    i = i - 1
    j = j - 1
    global moved
    if j >= 4 or i>=4:
        print("Can not move down right.")
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
            if piece.id=='q':
                piece.setWorth()
        elif nextP.id == 'd' or nextP.id == 'q':
            print("Blocked by 8", nextP.id)
            moved = False
        elif nextP.id == 'w':
            w.remove(nextP)
            piece.x += 1
            piece.y += 1
            moved = True
            if piece.id=='q':
                piece.setWorth()



def searchBestMoveW(states):
    best = -999
    bestState=0
    current=0
    for s in states:
        current=getScore(s)
        if best<current:
            best=current
            bestState=s
        elif best == current:
            if bool(random.getrandbits(1)):
                best = current
                bestState=s
    return bestState


def searchBestMoveQ(states):
    best = -9999
    bestState=0
    current=0
    for s in states:
        current=getScoreQ(s)
        if best<current:
            best=current
            bestState=s
        elif best == current:
            if bool(random.getrandbits(1)):
                best = current
                bestState=s
    return bestState


def transStates(possible):
    states = []
    for i in range(0,len(possible),4):
        state = State()
        state.wights=possible[i]
        state.dragons=possible[i+1]
        state.queen=possible[i+2]
        states.append(state)
    return states

'''
calculate total score of pieces current on board
'''
def getScore(state):
    wights=state.wights
    dragons=state.dragons
    queen=state.queen
    score=0
    for wi in wights:
        score+=wi.worth
    for di in dragons:
        score-=di.worth
    for q in queen:
        score-=q.worth
    return score

def getScoreQ(state):
    wights=state.wights
    dragons=state.dragons
    queen=state.queen
    score=0
    for wi in wights:
        score-=wi.worth
    for di in dragons:
        score+=di.worth
    for q in queen:
        score+=q.worth
    return score

def makeTree(state,player,depths):
    d=depths
    if depths==1:
        if player==1:
            possible=possibleMoves(state,1)
            states=transStates(possible)
            state=searchBestMoveW(states)
            return state
        elif player==2:
            possible=possibleMoves(state,2)
            states=transStates(possible)
            state=searchBestMoveQ(states)
            return state
    elif depths==2:
        tree = Node()
        tree.state = state

        possible = possibleMoves(state, 2)
        states = transStates(possible)
        for s in states:
            node = Node()
            node.state = s
            tree.addChild(node)
        high = -999
        bestMove = 0
        for i in range(len(tree.getChildrens())):
            s = tree.getChild(i).state
            s.estimate = getScoreQ(s)
            current = s.estimate
            if high < current:
                high = current
                bestMove = s
        return bestMove
    else:

        tree = Node()
        tree.state=state
        last=tree
        while depths>2:
            possible=possibleMoves(state,2)
            states=transStates(possible)
            for s in states:
                s.estimate=getScoreQ(s)
                node=Node()
                node.state=s
                last.addChild(node)
            if last==tree:
                for i in range(len(last.getChildrens())):
                    n=last.getChild(i)
                    possible=possibleMoves(last.getChild(i).state,1)
                    states1=transStates(possible)

                    for s1 in states1:
                        s1.estimate=getScore(s1)
                        print(s1.estimate)
                        node=Node()
                        node.state=s1
                        n.addChild(node)
            depths-=1
        if depths==2:
            '''
            DFS
            '''
            for i in range(len(tree.getChildrens())):
                best=-999
                for c in tree.getChild(i).childrens:
                    if c.estimate>best:
                        tree.getChild(i).estimate=c.estimate
                        print(tree.getChild(i).estimate)
                        best=c.estimate
            highest=-999
            bestMove=0
            for i in range(len(tree.getChildrens())):
                if tree.getChild(i).estimate>highest:
                    highest=tree.getChild(i).estimate
                    bestMove=tree.getChild(i).state
                elif tree.getChild(i).estimate==highest:
                    if bool(random.getrandbits(1)):
                        highest = tree.getChild(i).estimate
                        bestMove = tree.getChild(i).state
        return bestMove









def search(state,player,depths):
    if depths==1:
        if player==1:
            possible=possibleMoves(state,1)
            states=transStates(possible)
            state=searchBestMoveW(states)
            return state
        elif player==2:
            possible=possibleMoves(state,2)
            states=transStates(possible)
            state=searchBestMoveQ(states)
            return state
    else:
        if depths==2:
            theState = recurSearch(state,player)
        else:
            while depths != 2:
                theState = recurSearch(state, player)
                if player==1:
                    player=2
                else:
                    player=1
                depths-=1

        return theState

def recurSearch(state,player):
    if player == 1:
        possible = possibleMoves(state, 1)
        states = transStates(possible)
        currentBest = -999
        bestMove = 0
        for s in states:
            possible1 = possibleMoves(s, 2)
            states1 = transStates(possible1)
            state1 = searchBestMoveW(states1)
            score = getScore(state1)
            s.worth = score
            if currentBest < score:
                currentBest = score
                bestMove = s
            elif currentBest == score:
                if bool(random.getrandbits(1)):
                    bestMove = s
                    if len(bestMove.queen) == 0:
                        print("Wights' won!")
                        sys.exit(turns)
                    bestMove.queen[0].setWorth()
        return bestMove
    elif player == 2:
        possible = possibleMoves(state, 2)
        states = transStates(possible)
        currentBest = -999
        bestMove = 0
        for s in states:
            possible1 = possibleMoves(s, 1)
            states1 = transStates(possible1)
            state1 = searchBestMoveQ(states1)
            score = getScoreQ(state1)
            s.worth = score

            if currentBest < score:
                currentBest = score
                bestMove = s
            elif currentBest == score:
                if bool(random.getrandbits(1)):
                    bestMove = s
                    bestMove.queen[0].setWorth()
        return bestMove

print("Please enter the X,Y coordinates of piece and the direction you would like to move in order.")
print("Direction code:")
print("1: Forward                2: Backward                 3:Left                       4:Right   \n"
      "5:Forward-Left Diagonal   6:Forward-Right Diagonal    "
      "7: Backward-Left Diagonal    8: Backward-Right Diagonal")
while True:
    character = int(input("Please select your character: 1.Wights   2.Queen     3.None  4.Both"))
    if (character < 1 or character > 4):
        print("Character number must between 1-4")
        continue
    else:
        break
if character!=4 and character!=3:
    depth = int(input("Please enter the depths of AI search level: "))
if character == 3:
    depth = int(input("Please enter the depths of First AI search level: "))
print("----------------------Begin---------------------------")
board = createBoard()
wights = []
dragons = []
queen = []

wights,dragons,queen = getPos(board)
state=State()
state.wights=wights
state.dragons=dragons
state.queen=queen
printBoard(state)
turns = 0
moved = False
player = 1
repeat = 0

while turns < 50:
    '''
    check win
    '''

    if len(state.queen)==0:
        print("Wights Won!")
        print(turns)
        sys.exit()
    if (state.queen[0].x==5):
        print("Queen won!")
        print(turns)
        sys.exit()
    if len(state.wights)==0:
        print("Queen Won!")
        print(turns)
        sys.exit()
    if character == 4:
        if turns % 2 == 0:
            player = 1
            if wTurn(state):
                turns += 1
        elif turns % 2 == 1:
            player = 2
            if qTurn(state):
                turns += 1
    elif character == 2:
        if turns % 2 == 0:
            player = 1
            print("Wights' turn:")
            state = search(state, 1, depth)
            printBoard(state)
            turns += 1

        elif turns % 2 == 1:
            player = 2
            if qTurn(state):
                turns += 1
    elif character == 1:
        if turns % 2 == 0:
            player = 1
            if wTurn(state):
                turns += 1
        elif turns % 2 == 1:
            player = 2
            print("Queen's turn:")
            state = search(state, 2,depth)
            printBoard(state)
            turns += 1
    elif character == 3:

        if turns % 2 == 0:
            player = 1
            print("Wights' turn:")
            state = search(state,1,depth)
            printBoard(state)
            turns+=1

        elif turns % 2 == 1:
            player=2
            print("Queen's turn:")
            state = search(state,2,depth)
            printBoard(state)
            turns+=1

    if turns==50:
        print("50 TURNS, DRAW.")
