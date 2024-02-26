from maze import Maze
from hexagonalmaze import *

labyrinth = Maze(5, 5)
labyrinth.generatelabyrinth()
labyrinth.defindpath()
labyrinth.verticallabyrinth(0.5)
labyrinth.horizontallabyrinth(1)
labyrinth.drawlabyrinth()

labyrinthhex = Hexagonalmaze(5, 5)
labyrinthhex.generatelabyrinth()
labyrinthhex.defindpath()
labyrinthhex.drawhexlabyrinth()
