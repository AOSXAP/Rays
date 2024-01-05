from dependencies.graphics import *
from logic.player import *
from logic.structure import Map
import math

class Game():
    def __init__(self, px:int, py:int,rays:int,lockedRegion:int) -> None:
        self.__win = GraphWin("Rays", px, py)
        self.__map = Map(self.__win,px,py)
        self.player = Player()

        self.__map.buildRandomMap(lockedRegion)

        for k in range(rays):
            self.player.addRay(k*math.pi/(2*rays)-math.pi/4,500)


    def getKey(self):
        keyString = self.__win.checkKey()
        return keyString
    
    def movePlayer(self,direction):
        prevPos = self.player.coords()
        direct = 1
        ok = True

        if direction == 'Left':
            self.player.setX(self.player.coords().x - 10)
            direct = 3
        elif direction == 'Right':
            self.player.setX(self.player.coords().x + 10)
            direct = 1
        elif direction == 'Up':
            self.player.setY(self.player.coords(). y - 10)
            direct = 4
        elif direction == 'Down':
            self.player.setY(self.player.coords().y + 10)
            direct = 2

        for zone in self.__map.lockedZones:
            if self.player.intersects(zone):
                self.player.set_coords(prevPos)
                ok = False
                break
        
        if ok:
            self.player.setDir(direct)

    def drawPlayer(self):
        self.rayRepo = []
        new_repr = self.player.representation()
        new_repr.draw(self.__win)
        
        for ray in self.player.getRays():
            new_radius = ray.getRadius()
            
            for zone in self.__map.lockedZones:
                normalizedRadius = new_radius

                if self.player.getDir() == 1 and self.player.getX() < zone[1].getX():
                    normalizedRadius = ray.resizeRay(zone,self.player)
                if self.player.getDir() == 2 and self.player.getY() < zone[1].getY():
                    normalizedRadius = ray.resizeRay(zone,self.player)
                if self.player.getDir() == 3 and self.player.getX() > zone[0].getX():
                    normalizedRadius = ray.resizeRay(zone,self.player)
                if self.player.getDir() == 4 and self.player.getY() > zone[0].getY():
                    normalizedRadius = ray.resizeRay(zone,self.player)
                new_radius = min(normalizedRadius,new_radius)

            completeRay = ray.completeRay(self.player,new_radius)
            self.player.rayRepo.append(completeRay)

            completeRay.draw(self.__win)
        
        self.player.last_repr = new_repr

    def undrawPlayer(self):
        self.player.last_repr.undraw()

        for ray in self.player.rayRepo:
            ray.undraw()
        

    def updatePlayer(self):
        self.undrawPlayer()
        self.drawPlayer()
