''''
    Class: Node. Make each state a node, each node has a field state, has a list of children, one parent and a estimate value.
    Node class methods:
    addChild() add a child node and set the child node’s parent to self
    isLeaf() check if current node is a leaf node
    wSetESTFromChild()	find the maximum value from its children and set estimate value
    qSetESTFromChild()	find the maximum value from its children and set estimate value
    getChild(i) return the child node that is ith in the list
    numChild() return the length of children
    getParent()	return its parent node
    getChildrens()	return the children list
    setParent(parent)	set the parent of current node
    setState(state)	set the state of current node'''



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
class Node:
    def __init__(self):
        self.state=0
        self.childrens = []
        self.parent= None
        self.estimate=-999

    def hasChild(self,i):
        if i > len(self.childrens):
            return False
        else:
            return True
    def addChild(self,child):
        child.setParent(self)
        self.childrens.append(child)

    def isLeaf(self):
        if len(self.childrens)==0:
            return True
        else:
            return False
    def wSetESTFromChild(self):
        best=-999
        for c in self.childrens:
            if best<getScore(c.state):
                best=getScore(c.state)
        self.estimate=best

    def qSetESTFromChild(self):
        best=-999
        for c in self.childrens:
            if best<getScore(c.state):
                best=getScore(c.state)
        self.estimate=best
    def getChild(self,i):
        return self.childrens[i]

    def numChild(self):
        return len(self.childrens)

    def getParent(self):
        return self.parent

    def getChildrens(self):
        return self.childrens

    def setParent(self,parent):
        self.parent=parent

    def setState(self,state):
        self.state=state

