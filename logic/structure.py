from dependencies.graphics import *
import random

class Map:
    def __init__(self, win, px,py):
        self.__px = px
        self.__py = py
        self.__win = win

        self.__padding = 20
        self.lockedZones = []

        self.buildBorders()

    def buildBorders(self):
        #upper border
        self.lockedRegion(Point(0,0),Point(self.__px,self.__padding))
        
        #lower border
        self.lockedRegion(Point(0,self.__py-self.__padding),Point(self.__px,self.__py))

        #left border
        self.lockedRegion(Point(0,0),Point(self.__padding,self.__py))

        #right border
        self.lockedRegion(Point(self.__px-self.__padding,0),Point(self.__px,self.__py))


    def lockedRegion(self, StartPoint: Point, EndPoint: Point):
        border = Rectangle(StartPoint, EndPoint)
        border.setFill("black")
        border.draw(self.__win)

        self.lockedZones.append([StartPoint,EndPoint])
    
    def demoMap(self):
        self.lockedRegion(Point(70,150),Point(280,180))

        self.lockedRegion(Point(123,90),Point(300,200))

        self.lockedRegion(Point(223,330),Point(340,530))

        self.lockedRegion(Point(380,90),Point(550,530))

    def buildRandomMap(self, regionsNumber):
        startX = self.__px // regionsNumber
        startY = self.__px // regionsNumber

        for _ in range(1,regionsNumber):
            x = random.randint(50, self.__px)
            y = random.randint(50, self.__py)

            sizeX = random.randint(2*startX,4*startX)
            sizeY = random.randint(2*startY,4*startY)

            self.lockedRegion(Point(x,y),Point(x+sizeX,y+sizeY))
