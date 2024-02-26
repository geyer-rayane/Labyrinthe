import math

class Graph:
  def __init__(self):
    self.adjacency = {}
    self.weights = {}
    
  def __str__(self):
    return "adjacency : " + str(self.adjacency) + ", weights : " + str(self.weights)

  def add_node(self, s):
    if s in self.adjacency:
      return
    self.adjacency[s] = set()

  def add_arc(self, arc, weight = 1):
    s1, s2 = arc
    self.add_node(s1)
    self.add_node(s2)
    self.weights[arc] = weight
    self.adjacency[s1].add(s2)
    
  def remove_arc(self, arc):
    if arc not in set.weights:
      return
    del self.weights[arc]
    s1, s2 = arc
    self.adjacency[s1].remove(s2)
    
  def remove_node(self, node):
    if node not in self.adjacency:
      return
    for other in self.adjancency:
      self.remove_arc( (node, other) )
      self.remove_arc( (other, node) )
    del self.adjancency[node]
      
  def nodes(self):
    return set(self.adjacency)
    
  def successors(self, node):
    return set(self.adjacency[node])
    
  def predecessors(self, node):
    return set(s for s in self.adjacency if s in self.adjacency[node])
    
  def arc_weight(self, arc):
    return self.weights[arc]
    
  def set_arc_weight(self, arc, weight):
    self.weights[arc] = weight


def extract_min(F, distances): 
    min_dst = math.inf 
    min_s = None  
    for s in F: 
        if distances[s] <= min_dst: 
            min_s = s 
            min_dst = distances[s] 
    F.remove(min_s) 
    return min_s 
  
