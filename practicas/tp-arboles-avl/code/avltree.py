class AVLTree:
    root = None

class AVLnode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None

"""
rota hacia la izquierda el nodo que se la pasa (hace la rotacion sin importar 
el bf del nodo q se le pase)
"""

def rotateLeft(avl,avlnode) :

    newroot = avlnode.rightnode
    #si se tiene q hacer una rotacion a la izquierdo la newroot va a aser el nodo de la derecha y 
    #ademas si esta newroot tiene un nodo a la izquierdo pasa a ser el nodo derecho de la oldroot
    if newroot.leftnode != None :
        avlnode.rightnode = newroot.leftnode
        avlnode.rightnode.parent=avlnode

    if avlnode.parent == None :
        avl.root = newroot
        avlnode.parent = newroot

    else : 
        if avlnode.parent.rightnode == avlnode :
            avlnode.parent.rightnode = newroot 
            avlnode.parent = newroot

        else :
            avlnode.parent.leftnode = newroot 
            avlnode.parent = newroot

    return newroot

"""
rota hacia la derecha el nodo que se la pasa (hace la rotacion sin importar 
el bf del nodo q se le pase)
"""

def rotateRight(avl,avlnode) :

    newroot = avlnode.leftnode
    #si se tiene q hacer una rotacion a la derecha la newroot va a aser el nodo de la izquierda y 
    #ademas si esta newroot tiene un nodo a la derecha pasa a ser el nodo izquierdo de la oldroot  
    if newroot.rightonode != None :
        avlnode.leftnode = newroot.rightnode
        avlnode.leftnode.parent=avlnode

    if avlnode.parent == None :
        avl.root = newroot
        avlnode.parent = newroot

    else : 
        if avlnode.parent.rightnode == avlnode :
            avlnode.parent.rightnode = newroot 
            avlnode.parent = newroot

        else :
            avlnode.parent.leftnode = newroot 
            avlnode.parent = newroot
    return newroot

"""
calcula el bf de cada nodo
"""

def calculateBalance(avl) :
    cbfRecursive(avl.root)
    return avl
#calcula el bf de cada nodo de un arbol
def cbfRecursive(node):
    if node is None:
        return 
    cbf(node)
    cbfRecursive(node.rightnode)
    cbfRecursive(node.leftnode)
    return 
#calcula el bf de un nodo
def cbf(node):

    rh=height(node.rightnode)
    lh=height(node.leftnode)
    node.bf=lh-rh
    #cbf(node.rightnode)
    #cbf(node.leftnode)
    return node.bf
#calcula la altura de un arbol o subarbol
def height(avlnode) :
    if avlnode is None :
        return -1 

    rh = 1 + height(avlnode.rightnode)  
    lh = 1 + height(avlnode.leftnode)
    
    return max(rh,lh)
"""
vuelve a balancear un arbol  (falta codearlo)
1-calcular el bf de todos los nodos
2-Encontrar el primer elemento con abs(bf)>1 (search nodo)


"""
def reBalance(avl):
    calculateBalance(avl)
    #bfp = bf problema
    bfp = findBf(avl.root)
    #rebf = el nodo desde el que se tiene que calcular el bf denuevo
    rebf = bfp
    #while bfp is not None:
    if bfp.bf == 2:
        if bfp.leftnode.bf == -1:
            rotateLeft(avl,bfp.leftnode)
            rebf = bfp.leftnode

        rotateRight(avl,bfp)

    if bfp.bf == -2: 
        if bfp.rightnode.bf == 1:
            rotateRight(avl,bfp.rightnode)
            rebf = bfp.rightnode     

        rotateLeft(avl,bfp)

        #bfp = findBf(avl.root)
    balanceAncestor(rebf)
    return  avl

def balanceAncestor(node):
    if node is None:
        return 
    cbf(node)
    balanceAncestor(node.parent)

def findBf(node):
    if node is None:
        return None
    
    if abs(node.bf)>1:
        return node
    
    bfL=findBf(node.leftnode)
    if bfL is not None:
        return bfL
    
    bfR=findBf(node.rightnode)
    if bfR is not None: 
        return bfR 
