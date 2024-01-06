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

    def intersectsZone(self, x,y, zone0X,zone0Y,zone1X,zone1Y):
        if x > zone0X and y > zone0Y:
            if x < zone1X and y < zone1Y:
                return True
                
        return False
        
    def resizeRay(self, zone: [Point,Point], player) -> float:
        '''
        Description: Resizes a ray by checking if it hits any locked regions and reducing its radius(if that's the case)
        Input: [Point,Point], Player
        Output: float
        '''
        new_radius = self.__radius

        theta = self.getThetaByDir(player.getDir())
        cosTheta = math.cos(theta)
        sinTheta = math.sin(theta)

        x = player.getX()
        y = player.getY()

        initX, initY = x, y

        zone0X, zone0Y = zone[0].getX(), zone[0].getY()
        zone1X, zone1Y = zone[1].getX(), zone[1].getY()

        step = 4

        for _ in range(1,self.__radius+1,step):
            x += step * cosTheta
            y += step * sinTheta

            if self.intersectsZone(x,y,zone0X,zone0Y,zone1X,zone1Y):
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