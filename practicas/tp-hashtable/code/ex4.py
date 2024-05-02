from dictionary import *

def is_permutation(s1,s2):
    #crea una tabla de tamaño s1
    D=creat(len(s1))
    #guarda todos los caracteres de s1 en la hashTable
    for caracter in s1:
        insert(D,caracter,caracter)
    #busca todos los caracteres de s2 en la hashTable
    for caracter in s2:
        if len(s1) != len(s2) or search(D,caracter) is None:
            return False   
    return True

