from logic.structure import *
from logic.player import *
from logic.game import *

displayX,displayY = 1000,700

rays = 50
raySize = 600

lockedRegions = 50

game = Game(displayX,displayY,rays,raySize,lockedRegions)

while True:
    key = game.getKey()

    if key != "":
        coords = game.player.coords()
        game.movePlayer(key)
        game.updatePlayer()
