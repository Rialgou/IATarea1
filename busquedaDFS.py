import numpy as np
import parseGraph 
class Graph:
    def __init__(self,h,edges):
        self.vlist ={}
        vsize = len(h)
        for i in range(vsize):
            self.vlist[h[i][0]] = i 
        self.adjList = [None]*vsize

        for i in range(vsize):
            self.adjList[i] =[]
        for(src,dest,weight) in edges:
            self.adjList[self.vlist[src]].append((dest,weight))

    def printvlist(self):
        print(self.vlist)    
def printGraph(graph):
    for src in range(len(graph.adjList)):
        for(dest,weight) in graph.adjList[src]:
            print(f'({src} -> {dest},{weight})',end='')
            print()

data = parseGraph.parseGraph()
ini = data[0]
goal = data[1]
h = data[2]
edges = data[3]
print(ini)
print(goal)
print(h)
print(edges)
g = Graph(h,edges)
g.printvlist()
printGraph(g)
