class AVLTree:
    root = None

class AVLnode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None

def rotateLeft(avl,avlnode) :

    newroot = avlnode.rightnode

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

def rotateRight(avl,avlnode) :

    newroot = avlnode.leftnode

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

def calculateBalance(avl) :
    return cbf(avl.root)

def cbf(node):

    if node == None:
        return 
    rh=height(node.rightnode)
    lh=height(node.leftnode)
    print(lh-rh)
    node.bf=lh-rh
    cbf(node.rightnode)
    cbf(node.leftnode)

def height(avlnode) :
    if avlnode is None :
        return -1 

    rh = 1 + height(avlnode.rightnode)  
    lh = 1 + height(avlnode.leftnode)
    
    return max(rh,lh)
