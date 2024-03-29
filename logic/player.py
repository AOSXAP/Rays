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

    def intersects(self,zone):
        '''
        Description: checks if player is in a zone
        '''
        for i in [-1,1]:
            for j in [-1,1]:
                if self.__x + i * self.__size > zone[0].getX() and self.__y + j * self.__size > zone[0].getY():
                    if self.__x + i * self.__size < zone[1].getX() and self.__y + j * self.__size < zone[1].getY():
                        return True
                                
        return False
    
    def canMove(self, map):
        mapGrid = map.getGrid()

        for radius in range(-self.__size//2,self.__size//2):
            if mapGrid[int(self.__x)+radius][int(self.__y)] == 1:
                return False
            
            if mapGrid[int(self.__x)][int(self.__y)+radius] == 1:
                return False
            
        return True

