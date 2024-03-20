import avltree

class AVLTree:
    root = None

class AVLnode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None

def lee(B,c):
    if B!=None:
        print(c,B.value, "/", B.bf)
    else:
        return
        
    if B.leftnode!=None:
        lee(B.leftnode,"L ")
    if B.rightnode!=None:
        lee(B.rightnode,"R ")

B=AVLTree()
B.root=AVLnode()
#B.root.key=1
B.root.value=10
B.root.leftnode=AVLnode()
B.root.leftnode.value=5
#B.root.leftnode.key=2
#B.root.leftnode.parent=B.root
B.root.leftnode.leftnode=AVLnode()
B.root.leftnode.leftnode.value=4
#B.root.leftnode.leftnode.key=22
#B.root.leftnode.leftnode.parent=B.root.leftnode
B.root.leftnode.leftnode.leftnode=AVLnode()
B.root.leftnode.leftnode.leftnode.value=2
#B.root.leftnode.leftnode.leftnode.leftnode=AVLnode()
#B.root.leftnode.leftnode.leftnode.leftnode.value=1
B.root.leftnode.rightnode=AVLnode()
B.root.leftnode.rightnode.value=6
#B.root.leftnode.rightnode.key=23
#B.root.leftnode.rightnode.parent=B.root.leftnode
B.root.rightnode=AVLnode()
B.root.rightnode.value=15
B.root.rightnode.rightnode=AVLnode()
B.root.rightnode.rightnode.value=20
B.root.rightnode.leftnode=AVLnode()
B.root.rightnode.leftnode.value=12
B.root.rightnode.rightnode.rightnode=AVLnode()
B.root.rightnode.rightnode.rightnode.value=30

#B.root.rightnode.key=3
#B.root.rightnode.parent=B.root
lee(B.root,"Root ")
#print(avltree.height(B.root))
avltree.calculateBalance(B)
lee(B.root,"Root ")