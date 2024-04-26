class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False  

def delete(T,cad):

    if search(T,cad) is False:
          return False
    node=searchLast(T,cad)

    if node.children is not None:
         node.isEndOfWord=False
         return True

    deleteR(searchLast(T,cad))

def deleteR(node):
    
    if len(node.parent.children) == 1:
        node.parent.children = None
    else:
         node.parent.children.remove(node)  
         return True  
    
    if node.parent.isEndOfWord is True:
         return True
    
    if node.parent is None:
        return True
    
    deleteR(node.parent)
    return

def findKey(L,c):

    for i in range(len(L)):
        if L[i].key==c:
            return L[i]
    return None

def searchLast(T,cad):
    if T.root==None:
        return False

    n=0
    node=T.root.children

    while findKey(node,cad[n]) is not None:
        node=findKey(node,cad[n])
        
        if n+1 is len(cad):
                return node
        
        if node.children is None:
                return False
                
        n=n+1
        node=node.children
    return False

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
        t.parent=T.root
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

def patron(T,p,n): #(trie, patron, tamaño)
    print("patron")
    if len(p)<n:
        print("caso1")
        return False
    #ultima letra del prefix
    uP = searchLast(T,p)
    if len(p)==n:
        if search(T,p):
            print("caso2")
            return print(p)
        else:
            print("caso3")
            return False
    return patronR(uP.children,p,len(p),n)       
              
def patronR(lista, cad, cont, n):
    print(cad)
    for i in range(lista):
        cad=cad+lista[i]
        if cont == n and lista[i].isEndOfWord is True:
            return print(cad)
        elif cont == n:
             return 
        else:
             patronR(lista[i].children,cad,cont+1,n)
