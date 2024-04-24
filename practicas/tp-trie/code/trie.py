class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False
def findKey(L,c):
    for i in range(len(L)):
        if L[i].key==c:
            return L[i]
    return None

def insert(T,cad):
    n=0
    print("insert")

    if T.root==None:
        print("caso 1")
        T.root=TrieNode()
        insertR(T.root,cad)
        return T
    
    print("insert")
    node=findKey(T.root.children,cad[n])

    if node is not None:
        print("caso 2")
        n=n+1
        node=node.children

        while findKey(node,cad[n]) is not None:
            node=findKey(node,cad[n])
            if n+1==len(cad):
                node.isEndOfWord=True
                return T
                    
            n=n+1
            if node.children is None:
                print(cad[n:])
                insertR(node,cad[n:])
                return T
            else:
                node=node.children

        print(": ", cad[n:])
        insertR(node[0].parent,cad[n:])
        
        return T
    else:
        print("insert")
        t=TrieNode()
        t.key=cad[0]
        T.root.children.append(t)
        insertR(t,cad[1:])
        return T

def insertR(node,cad):
    k=cad[0]
    cadAux=cad[1:]
    t=TrieNode()
    t.parent=node
    t.key=k
    if node.children is None:
        node.children=[t]
    else:
        node.children.append(t)

    if len(cad)==1:
        t.isEndOfWord=True
        return
    
    insertR(t,cadAux)      



