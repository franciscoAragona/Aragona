import trie

class Trie:
    root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False

def leeTrie(lista, cad, endWord):
    if endWord is True:
        print(cad)
    if lista is None:
        return  
    
    for i in range(len(lista)):    
        leeTrie(lista[i].children, cad+lista[i].key,  lista[i].isEndOfWord)

def lee(node):
    if node.key != None:
        print(node.key)
        if node.isEndOfWord is True:
            print("isEndOfWord")
    else:
        return
    if node.children != None:
        lee(node.children[0])
T1=Trie()
#T1=trie.insert(T1,"color")
T1=trie.insert(T1,"madera")
T1=trie.insert(T1,"mama")
#T1=trie.insert(T1,"polar")
print(trie.Autocomplete(T1,"ma"))
"""
lee(A)
trie.insertR(C,"do")
print("------------")
lee(A)
#lee(T1.root.children)
print("------------")
T1=trie.insert(T1,"color")
lee(T1.root.children[0])
print("------------")
T1=trie.insert(T1,"colores")
lee(T1.root.children[0])
T1=trie.insert(T1,"colorear")
T1=trie.insert(T1,"polar")
print("------------")

lee(T1.root.children[1])
print(trie.search(T1,"cola"))
T1=trie.insert(T1,"cola")
print(trie.search(T1,"cola"))
print(len([]))
print("------------")
#lee(A)
#trie.delete(T,"de")
print("------------")
#lee(A)
#trie.delete(T,"dedo")
print("------------")
#lee(A)
print("------------")
#trie.delete(T1,"polar")
#lee(T1.root.children[1])
#print(T1.root.children)
"""


    