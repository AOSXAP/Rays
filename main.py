from logic.structure import *
from logic.game import *

displayX,displayY,rays,lockedRegions = 700,700,30,30
game = Game(displayX,displayY,rays,lockedRegions)

while True:
    key = game.getKey()

    if key != "":
        coords = game.player.coords()
        game.movePlayer(key)
        game.updatePlayer()
