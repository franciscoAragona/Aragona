#crea un diccionario de tamaño m
def creat(m):
    D={}
    #se encarga de rellenarlo en none
    for i in range(m):
        D[i]=None
    return D

#funcion de hash por resto
def funcHash(k,m):
    if type(k) is str:
        if len(k) == 1:
            # ord() devuelve el valor que representa en el código Unicode
            return ord(k) % m
        else:
            return len(K) % m
    return k % m

#insert de un elemetnon en el diccionario ya creado
def insert(D, key, value):
    slot= funcHash(key,len(D))
    #casillero vacio
    if D[slot] is None:
        D[slot]=(key,value)
    #el slot ya tiene mas de un elemento
    elif type(D[key]) is list:
        D[slot].append((key,value))
    #el slot tiene un solo elemento
    else:
        D[slot]=[D[slot]]
        D[slot].append((key,value))
    return D

def search(D,key):
    return D[funcHash(key,len(D))]

def delete(D,key):

    return

m=9
D=creat(m)
print(D)
insert(D,funcHash(15,m),"oso")
print(D)
insert(D,funcHash(33,m),"casa")
print(D)


"""
def direc(d,v,k):
    if d[k] is None:
        d[k]=v
    elif type(d[k]) is list:
        d[k].append(v)
    else:
        d[k]=[d[k]]
        d[k].append(v)
    return d
dic = { 1:2, 2:None, 3:4}
print(dic)

dic[5]= [2,5,5,6]
print(dic, "::::::")
print(dic[5])
direc(dic,"u",5)
print(dic, "-------")

print(dic.values())
print(dic.keys())
"""