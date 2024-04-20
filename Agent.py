from random import random as RandFloat
from numpy import random as RandNorm
from math import radians, sin, cos

class Agent:
    def __init__(self, target):
        self.x = RandFloat()*100
        self.y = RandFloat()*100
        self.direction = RandFloat()*360
        self.velocity = abs(RandNorm.normal()*5)
        self.target = target
        self.alive = True
        self.tags = 0

    def tagged(self):
        self.alive = False

    def tag(self):
        self.tags += 1

    def move(self, rotation, distance):
        self.direction += rotation
        rads = radians(self.direction)
        self.x += cos(rads)*distance
        self.x = (self.x)%100
        self.y += sin(rads)*distance
        self.y = (self.y)%100

    def changeVelocity(self, velocity):
        self.velocity = velocity

    def updateTarget(self, target):
        self.target = target
