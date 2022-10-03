class Pips:
    count = None

    def __init__(self, number):
        self.count = number

class Side:
    pips = None

    def __init__(self, pip_value):
        self.pips = pip_value

class Domino:
    top = None
    bottom = None

    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

class Set:
    domino = None

    def __init__(self):
        self.domino = []

    def add(self, domino):
        self.domino.append(domino)
