import trie

class Trie:
    root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False

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
lee(A)
#trie.delete(T,"de")
print("------------")
lee(A)
trie.delete(T,"dedo")
print("------------")
lee(A)



    