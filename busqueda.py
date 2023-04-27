import queue
import parseGraph
import random

class Node:
    #se crea el nodo con su valor, una lista de hijos y su cantidad de 
    #expansiones inicializada en 0
    def __init__(self, v, h):
        self.v = v
        self.h = h
        self.children = []
        self.exp = 0
    #funcion para agregar un hijo a un nodo
    def addChild(self, child, weight):
        self.children.append((child,weight))
class SearchTree:
    #se inicializa el arbol con el nodo raiz y los hijos
    #se le pasa el nodo de inicio, la meta, las heuristicas y las aristas
    def __init__ (self, ini, goal, h, edges):
        #se crea un diccionario que contendra los nodos con sus heuristicas en un diccionario
        #la llave sera el valor
        self.vlist = {}
        #se crea una lista con todos los nodos 
        self.klist = []
        #se rellena la lista de nodos
        for i in range(len(h)):
            self.klist.append(h[i][0])
        #se busca el nodo de inicio y se inserta en el diccionario 
        index = self.klist.index(ini)
        self.vlist[h[index][0]] = Node(h[index][0],h[i][1])
        self.ini = self.vlist[h[index][0]]
        #print(self.ini.v)
        #en el caso de la meta solo se utilizara el valor
        self.goal = goal
        #se rellena el diccionario con todos los nodos que faltan
        #y su respectiva heuristica
        for i in range(len(h)):
            if h[i][0] not in self.vlist:
                self.vlist[h[i][0]] = Node(h[i][0],h[i][1])
        #se agregan los hijos a cada nodo en base a la arista pasada anteriormente
        for i in range(len(edges)):
            self.vlist[edges[i][0]].addChild(self.vlist[edges[i][1]],edges[i][2])


    def printList(self,h):
        for i in range(len(self.vlist)):
            print(self.vlist[h[i][0]].children)

    def dfs(self):
        #se crea una lista con el nodo raiz, el camino inicial, y el costo inicial
        stack = [(self.ini, [],0)]
        #se crea una lista de nodos visitados 
        visited = []
        #print(self.ini.v)
        #se itera mientras haya rutas sin explorar
        while stack:
            #se guardan los datos del tope de la lista
            newNode, newRoute, newCost = stack.pop()
            #si se llega al objetivo, se imprime la ruta, el costo y las expansiones de cada nodo
            if newNode.v == self.goal:
                newRoute.append(newNode)
                path = ' -> '.join([node.v for node in newRoute])
                print(path)
                print(f"Costo: {newCost}")
                tExp =0
                nodeList = []
                for node in self.vlist.values():
                    print(f"{node.v}: {node.exp}")
                    nodeList.append((node.v,node.exp))
                    tExp+= node.exp
                if newCost == 18:
                    opt = True
                    return path, newCost, opt,nodeList, tExp 
                opt = False 
                return path, newCost, opt, nodeList, tExp
                
            #si el nodo no ha sido visitado
            if newNode not in visited:
                #print(f"hijos del nodo actual: {newNode.children}")
                #se agrega al set 
                visited.append(newNode)
                #se notifica su expansión
                newNode.exp += 1
                #se crea una lista que copia a los hijos del nodo actual
                #para cambiar su orden aleatoriamente, asi cumple condición de
                #escoger sucesor al azar
                childList = newNode.children.copy()
                random.shuffle(childList)
                #se agregan los nodos hijos a la lista
                for child, cost in childList:
                    #print(f"el peso es: {cost}")
                    stack.append((child, newRoute + [newNode],newCost+cost))
        print("no se encontró una solución")
    
    def uniformCost(self):
        #se crea un diccionario del costo acumulado 
        cost = {self.ini: 0}
        #se crea una cola de prioridad con prioridad inicial
        #nodo raiz y camino
        stackq = queue.PriorityQueue()
        stackq.put((0,self.ini, []))
        #se crea una lista de nodos visitados
        visited = []
        #se itera mientras haya rutas sin explorar
        while stackq:
            #se recuper la prioridad que no se usa, el nodo que se exploro, la nueva ruta
            _,newNode, newRoute = stackq.get()
            #si se llega al objetivo se imprime el camino, costo y expansionee
            if newNode.v == self.goal:
                newRoute.append(newNode)
                path = ' -> '.join([nodo.v for nodo in newRoute])
                print(path)
                print(f"Costo: {cost[newNode]}")
                nodeList = []
                tExp = 0
                for node in self.vlist.values():
                    print(f"{node.v}: {node.exp}")
                    nodeList.append((node.v,node.exp))
                    tExp+= node.exp
                if newCost == 18:
                    opt = True
                    return path, newCost, opt,nodeList, tExp 
                opt = False 
                return path, newCost, opt, nodeList, tExp
            #se expande el nodo
            newNode.exp += 1
            #si el nodo no ha sido visitado se agrega al set
            if newNode not in visited:
                visited.append(newNode)
                #se calculan los costos acumulados y se verifica si el costo del camino
                #desde la raiz hasta el hijo actual es menor que el costo minimo actual
                #si es así se actualiza el costo minimo y se agrega a la lista
                for child, weight in newNode.children:
                    newCost = cost[newNode] + weight
                    if child not in cost or newCost < cost[child]:
                        cost[child] = newCost
                        stackq.put((newCost, child, newRoute + [newNode]))
        print("No se encontró solución")
        
    def greedy(self):
        #se procede con el mismo procedimiento de dfs pero agregando la heuristica del nodo
        stack = [(self.vlist[self.ini.v],self.ini, [],0)]
        visited = []
        #print(self.ini.v)
        while stack:
            #lo mismo de dfs pero además se recupera la heuristica
            newH,newNode, newRoute, newCost = stack.pop(0)
            #print(newH)
            #si se llega al objetivo se imprime el camino, el costo y las expansiones
            if newNode.v == self.goal:
                newRoute.append(newNode)
                path = ' -> '.join([node.v for node in newRoute])
                print(path)
                print(f"Costo: {newCost}")
                nodeList = []
                tExp = 0
                for node in self.vlist.values():
                    print(f"{node.v}: {node.exp}")
                    nodeList.append((node.v,node.exp))
                    tExp+= node.exp
                if newCost == 18:
                    opt = True
                    return path, newCost, opt,nodeList, tExp 
                opt = False 
                return path, newCost, opt, nodeList, tExp
            #se suma la expansión
            #si el nodo no se ha visitado se agrega al set de visitados 
            newNode.exp += 1
            if newNode not in visited:
                #print(f"hijos del nodo actual: {newNode.children}")
                visited.append(newNode)
                #se agregan los hijos a la lista y luego se ordena la lista para
                #tener el hijo con menor costo de la heuristica
                for child, cost in reversed(newNode.children):
                    if child not in visited:
                        stack.append((self.vlist[child.v].h,child, newRoute + [newNode],newCost+cost))
                stack.sort()
        print("no se encontró una solución")

    def starA(self):
        #se inicia el diccionario con los costos acumulados 
        cost = {self.ini: 0}
        #cola de prioridad que tendra la función de evaluación, el nodo inicial y el camino inicial
        stackq = queue.PriorityQueue()
        stackq.put((self.vlist[self.ini.v],self.ini, []))
        #se crea una lista de nodos visitados
        visited = []
        #se itera mientras haya contenido
        while stackq:
            #se recuperan los datos 
            _,newNode, newRoute = stackq.get(0)
            #si se llega al nodo solución se imprime la ruta el costo y las expansiones
            if newNode.v == self.goal:
                newRoute.append(newNode)
                path = ' -> '.join([nodo.v for nodo in newRoute])
                print(path)
                print(f"Costo: {cost[newNode]}")
                nodeList = []
                tExp = 0
                for node in self.vlist.values():
                    print(f"{node.v}: {node.exp}")
                    nodeList.append((node.v,node.exp))
                    tExp+= node.exp
                if newCost == 18:
                    opt = True
                    return path, newCost, opt,nodeList, tExp 
                opt = False 
                return path, newCost, opt, nodeList, tExp
            #se expande el nodo actual
            newNode.exp += 1
            #si el nodo no ha sido visitado se agrega al set de visitados
            if newNode not in visited:
                visited.append(newNode)
                #se recorren los hijos y se crea el nuevo costo en base a la función del costo acumulado más la heuristica
                for child, weight in newNode.children:
                    #se calcula el nuevo costo
                    newCost = cost[newNode] + weight
                    #si el costo del hijo no se ha calculado o si 
                    #el nuevo costo es menor que el costo del hijo, se
                    #asigna ese nuevo costo al hijo, ya que se encuentra un 
                    #valor menor para el camino, se crea la nueva función de evaluación
                    #y se agrega el valor asociado al hijo y la ruta actualizada
                    if child not in cost or newCost < cost[child]:
                        cost[child] = newCost
                        f = newCost + self.vlist[child.v].h
                        stackq.put((f, child, newRoute + [newNode]))
        print("No se encontró solución")
        

data = parseGraph.parseGraph()
ini = data[0]
goal = data[1]
h = data[2]
edges = data[3]
tree = SearchTree(ini,goal,h,edges)
option = input(f"ingrese que algoritmo desea usar: \n1.DFS\n2.Costo uniforme\n3.Greedy\n4.A*\n")
match option:
    case "1":
        tree.dfs()
    case "2":
        tree.uniformCost()
    case "3":
        tree.greedy()
    case "4":
        tree.starA()
    case _:
        print("no has elegido una opción disponible")
