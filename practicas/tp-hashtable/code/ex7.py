def compresion(cad):
    cadAux=""
    cont=1
    #recorro la palabra de tamaño n, asique la complejidad temporal es O(n)
    for x in range(1, len(cad)):
        #llevo un conteo de todas las letras que son iguales a Cad[x-1]
        if cad[x] == cad[x-1]:
            cont += 1
        else:
            #cuando el caracter x es distinto del x-1 concatena el caracter x-1 y el cont
            cadAux += cad[x-1] + str(cont)
            #en la siguiente iteracion la letra x-1 va a ser nuestra x actual por lo que hay que contarla una vez
            cont=1
    #cuando se sale del bucle, el ultimo caracter no se llega a guardar, por eso hay q agregar esta linea
    cadAux += cad[-1] + str(cont)
    #se compaaran las cadenas y se devuelve la mas corta
    if len(cad)>len(cadAux):
        return cadAux
    else:
        return cad
    
d=compresion("aaaabbaaaabbbbbbbbbbbbbbbbbbbb")
print(d)
d=compresion("a")
print(d)

"""
#no use esto pq era mas complejo de lo q pense, pero est abuena la implementacion del hashCad
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

def hashCad(key):
    if key.isupper():
        return ord(key)-ord("A")
    else:
        return ord(key)-ord("a")+26
"""

