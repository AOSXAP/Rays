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
        cosTheta = math.cos(theta)
        sinTheta = math.sin(theta)

        x = player.getX()
        y = player.getY()

        initX, initY = x, y

        zone0X, zone0Y = zone[0].getX(), zone[0].getY()
        zone1X, zone1Y = zone[1].getX(), zone[1].getY()

        for _ in range(1,self.__radius+1,5):
            x += 5 * cosTheta
            y += 5 * sinTheta

            if x > zone0X and y > zone0Y:
                if x < zone1X and y < zone1Y:
                    return math.sqrt((initX - x)**2 + (initY-y)**2)
                
        return new_radius
    
    def completeRay(self,player,radius):
        dir = player.getDir()
        theta = self.getThetaByDir(dir)

        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

        rayRepr = Line(player.coords(),Point(player.getX()+x,player.getY()+y))
        rayRepr.setFill("green")

        return rayRepr
