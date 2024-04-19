class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False

def insertR(node,cad):
    k=cad[0]
    cadAux=cad[1:]
    t=TrieNode()
    t.parent=node
    t.key=k
    node.children=[t]

    if len(cad)==1:
        t.isEndOfWord=True
        return
    
    insertR(t,cadAux)      



