from dependencies.graphics import *
import math

class Ray:
    def __init__(self,theta,radius) -> None:
        self.__theta = theta
        self.__radius = radius

    def getRadius(self):
        return self.__radius
    
    def setRadius(self,radius):
        self.__radius = radius

    def getTheta(self):
        return self.__theta
    
    def setTheta(self,theta):
        self.__theta = theta

    def getThetaByDir(self,dir):
        theta = self.__theta

        if dir == 2:
            theta += math.pi/2
        elif dir == 3:
            theta += math.pi
        elif dir == 4:
            theta -= math.pi/2

        return theta

    def resizeRay(self,zone,player):
        new_radius = self.__radius

        theta = self.getThetaByDir(player.getDir())

        for r in range(self.__radius+1):
            x = player.getX() + r * math.cos(theta)
            y = player.getY() + r * math.sin(theta)

            if x > zone[0].getX() and y > zone[0].getY():
                if x < zone[1].getX() and y < zone[1].getY():
                    return r-1
        return new_radius
    
    def completeRay(self,player,radius):
        dir = player.getDir()
        theta = self.getThetaByDir(dir)

        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

        rayRepr = Line(player.coords(),Point(player.getX()+x,player.getY()+y))
        rayRepr.setFill("green")

        return rayRepr
