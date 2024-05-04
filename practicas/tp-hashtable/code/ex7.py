from dictionary import *

def insertCad(D, key, value):
    slot= hashCad(key)
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

def compresion(cad):
    d=creat(52)
    cadAux=cad[0]
    cadActual=cad[0]
    for c in cad:
        insertCad(d,c,c)
    for x in range(1,len(cad)):
        if cadActual != cad[x]:
            if type(d[hashCad(cadActual)]) is list:
                cadAux=cadAux+str(len(d[hashCad(cadActual)]))+cad[x]
                cadActual=cad[x]
            else:
                cadAux=cadAux+"1"
            print(cadAux)

    return d

def hashCad(key):
    if key.isupper():
        return ord(key)-ord("A")
    else:
        return ord(key)-ord("a")+26

print(ord("a"))
print(ord("z"))
print(ord("z")-ord("a"))
print(ord("A"))
print(ord("Z"))
print(ord("Z")-ord("A"))    
print("###########")
s="abcdefghijklmnopklrstuwvxyz"
len(s)
print("###########")

#d=compresion("abcdefghijklmnopqrstuwvxyz".upper())
d=compresion("aaabbaaabc")
#lee(d)