"""
eliminar y insertar nodo copia de binary tree de algo1 (search)
"""
def search(B,element):
  return SearchR(B.root,element)
def SearchR(B,element):
  if B!=None and B.value==element:
    return B
  if B.leftnode!=None:
    kl=SearchR(B.leftnode,element)
    if kl!=None:
      return kl
  if B.rightnode!=None:
    kr=SearchR(B.rightnode,element)
    if kr!=None:
      return kr

def insert(B,l,k):
  if l==None or k==None:
    return None
  newB=AVLnode()
  newB.value=l
  newB.key=k
  newB.bf=0
  if B.root==None:
    B.root=newB
    return k
  else:
    newB.parent=B.root
    InsertR(B.root,newB)
    balanceAncestor(newB)
    return search(B,l)
def InsertR(B,newB):
  if B.key < newB.key:
    if B.rightnode==None:
      B.rightnode=newB
      return B
    else:
      newB.parent=B.rightnode
      return InsertR(B.rightnode,newB)
  elif B.key > newB.key:
    if B.leftnode==None:
      B.leftnode=newB
      return B
    else:
      newB.parent=B.leftnode
      return InsertR(B.leftnode,newB)

def delete(B,l):
  if search(B,l)==None:
    return None
  else:
    nodeAux = search(B,l)
    ancestor = nodeAux.parent
    deleteR(B.root,search(B,l))
    balanceAncestor(ancestor)
    
"""
def deleteKey(B,k):
    return deleteR(B.root,k)
"""
def minDmax(nodeT):
  if nodeT.leftnode!=None:
    return minDmax(nodeT.leftnode)
  else:
    eliminaNode(nodeT)
    return nodeT

def eliminaNode(node):
  if node.parent.rightnode==node:
    node.parent.rightnode=None
  else:
    node.parent.leftnode=None

def deleteR(nodeT,k):
  if nodeT.key==k:
    if nodeT.rightnode==None and nodeT.leftnode==None:
      eliminaNode(nodeT)

    elif nodeT.rightnode==None and nodeT.leftnode!=None:
      if nodeT.parent.rightnode!=None:
        if nodeT.parent.rightnode==nodeT: 
          nodeT.parent.rightnode=nodeT.leftnode
          nodeT.leftnode.parent=nodeT.parent.rightnode
      else:
        if nodeT.parent.leftnode!=None:
          nodeT.parent.leftnode=nodeT.leftnode
          nodeT.leftnode.parent=nodeT.parent.leftnode
    elif nodeT.rightnode!=None and nodeT.leftnode==None:
      if nodeT.parent.rightnode!=None:
        if nodeT.parent.rightnode==nodeT: 
          nodeT.parent.rightnode=nodeT.rightnode
          nodeT.rightnode.parent=nodeT.parent.rightnode
      else:
        if nodeT.parent.leftnode!=None:
          nodeT.parent.leftnode=nodeT.rightnode
          nodeT.leftnode.parent=nodeT.parent.leftnode

    else:
        if nodeT.rightnode.leftnode==None:
          nodeAux=nodeT.rightnode
          eliminaNode(nodeT.rightnode)
        elif nodeT.leftnode.rightnode==None:
          nodeAux=nodeT.leftnode
          eliminaNode(nodeT.leftnode)
        else:
          nodeAux=minDmax(nodeT.rightnode)
          nodeAux.parent=nodeT.parent
          nodeAux.rightnode=nodeT.rightnode
          nodeAux.leftnode=nodeT.leftnode
        if nodeAux.rightnode != None:
          nodeAux.rightnode.parent=nodeAux
        if nodeAux.leftnode !=None:
          nodeAux.leftnode.parent=nodeAux
        if nodeT.parent.rightnode==nodeT:
          nodeT.parent.rightnode=nodeAux
        else:
          nodeT.parent.leftnode=nodeAux
    return k
  else:
    if nodeT.rightnode!=None:
      return deleteR(nodeT.rightnode,k)
    if nodeT.leftnode!=None:
      return deleteR(nodeT.leftnode,k)      
 
