import numpy as np

def parseGraph():
    #conjunto con toda la información parseada
    file = open("grafo.txt","r")
    data = []
    init = file.readline().split(' ')[1].strip()
    goal = file.readline().split(' ')[1].strip()
    h =[]
    edges =[]
    for i in range(8):
        aux = file.readline().split(' ')
        dictionary = {aux[0]:int(aux[1])}
        h.append(dictionary)
    for i in range(10):
        aux =file.readline().split(',')
        edges.append([aux[0],aux[1],int(aux[2])])

    
    print(init)
    print(goal)
    print(h)
    print(edges)
    data.append(init)
    data.append(goal)
    data.append(h)
    data.append(edges)
    return data
    


data = parseGraph()
print(data[0])
print(data[1])
print(data[2])
print(data[3])