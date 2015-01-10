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
            return L()
        if key == "right":
            return R()
        if key == "straight":
            return F()
        if key == "backwards":
            return B()
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
        return 100

    def getRight(self):
        return 100


class FL(State):
    def press(self, key):
        return Stop()

    def release(self, key):
        if key == "left":
            return F()
        if key == "straight":
            return L()
        return Stop()

    def getLeft(self):
        return 50

    def getRight(self):
        return 100


class FR(State):
    def press(self, key):
        return Stop()

    def release(self, key):
        if key == "right":
            return F()
        if key == "straight":
            return R()
        return Stop()

    def getLeft(self):
        return 100

    def getRight(self):
        return 50


class R(State):
    def press(self, key):
        if key == "straight":
            return FR()
        if key == "backwards":
            return BR()
        return Stop()

    def release(self, key):
        return Stop()

    def getLeft(self):
        return 50

    def getRight(self):
        return 0


class L(State):
    def press(self, key):
        if key == "straight":
            return FL()
        if key == "backwards":
            return BL()
        return Stop()

    def release(self, key):
        return Stop()

    def getLeft(self):
        return 0

    def getRight(self):
        return 50

class B(State):
    def press(self, key):
        if key == "left":
            return BL()
        if key == "right":
            return BR()
        return Stop()

    def release(self, key):
        if key == "left":
            return B()
        if key == "right":
            return B()
        return Stop()

    def getLeft(self):
        return -100

    def getRight(self):
        return -100

class BL(State):
    def press(self, key):
        return Stop()

    def release(self, key):
        if key == "left":
            return B()
        return Stop()

    def getLeft(self):
        return -50

    def getRight(self):
        return -100

class BR(State):
    def press(self, key):
        return Stop()

    def release(self, key):
        if key == "right":
            return B()
        return Stop()

    def getLeft(self):
        return -100

    def getRight(self):
        return -50
