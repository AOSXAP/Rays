from dependencies.graphics import *
from logic.ray import Ray
import math

class Player:
    def __init__(self) -> None:
        self.__size = 10

        self.__x = 30 + self.__size
        self.__y = 30 + self.__size
        
        # 1 = right , 2 = down, 3 = left , 4 = up
        self.__dir = 1 

        self.__rays = []
        self.rayRepo = []

        self.last_repr = self.representation()

    def getX(self):
        return self.__x
    
    def setX(self,x):
        self.__x = x

    def getY(self):
        return self.__y
    
    def setY(self,y):
        self.__y = y

    def getDir(self):
        return self.__dir
    
    def setDir(self, direction):
        self.__dir = direction

    def coords(self):
        return Point(self.__x,self.__y)
    
    def set_coords(self,coords:Point):
        self.__x = coords.x
        self.__y = coords.y
    
    def representation(self):
        return Circle(self.coords(), self.__size)
    
    def getRays(self):
        return self.__rays
    
    def addRay(self,theta,radius):
        ray = Ray(theta,radius)
        self.__rays.append(ray)

    def completeRay(self,ray,radius,dir):
        theta = ray.getTheta()

        if dir == 2:
            theta += math.pi/2
        if dir == 3:
            theta += math.pi
        if dir == 4:
            theta -= math.pi/2

        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

        aLine = Line(self.coords(),Point(self.__x+x,self.__y+y))
        aLine.setFill("green")

        return aLine
    
    def intersects(self,zone):
        for i in [-1,1]:
            for j in [-1,1]:
                if self.__x + i * self.__size > zone[0].getX() and self.__y + j * self.__size > zone[0].getY():
                    if self.__x + i * self.__size < zone[1].getX() and self.__y + j * self.__size < zone[1].getY():
                        return True
                                
        return False

