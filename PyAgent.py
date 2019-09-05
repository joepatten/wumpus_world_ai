# PyAgent.py
import random
import Action
import Orientation


class Py_Agent:
    def __init__(self):
        self.step = 0
        self.has_gold = False
        self.has_arrow = True
        self.orient = 0
        self.location = [1, 1]
        self.orientations = ['RIGHT', 'UP', 'LEFT', 'DOWN']
        self.go_forward = False

    def get_location(self):
        return self.location

    def get_orientation(self):
        return self.orientations[self.orient]

    def shoot_arrow(self):
        self.has_arrow = False

    def turn_left(self):
        self.orient = (self.orient + 1) % 4

    def turn_right(self):
        self.orient = (self.orient - 1) % 4

    def grab_gold(self):
        self.has_gold = True

    def should_climb(self):
        return pa.has_gold and pa.location == [1, 1]

    def update_location(self, bump):
        orientation = self.get_orientation()
        if bump != 1:
            if orientation == 'RIGHT':
                self.location[0] += 1
            if orientation == 'LEFT':
                self.location[0] -= 1
            if orientation == 'UP':
                self.location[1] += 1
            if orientation == 'DOWN':
                self.location[1] -= 1
        self.go_forward = False


pa = Py_Agent()


def PyAgent_Constructor():
    print("PyAgent_Constructor")


def PyAgent_Destructor():
    print("PyAgent_Destructor")


def PyAgent_Initialize():
    print("PyAgent_Initialize")


def PyAgent_Process(stench, breeze, glitter, bump, scream):
    # 4) Update location if you have gone forward in last turn
    if pa.go_forward:
        pa.update_location(bump)

    # 3a) Grab gold if see glitter
    if (glitter == 1):
        pa.grab_gold()
        return Action.GRAB

    # 3b) Climb out if at location [1, 1] and have gold
    if pa.should_climb:
        Action.CLIMB

    # 3c) Shoot arrow if smell stench and if have arrow
    if (stench == 1):
        if pa.has_arrow:
            pa.shoot_arrow()
            return Action.SHOOT

    # 3d) If bump into wall, randomly turn right or left
    if (bump == 1):
        random_draw = random.random()
        if random_draw > .5:
            pa.turn_left()
            return Action.TURNLEFT
        else:
            pa.turn_right()
            return Action.TURNRIGHT

    # 3e) Else, go forward
    pa.go_forward = True
    return Action.GOFORWARD


def PyAgent_GameOver(score):
    print("PyAgent_GameOver: score = " + str(score))
