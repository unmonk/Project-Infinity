__author__ = 'Scott'
import pygame
from Vectors import *
from Constants import *

def getDepth(objA, objB):

    #half sizes of objects
    halfWidA = objA.width / 2
    halfHtA = objA.height / 2
    halfWidB = objB.width / 2
    halfHtB = objB.height / 2

    #centers
    centerA = Vectors(objA.left + halfWidA, objA.top + halfHtA)
    centerB = Vectors(objB.left + halfWidB, objB.top + halfHtB)

    #calculate minimim intersecting distances
    distanceX = centerA.x - centerB.x
    distanceY = centerA.y - centerA.y

    minX = halfWidA + halfWidB
    minY = halfHtA +  halfHtB

    if distanceX >= minX and distanceY >= minY:
        return Vectors(0, 0)




