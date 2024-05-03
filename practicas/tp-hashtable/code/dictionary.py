class dicNode:
    key=None
    value=None
def lee(D):
    for i in range(len(D)):
        if D[i] is None:
            print(None)
        elif type(D[i]) is not list:
            print(D[i].key," : ",D[i].value)
        else:
            for j in range(len(D[i])):
                if j != len(D[i])-1:
                    print(D[i][j].key,":",D[i][j].value, end=" ---> ")
                else:
                    print(D[i][j].key,":",D[i][j].value, end="")
            print()
#crea un lista de tamaño m
def creat(m):
    D=[None]*m
    return D

#funcion de hash por resto
def hashResto(k,m):
    if type(k) is str:
        if len(k) == 1:
            # ord() devuelve el valor que representa en el código Unicode
            return ord(k) % m
        else:
            return len(k) % m
    return k % m

#insert de un elemetnon en el diccionario ya creado
def insert(D, key, value):
    slot= hashResto(key,len(D))
    node=dicNode()
    node.key=key
    node.value=value
    #casillero vacio
    if D[slot] is None:
        D[slot]=node
    #el slot ya tiene mas de un elemento
    elif type(D[slot]) is list:
        D[slot].append(node)
    #el slot tiene un solo elemento
    else:
        D[slot]=[D[slot]]
        D[slot].append(node)
    return D

def search(D,key):
    #accedo al slot
    slot=D[hashResto(key,len(D))]
    #si es una lista busca la key y develve el value
    if type(slot) is list:
        for i in range(len(slot)):
            if slot[i].key == key:
                return slot[i].value
    #si no es una lista, verifica que no sea nulo y que el unico elemento q haya se el de la key
    elif slot is not None:
        if slot.key == key:
            return slot
    return None


def delete(D,key):
    #busca el slot donde deberia estar la key q buscamos
    slot=D[hashResto(key,len(D))]
    #caso de que el slot sea una lista
    if type(slot) is list:
        for i in range(len(slot)):
           if slot[i].key == key:
                slot[i].key=None
                return D
    #caso en el que no es una lista, pero no esta vacio
    elif slot is not None:
        if slot.key == key:
            slot[i].key=None
            return D
    return D
"""
m=9
D=creat(m)
print(D)
insert(D,15,"oso")
print(D[hashResto(15,m)].key)
print(D)
insert(D,33,"casa")
print(D)
print(search(D,15))
print(search(D,16))
lee(D)
delete(D,15)
lee(D)
"""