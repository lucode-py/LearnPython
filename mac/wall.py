from ursina import *

class wall:
    def __init__(self):
        self.Zpos = 5
        self.Xpos = 5
        self.compter = 0
        for self.i in range(100):
            self.compter+=1
            Entity(model="cube", collider="box", z=self.Zpos, x=self.Xpos, texture="grass")
            self.Zpos -= 1
            if self.compter == 10:
                self.compter = 0
                self.Xpos -= 1
                self.Zpos = 5

