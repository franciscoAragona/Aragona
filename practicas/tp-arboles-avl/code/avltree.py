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
    cbf(node)
    cbfRecursive(node.rightnode)
    cbfRecursive(node.leftnode)
    return 
#calcula el bf de un nodo
def cbf(node):

    if node == None:
        return 
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
"""



