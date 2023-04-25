import parseGraph
import random

class Node:
    #se crea el nodo con su valor, una lista de hijos y su cantidad de 
    #expansiones inicializada en 0
    def __init__(self, v,h):
        self.v = v
        self.h = h
        self.children = []
        self.exp = 0
    #funcion para agregar un hijo a un nodo
    def addChild(self, child, weight):
        self.children.append((child,weight))
class SearchTree:
    #se inicializa el arbol con el nodo raiz y los hijos
    def __init__ (self, ini, goal, h, edges):
        self.vlist = {}
        self.klist = []
        for i in range(len(h)):
            self.klist.append(h[i][0])
        index = self.klist.index(ini)
        self.vlist[h[index][0]] = Node(h[index][0],h[i][1])
        self.ini = self.vlist[h[index][0]]
        #print(self.ini.v)
        self.goal = goal
        for i in range(len(h)):
            if h[i][0] not in self.vlist:
                self.vlist[h[i][0]] = Node(h[i][0],h[i][1])
        
        for i in range(len(edges)):
            self.vlist[edges[i][0]].addChild(self.vlist[edges[i][1]],edges[i][2])


    def printList(self,h):
        for i in range(len(self.vlist)):
            print(self.vlist[h[i][0]].children)
    def dfs(self):
        stack = [(self.ini, [],0)]
        visitados = set()
        #print(self.ini.v)
        while stack:
            newNode, newRoute, newCost = stack.pop()
            if newNode.v == self.goal:
                newRoute.append(newNode)
                path = ' -> '.join([node.v for node in newRoute])
                print(path)
                print(f"Costo: {newCost}")
                for node in newRoute:
                    print(f"{node.v}: {node.exp}")
                return
            if newNode not in visitados:
                #print(f"hijos del nodo actual: {nodo_actual.children}")
                visitados.add(newNode)
                newNode.exp += 1
                childList = newNode.children.copy()
                random.shuffle(childList)
                for child, cost in childList:
                    #print(f"el peso es: {peso}")
                    stack.append((child, newRoute + [newNode],newCost+cost))
        print("no se encontró una solución")
    def uf(self):

        return   
    
data = parseGraph.parseGraph()
ini = data[0]
goal = data[1]
h = data[2]
edges = data[3]

tree = SearchTree(ini,goal,h,edges)
tree.dfs()