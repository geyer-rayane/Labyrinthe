from graph import *
from render import * 
from coveringtree import *
import random

class Maze(): 
    
    def __init__(self, width, height) :
        
        self.width = width
        self.height = height
        self.mazegrid = self.randomrepresentlabyrinth(width, height)
        self.path = []
        
    def representlabyrinth (self, width, height) : 
        # l'idée de generer notre graphe selon les quatres directions
        # haut, bas, gauche et droite. Pour assurer le voisinage décrit naturellement par les labyrintes 
        # et si il existe un lien entre (a,b), il en est aussi pour (b,a) en gardant le meme poids
        # cette methode revoie le graphe generation. qu'on va passer a notre grille dans le constructeur.
        graph = Graph()
        for x in range(width) : 
            for y in range(height) : 
                if y > 0 : 
                    down_link_direct = ((x,y),(x, y - 1))
                    down_link_reciprocal = ((x, y - 1),(x,y))
                    graph.add_arc(down_link_direct, weight = 1)
                    graph.add_arc(down_link_reciprocal, weight = 1)
                if y < height - 1 : 
                    up_link_direct = ((x,y),(x, y + 1))
                    up_link_reciprocal = ((x, y + 1),(x,y))
                    graph.add_arc(up_link_direct, weight = 1)
                    graph.add_arc(up_link_reciprocal, weight = 1)
                if x > 0 : 
                    left_link_direct = ((x,y),(x - 1, y))
                    left_link_reciprocal = ((x - 1, y),(x,y))
                    graph.add_arc(left_link_direct,weight = 1)
                    graph.add_arc(left_link_reciprocal,weight = 1)
                if x < width - 1 : 
                    right_link_direct = ((x,y),(x + 1, y))
                    right_link_reciprocal = ((x + 1,y),(x,y))
                    graph.add_arc(right_link_direct, weight = 1)
                    graph.add_arc(right_link_reciprocal, weight = 1)
               
        return graph
    
    def showgraph (self, draw_coordinates) : 
        # cette methode est décrite dans le mondule render.
        draw_tree(self.mazegrid)
        
    def drawlabyrinth (self) : 
        # cette methode est décrite dans le mondule render.
        draw_square_maze(self.mazegrid, self.path, draw_coordinates = False)
    
    def randomrepresentlabyrinth(self, width, height) : 
        # pareil comme la methode 'representlabyrinth' mais cette fois on va utiliser un poids aleatoire.
        # en utilisant random et la methode random.uniform.
        # une variable reçoit random.uniform(0,1), une valeur aleatoire entre 0 et 1
        # tout en assurant que le meme poids existe entre (a,b) et (b,a)
        graph = Graph()
        for x in range(width) : 
            for y in range(height) : 
                if y > 0 : 
                    down_link_direct = ((x,y),(x, y - 1))
                    down_link_reciprocal = ((x, y - 1),(x,y))
                    weight = random.uniform(0, 1)
                    graph.add_arc(down_link_direct, weight)
                    graph.add_arc(down_link_reciprocal, weight)
                if y < height - 1 : 
                    up_link_direct = ((x,y),(x, y + 1))
                    up_link_reciprocal = ((x, y + 1),(x,y))
                    weight = random.uniform(0, 1)
                    graph.add_arc(up_link_direct, weight)
                    graph.add_arc(up_link_reciprocal,weight)
                if x > 0 : 
                    left_link_direct = ((x,y),(x - 1, y))
                    left_link_reciprocal = ((x - 1, y),(x,y))
                    weight = random.uniform(0, 1)
                    graph.add_arc(left_link_direct,weight)
                    graph.add_arc(left_link_reciprocal,weight)
                if x < width - 1 : 
                    right_link_direct = ((x,y),(x + 1, y))
                    right_link_reciprocal = ((x + 1,y),(x,y))
                    weight = random.uniform(0, 1)
                    graph.add_arc(right_link_direct, weight)
                    graph.add_arc(right_link_reciprocal, weight)
        
        return graph
    
    def generatelabyrinth (self) : 
        # tree recoit le resultat de l'algorithme prim
        # on cree un graph vide 'maze' avec la classe Graph
        # en utilisant prim, on a remarqué que parfois il existe des valeurs None, donc on a ajouté une condition 
        # que node et les voisins de node ne sont pas None
        # Puis on a assurer que notre graphe n'est pas orienté
        # et on a redefini self.mazegrid avec ce qu'on a obtenu comme graphe.
        tree = prim_algorithm(self.mazegrid)
        maze = Graph()
        for node in tree.keys() : 
            if node is not None and tree[node] is not None : 
                maze.add_arc((node,tree[node]))
                maze.add_arc((tree[node], node))
        
        self.mazegrid = maze
    
    def dfspath(self, current, objective) : 
        
        temp = [[current]]
        visited = []
        
        while temp : 
            path = temp.pop(0)
            node = path[-1]
            if node == objective : 
                return path 
            for neighbor in self.mazegrid.successors(node) : 
                if neighbor not in visited : 
                    newpath = path + [neighbor]
                    temp.insert(0, newpath)
                    visited.append(neighbor)
    
    def defindpath(self) : 
        current = (0,0)
        objective = (self.width - 1, self.height - 1)
        self.path = self.dfspath(current, objective)
        
    def verticallabyrinth (self, distortion) : 
        self.generatelabyrinth()
        for node in self.mazegrid.nodes(): 
            for neighbor in self.mazegrid.successors(node) : 
                if node[0] == neighbor[0] and node[1] != neighbor[1] : 
                    self.mazegrid.set_arc_weight((node, neighbor), self.mazegrid.arc_weight((node, neighbor)) + distortion)
                                                 
    def horizontallabyrinth (self, distortion) : 
        self.generatelabyrinth()
        for node in self.mazegrid.nodes():
            for neighbor in self.mazegrid.successors(node) : 
                if node[0] != neighbor[0] and node[1] == neighbor[1] :
                    self.mazegrid.set_arc_weight((node, neighbor), self.mazegrid.arc_weight((node, neighbor)) + distortion)
    
    
