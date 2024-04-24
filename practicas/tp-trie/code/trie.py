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

def search(T,cad):
    if T.root==None:
        return False

    n=0
    node=T.root.children

    while findKey(node,cad[n]) is not None:
        node=findKey(node,cad[n])
        
        if n+1 is len(cad) and node.isEndOfWord is True:
                return True
        elif n+1 is len(cad) and node.isEndOfWord is False:
                return False
        if node.children is None:
                return False
                
        n=n+1
        node=node.children
    return False


def insert(T,cad):
    n=0

    if T.root==None:
        T.root=TrieNode()
        insertR(T.root,cad)
        return T
    
    node=findKey(T.root.children,cad[n])

    if node is not None:
        n=n+1
        node=node.children

        while findKey(node,cad[n]) is not None:
            node=findKey(node,cad[n])
            if n+1==len(cad):
                node.isEndOfWord=True
                return T
            
            n=n+1
            if node.children is None:
                insertR(node,cad[n:])
                return T
            else:
                node=node.children

        insertR(node[0].parent,cad[n:])
        return T
    
    else:
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



