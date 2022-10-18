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

    def __init__(self, size):
        self.domino = []

        for top in range(0, size + 1):
            for bottom in range(top, size + 1):

                top_side = Side(Pips(top))
                bottom_side = Side(Pips(bottom))
                new_domino = Domino(top_side, bottom_side)
                self.add(new_domino)
                print("created: ", top, bottom)

    def add(self, domino):
        self.domino.append(domino)

set = Set(6)
