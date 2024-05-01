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
    if len(p)>n:
        return False
    
    #ultima letra del prefix
    uP = searchLast(T,p)

    if len(p)==n:
        if search(T,p):
            return print(p)
        else:
            return False
        
    return patronR(uP.children, p, len(p), n, False)       
              
def patronR(lista, cad, cont, n, endWord):
    if cont == n and endWord is True:
        return print(cad)
    elif lista is None:
        return 
       
    for i in range(len(lista)):
        if cont == n: 
             return 
        else:    
            patronR(lista[i].children, cad+lista[i].key, cont+1, n, lista[i].isEndOfWord)

def compare(t1,t2):

    l1=[True]
    l2=[True]
    busquedaR(t1.root.children,t2,"", False,l1)
    busquedaR(t2.root.children,t1,"", False,l2)

    if len(l1) != len(l2) or l1[0] is False or l2[0] is False:
         return False
    return True

def busquedaR(lista,t, cad, endWord,listAux):
    if endWord is True:
        listAux.append(cad)
        if search(t,cad) is False:
            listAux[0] = False

    if lista is None:
        return listAux
    
    for i in range(len(lista)):    
        busquedaR(lista[i].children, t, cad+lista[i].key,  lista[i].isEndOfWord,listAux)

def invertir_palabra(cad):
     return cad[::-1]

def cad_invertida(T):
    valor=[False]
    def recorreT(T,lista, cad, endWord,valor):
        if endWord is True and search(T,invertir_palabra(cad)):
            valor[0] = True
            return 
        if lista is None:
            return  
        
        for i in range(len(lista)):    
            recorreT(T,lista[i].children, cad+lista[i].key,  lista[i].isEndOfWord,valor)
    recorreT(T,T.root.children, "", False,valor)
    return valor[0]

def Autocomplete(T,cad):
    l=[""]
    def AutocompleteR(node,cad,l):
        if len(node.children) == 1:
            
            cad=cad+node.children[0].key
            if node.children[0].isEndOfWord is True:
                l[0]=cad
                return
            AutocompleteR(node.children[0],cad,l)
        else:
            l[0]=cad
            return
        
    AutocompleteR(searchLast(T,cad),"",l)
    return l[0]