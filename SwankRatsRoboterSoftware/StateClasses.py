__author__ = 'Johannes'

class State:

    def press(self, key):
        return Stop()
    def release(self, key):
        return Stop()

    def getLeft(self):
        return 0

    def getRight(self):
        return 0

class Stop(State):
    def press(self, key):
        if key == "left":
            return  L()
        if key == "right":
            return R()
        if key == "straight":
            return  F()
        return Stop()

    def release(self, key):
        return Stop()

class F(State):
    def press(self, key):
        if key == "left":
            return FL()
        if key == "right":
            return FR()
        return Stop()

    def release(self, key):
        return Stop()

    def getLeft(self):
        return 60

    def getRight(self):
        return 60


class FL(State):
    def press(self, key):
        return  Stop()

    def release(self, key):
        if key == "left":
            return  F()
        if key == "straight":
            return  L()
        return Stop()

    def getLeft(self):
        return 30

    def getRight(self):
        return 60

class FR(State):
    def press(self, key):
        return Stop()

    def release(self, key):
        if key == "right":
            return F()
        if key == "straight":
            return  R()
        return Stop()

    def getLeft(self):
        return 60

    def getRight(self):
        return 30

class R(State):
    def press(self, key):
        if key == "straight":
            return  FR()
        return  Stop()

    def release(self, key):
        return Stop()

    def getLeft(self):
        return 30

    def getRight(self):
        return 0

class L(State):
    def press(self, key):
        if key == "straight":
            return  FL()
        return Stop()

    def release(self, key):
        return Stop()

    def getLeft(self):
        return 0

    def getRight(self):
        return 30