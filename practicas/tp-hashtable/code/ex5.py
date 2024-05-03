from dictionary import *
#la complejidad seria O(n) siendo n el tamaño de la lista 
def repetidos(lista):
    #creo el hashTable inicila 
    d=creat(9)
    #carga los valores de nuestra lista en el hash mientras q verifica si ya estan en el hash
    for i in lista:
        if search(d,i) is None:
            insert(d,i,i)
        else:
            return False
    return True
