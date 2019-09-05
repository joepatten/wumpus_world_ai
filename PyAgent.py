# PyAgent.py
import random
import time
import Action
import Orientation

#todo: make class to keep track of orientation, and where agent is and where they have been.
#matrix

#return to beginning and climb (if have gold)
class Py_Agent:
    def __init__(self):
        self.has_gold = False
        self.has_arrow = True
        self.orient = 0
        self.position = [1,1]
        self.orientations = ['RIGHT', 'UP', 'LEFT', 'DOWN']

    def shoot_arrow(self):
        self.has_arrow = False

    def turn_left(self):
        self.orient = (self.orient + 1)%4

    def turn_right(self):
        self.orient = (self.orient - 1)%4

    def go_forward(self, bump=False):
        orientation = self.orientations[self.orient]
        print('ORIENTATIONksdjfsdkjfhskdf: ',orientation)
        if bump == True:
            offset = -1
        else:
            offset = 1
        if orientation == 'RIGHT':
            self.position[0] += 1*offset
        if orientation == 'LEFT':
            self.position[0] -= 1*offset
        if orientation == 'UP':
            self.position[1] += 1*offset
        if orientation == 'DOWN':
            self.position[1] -= 1*offset



#actions found in agent.cc
pa = Py_Agent()

def PyAgent_Constructor ():
    print("PyAgent_Constructor")


def PyAgent_Destructor ():
    print("PyAgent_Destructor")

def PyAgent_Initialize ():
    print("PyAgent_Initialize")
    pa = Py_Agent()

def PyAgent_Process (stench,breeze,glitter,bump,scream):
    #time.sleep(.5)
    perceptStr = ""
    if (stench == 1):
        perceptStr += "Stench=True,"
        if pa.has_arrow == True:
            pa.shoot_arrow()
            return Action.SHOOT
    else:
        perceptStr += "Stench=False,"
    if (breeze == 1):
        perceptStr += "Breeze=True,"
    else:
        perceptStr += "Breeze=False,"
    if (glitter == 1):
        perceptStr += "Glitter=True,"
        return Action.GRAB
    else:
        perceptStr += "Glitter=False,"
    if (bump == 1):
        perceptStr += "Bump=True,"
        pa.go_forward(bump)
        random_draw = random.random()
        if random_draw > .5:
            pa.turn_left()
            return Action.TURNLEFT
        else:
            pa.turn_right()
            return Action.TURNRIGHT
    else:
        perceptStr += "Bump=False,"
    if (scream == 1):
        perceptStr += "Scream=True"
    else:
        perceptStr += "Scream=False"
    if pa.has_gold and pa.position == [1,1]:
        return Action.CLIMB
    print("PyAgent_Process(from python): " + perceptStr)
    
    return Action.GOFORWARD

def PyAgent_GameOver (score):
    print("PyAgent_GameOver: score = " + str(score))
    print('Agent is at {}'.format(pa.position))
    print('Orientation is {}'.format(pa.orientations[pa.orient]))
