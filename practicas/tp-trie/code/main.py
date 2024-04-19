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
        
    else:
        return
    if node.children != None:
        lee(node.children[0])
    
T=Trie()
T.root=TrieNode()
A=TrieNode()
A.key="d"
B=TrieNode()
B.key="s"
C=TrieNode()
C.key="e"
A.children=[C]
T.root.children=[A,B]
lee(A)
trie.insertR(C,"do")
print("!")
lee(A)





    