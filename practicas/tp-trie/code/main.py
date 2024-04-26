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
    
T=Trie()
T1=Trie()
T2=Trie()
T.root=TrieNode()
A=TrieNode()
A.key="d"
B=TrieNode()
B.key="s"
C=TrieNode()
C.key="e"
C.isEndOfWord=True
A.children=[C]
T.root.children=[A,B]
T1=trie.insert(T1,"dedos")
T1=trie.insert(T1,"desodorante")
T1=trie.insert(T1,"dely")
T1=trie.insert(T1,"deseo")
T1=trie.insert(T1,"deseos")
T1=trie.insert(T1,"desod")
T1=trie.insert(T1,"de")
T2=trie.insert(T2,"dedos")
T2=trie.insert(T2,"desodorante")
T2=trie.insert(T2,"dely")
T2=trie.insert(T2,"deseo")
T2=trie.insert(T2,"deseos")
T2=trie.insert(T2,"desod")
T2=trie.insert(T2,"de")
print(trie.compare(T1,T2))
T2=trie.insert(T2,"ded")
print(trie.compare(T1,T2))
#trie.patron(T1,"de",2)
#lee(T1.root.children[0])
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


    