import numpy as np
import parseGraph 
import random
class Graph:
    def __init__(self, edges):
        self.vlist = {}
        self.exp = {}
        for i in range(len(edges)):
            if edges[i][0] not in self.vlist:
                self.vlist[edges[i][0]] = {}
                self.exp[edges[i][0]] = 0
            if edges[i][1] not in self.vlist:
                self.vlist[edges[i][1]] = {}
                self.exp[edges[i][1]] = 0
            self.vlist[edges[i][0]][edges[i][1]] = edges[i][2]
    def getV(self):
        aux = self.vlist.keys()
        return aux
    def printVlist(self):
        print(self.vlist)
    def dfs(self, ini, goal):
        visited = set()
        stack = [(ini, [ini], 0)]
        while stack:
            (v, r, c) = stack.pop()
            if v not in visited:
                visited.add(v)
                self.exp[v] +=1
                if v == goal:
                    print(" -> ".join(r))
                    print("Costo: ",c)
                    self.exp[v] -=1
                    for key, value in self.exp.items():
                        print(key,": ",value)
                    return
                npool = list(self.vlist[v].keys())
                random.shuffle(npool)
                for n in npool:
                    if n not in visited:
                        weigth = self.vlist[v][n]
                        newR = r + [n]
                        newC = c + weigth
                        print(newR)
                        stack.append((n,newR,newC))
        print("no se encontro una solución")
        return        


data = parseGraph.parseGraph()
ini = data[0]
goal = data[1]
h = data[2]
edges = data[3]
#print(ini)
#print(goal)
#print(h)
print(edges)
g = Graph(edges)
g.printVlist()
g.dfs(ini,goal)
#g.printvlist()
#printGraph(g)
