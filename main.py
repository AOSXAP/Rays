from logic.structure import *
from logic.player import *
from logic.game import *

displayX,displayY = 700,700
rays = 30
lockedRegions = 80

game = Game(displayX,displayY,rays,lockedRegions)

while True:
    key = game.getKey()

    if key != "":
        coords = game.player.coords()
        game.movePlayer(key)
        game.updatePlayer()
