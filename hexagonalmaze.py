from maze import Maze
from graph import Graph 
from render import draw_hex_maze

class Hexagonalmaze(Maze) : 
    
    def __init__(self, width, height):
        super().__init__(width, height)
    
    def drawhexlabyrinth(self) : 
        draw_hex_maze(self.mazegrid, self.path, draw_coordinates = False)


    
