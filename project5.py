"""
Math 560
Project 5
Fall 2021

Partner 1: Ian Liu (cl583)
Partner 2: Leo Han (nh185)
Date:
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm
"""
def prim(adjList, adjMat):
    ##### Your implementation goes here. #####
    start = adjList[0]
    start.cost = 0
    Q = PriorityQueue(adjList)

    while not Q.isEmpty():
        v = Q.deleteMin()
        v.visited = True

        for neigh in v.neigh: #look for weight of edges and update the value if the node is not visited
            if not neigh.visited:
                if neigh.cost > adjMat[v.rank][neigh.rank]:
                    neigh.cost = adjMat[v.rank][neigh.rank]
                    neigh.prev = v
    return

################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
"""
def kruskal(adjList, edgeList):
    ##### Your implementation goes here. #####
    for v in adjList:
        makeset(v)
    X = []
    for e in edgeList:
        v1, v2 = e.vertices
        if find(v1).isEqual(find(v2)) == False:  
            X.append(e)
            union(v1, v2)
    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""
def makeset(v):
    ##### Your implementation goes here. #####
    v.pi = v
    v.height = 0
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""
def find(v): # use path compression to find node
    ##### Your implementation goes here. #####
    if v != v.pi:
        v.pi = find(v.pi)
    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v): # union the set every time we connect two nodes
    ##### Your implementation goes here. #####
    ru = find(u)
    rv = find(v)

    if ru == rv:
        return

    if ru.height > rv.height:
        rv.pi = ru
    elif ru.height < rv.height:
        ru.pi = rv
    else:
        ru.pi = rv
        rv.height = rv.height + 1
        pass
    return

################################################################################

"""
TSP
"""
def tsp(adjList, start):
    ##### Your implementation goes here. #####
    # initialized vertex to unvisted
    for v in adjList:
        v.visited = False
    
    tour = []
    stack = []
    stack.append(start)
    
    while stack:
        v = stack.pop()
        tour.append(v.rank)
        v.visited = True # mark visited before appending the node
        for neigh in v.mstN:
            if not neigh.visited:
                stack.append(neigh)
    tour.append(start.rank)
        
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
