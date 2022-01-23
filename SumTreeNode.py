def sumleftright(node):
    if node is None:
        return 0
    else:
        return node.value

    leftsum = sumleftright(node.left) 
    rightsum =  sumleftright(node.right)
    node.value = leftsum + rightsum

def CalcRoot(node):
    if node is None:
        return 0
    else:
        return node.value

    




class Node(object):
    def __init()__(self,value):
        self.value = value 
        self.left = None
        self.right=None



class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)


tree = BinaryTree(10)
tree.root.left = Node(5)
tree.root.right = Node(7)
tree.root.left.left= Node(2)
tree.root.left.right= Node(3)
tree.root.right.left= Node(4)
tree.root.right.right= Node(6)
