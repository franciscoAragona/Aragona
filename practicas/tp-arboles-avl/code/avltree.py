class AVLTree:
    root = None

class n:
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
    avlnode = avl.root

