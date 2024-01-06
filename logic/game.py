from dependencies.graphics import *
from logic.player import *
from logic.structure import Map
import math

class Game():
    def __init__(self, px:int, py:int,rays:int, raySize:int, lockedRegion:int) -> None:
        self.__win = GraphWin("Rays", px, py)
        self.__map = Map(self.__win,px,py)
        self.player = Player()

        self.__map.buildRandomMap(lockedRegion)

        for k in range(rays):
            self.player.addRay(k*math.pi/(2*rays)-math.pi/4,raySize)


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


        if not self.player.canMove(self.__map):
            self.player.set_coords(prevPos)
            ok = False
        
        if ok:
            self.player.setDir(direct)

    def drawPlayer(self):
        self.rayRepo = []
        new_repr = self.player.representation()
        new_repr.draw(self.__win)
        
        for ray in self.player.getRays():
            new_radius = ray.getRadius()

            new_radius = min(ray.resizeRay(self.player,self.__map),ray.getRadius())

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
