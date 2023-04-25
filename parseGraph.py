def parseGraph():
    #conjunto con toda la información parseada
    with open('grafo.txt','r') as file:
        data = []
        init = file.readline().split(' ')[1].strip()
        goal = file.readline().split(' ')[1].strip()
        h =[]
        edges =[]
        for f in file:
            aux = f.strip().split() if ' ' in f else f.strip().split(',')
            if(len(aux) == 2):
                dictionary = [aux[0],int(aux[1])]
                h.append(dictionary)
            elif(len(aux) == 3):
                edges.append([aux[0],aux[1],int(aux[2])])
    data.append(init)
    data.append(goal)
    data.append(h)
    data.append(edges)
    return data

