'''
    Class: State. Has field wights, dragons, queen, and estimate.
    I consider the current pieces on the board as a state, list of wights, dragons and queen construct a state. Each state has a estimate value
    to keep record of minimax value.'''

class State:
    def __init__(self):
        self.wights = 0
        self.dragons = 0
        self.queen = 0
        self.estimate = 0
