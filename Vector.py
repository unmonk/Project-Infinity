__author__ = 'Scott'
__author__ = 'SIU920142021'
import math
import copy

#shitty vector from Gimpy
class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, addVec):
        self.x += addVec.x
        self.y += addVec.y

    def subtract(self, subVec):
        self.x -= subVec.x
        self.y -= subVec.y

    def multiply(self, multVec):
        self.x *= multVec
        self.y *= multVec

    def divide(self, divVec):
        if not divVec == 0:
            self.x /= divVec.x
            self.y /= divVec.y

    def magnitude(self):
        a = self.x**2
        b = self.y**2
        c = math.sqrt(a+b)
        return c

    def normalize(self):
        mag = self.magnitude()
        self.divide(mag)

    def angles(self, object):
        dx = object.x - self.x
        dy = object.y - self.y
        rad = math.atan2(-dy, dx)
        rad %= 2 * math.pi
        deg = math.degrees(rad)
        return (deg, rad)

    def get_vector(self):
        return (self.x, self.y)

    def copySelf(self):
        return copy.copy(self)