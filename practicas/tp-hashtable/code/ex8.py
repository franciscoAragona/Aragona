from dictionary import *
#otro tipo de clase para str en el que se le puede agregar un index
class dicNode_str:
    key=None
    value=None
    indx=None
#lee para la clase dicNode_str()
def lee(D):
    for i in range(len(D)):
        if D[i] is None:
            print(None)
        elif type(D[i]) is not list:
            print(D[i].key," : ",D[i].value, D[i].indx)
        else:
            for j in range(len(D[i])):
                if j != len(D[i])-1:
                    print(D[i][j].key,":",D[i][j].value,D[i][j].indx, end=" ---> ")
                else:
                    print(D[i][j].key,":",D[i][j].value,D[i][j].indx , end="")
            print()
#le agrega al nodo a insertar un index
def insert_indexado(D, key, value,index):
    slot= hashResto(key,len(D))
    node=dicNode()
    node.key=key
    node.value=value
    node.indx=index
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

#busca una en un slot el value y devuelve el index 
def searchValue_indexStr(D,key,value):
    #accedo al slot
    slot=D[hashResto(key,len(D))]
    #si es una lista busca el value y develve el index
    if type(slot) is list:
        for i in range(len(slot)):
            if slot[i].value == value:
                return slot[i].indx
    #si no es una lista, verifica que no sea nulo y que el unico elemento q haya se el de la value
    elif slot is not None:
        if slot.value == value:
            return slot.indx
    return None

def ocurrencia(s1,s2):
    d=creat(11)
    #divide el funcionamiento para buscar simpre dentro de la palabra mas grande
    if len(s1) > len(s2):
        cad1 = s1
        cad2 = s2
    elif len(s1) < len(s2):
        cad1 = s2
        cad2 = s1
    else:
        if s1 == s2:
            return 0
        else:
            return None
    #recorre la palabra mas grande guardando todas las posibles combinaciones de la longitud de la palabra mas chica
    #O(len(cad1)-len(cad2)+1)
    for i in range(0,len(cad1)-len(cad2)+1):
        #key=el primer caracter de la cadena a guardar; value=cadena de longitud de la mas chica; 
        #indx=la posicion en la que se encuentra el inicio del value en la cadena  mas grande 
        #O(1)
        insert_indexado(d,cad1[i],cad1[i:len(cad2)+i],i)
    #O(n/m)
    return searchValue_indexStr(d,cad2[0],cad2)


s="abracadabrayamaltamalsamelconolzazasabaquedasedapedareda"
i=ocurrencia(s,"tama")
print(s[i:i+4])
s="abracadabrayamaltamalsamelconolzazasabaquedasedapedareda"
print(ocurrencia("tama","tame"))
