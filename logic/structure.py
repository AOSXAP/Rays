from dependencies.graphics import *
import random

class Map:
    structureColors = ['red','blue','purple','cyan','green']

    def __init__(self, win, px,py):
        self.__px = px
        self.__py = py
        self.__win = win

        self.__padding = 20
        self.lockedZones = []

        self.buildBorders()

    def buildBorders(self) -> None:
        #Description: Builds initial map borders based on the map padding

        #upper border
        self.lockedRegion(Point(0,0),Point(self.__px,self.__padding),"black")
        
        #lower border
        self.lockedRegion(Point(0,self.__py-self.__padding),Point(self.__px,self.__py),"black")

        #left border
        self.lockedRegion(Point(0,0),Point(self.__padding,self.__py),"black")

        #right border
        self.lockedRegion(Point(self.__px-self.__padding,0),Point(self.__px,self.__py),"black")


    def lockedRegion(self, StartPoint: Point, EndPoint: Point, color: str = "") -> None:
        '''
        Description: Builds a rectangle looking locked region
        Input:Point,Point,Str(optional)
        Output:None
        '''
        border = Rectangle(StartPoint, EndPoint)
        if not color:
            border.setFill(random.choice(self.structureColors))
        else:
            border.setFill(color)

        border.draw(self.__win)

        self.lockedZones.append([StartPoint,EndPoint])
    
    def demoMap(self):
        #Description: demo map, used for testing
        self.lockedRegion(Point(70,150),Point(280,180))

        self.lockedRegion(Point(123,90),Point(300,200))

        self.lockedRegion(Point(223,330),Point(340,530))

        self.lockedRegion(Point(380,90),Point(550,530))

    def buildRandomMap(self, regionsNumber:int) -> None:
        '''
        Description: Based on regionNumber, it will generate multiple locked regions
        Input: int
        Output: None
        '''
        startX = self.__px // regionsNumber
        startY = self.__px // regionsNumber

        for _ in range(1,regionsNumber):
            x = random.randint(50, self.__px)
            y = random.randint(50, self.__py)

            sizeX = random.randint(2*startX,4*startX)
            sizeY = random.randint(2*startY,4*startY)

            self.lockedRegion(Point(x,y),Point(x+sizeX,y+sizeY))
