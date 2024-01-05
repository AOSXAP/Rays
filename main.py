from logic.structure import *
from logic.game import *

game = Game(700,700)

while True:
    key = game.getKey()

    if key != "":
        coords = game.player.coords()
        game.movePlayer(key)
        game.updatePlayer()
