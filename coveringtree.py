import math
from graph import *

def prim_algorithm (mazegraph):
    distances = {}
    parents   = {}
    for v in mazegraph.nodes() : 
        distances[v] = math.inf
        parents[v] = None      
    F = mazegraph.nodes()
    while ( len(F) != 0 ) : 
        u = extract_min(F, distances)
        for v in mazegraph.successors(u):
            if v in F and mazegraph.arc_weight( (u, v) ) < distances[v] : 
                distances[v] = mazegraph.arc_weight( (u, v) )
                parents[v] = u   
    return parents


