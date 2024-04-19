class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False

T=Trie()
T.root=TrieNode()
A=TrieNode()
A.key="d"
T.root.children=[A]
lee(T.root)

def lee(node):
    if node != None:
        print(node.key)
        lee(node.children)
    else:
        return
    