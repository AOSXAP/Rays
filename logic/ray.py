from dependencies.graphics import *
from logic.player import *
import math

class Ray:
    def __init__(self, theta:float, radius:int) -> None:
        #theta is the angle of the ray
        self.__theta = theta

        #radius is the absolute length of the ray
        self.__radius = radius

    def getRadius(self):
        return self.__radius
    
    def setRadius(self,radius):
        self.__radius = radius

    def getTheta(self):
        return self.__theta
    
    def setTheta(self,theta):
        self.__theta = theta

    def getThetaByDir(self, dir:int) -> float:
        '''
        Description: Modify the theta angle based on the direction of the player
        Input: int
        Output: float
        '''
        theta = self.__theta

        if dir == 2:
            theta += math.pi/2
        elif dir == 3:
            theta += math.pi
        elif dir == 4:
            theta -= math.pi/2

        return theta
        
    def resizeRay(self, player, map) -> float:
        '''
        Description: Resizes a ray by checking if it hits any locked regions and reducing its radius(if that's the case)
        Input: Player, Map
        Output: float
        '''
        new_radius = self.__radius

        theta = self.getThetaByDir(player.getDir())
        cosTheta = math.cos(theta)
        sinTheta = math.sin(theta)

        x = player.getX()
        y = player.getY()

        initX, initY = x, y

        mapGrid = map.getGrid()

        step = 3

        for _ in range(1,self.__radius+1,step):
            x += step * cosTheta
            y += step * sinTheta

            if x > map.getPx() or y > map.getPy():
                break

            if x < 0 or y < 0:
                break

            if mapGrid[int(x)][int(y)] == 1:
                return math.sqrt((initX - x)**2 + (initY-y)**2)
                
        return new_radius
    
    def completeRay(self, player, radius: float) -> Line:
        '''
        Description: Build the representation of a ray
        Input: Player, float
        Output: Line
        '''

        dir = player.getDir()
        theta = self.getThetaByDir(dir)

        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

        rayRepr = Line(player.coords(),Point(player.getX()+x,player.getY()+y))
        rayRepr.setFill("black")

        return rayRepr