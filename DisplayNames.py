class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self.root.insert(val)
class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, val):
        if self is None:
            self = Node(val)
            return
        current = self
        while current:
            parent = current
            if val < current.val:
                current = current.leftChild
            else:
                current = current.rightChild

        if(val < parent.val):
            parent.leftChild = Node(val)
        else:
            parent.rightChild = Node(val)

class DisplayLobby: 
    
    def __init__(self, root):
        self.stack = list()
        self.push_all(root)

    def push_all(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.leftChild

    def has_next(self):
        return len(self.stack) > 0

    def next_name(self):
        tmpNode = self.stack.pop()
        self.push_all(tmpNode.rightChild)
        return tmpNode.val

    def next_page(self):
        res = []
        for i in range(0, 10):
            if self.has_next():
                res.append(self.next_name())
            else:
                break
        return res

## Driver code

# creating the tree for demo
bst = BinarySearchTree()
names = ["Jeanette", "Latasha", "Elvira", "Caryl", "Antoinette", "Cassie", "Charity", "Lyn", "Elia", "Anya", "Albert", "Cherlyn", "Lala", "Kandice", "Iliana"]
for name in names:
    bst.insert(name)

display = DisplayLobby(bst.root)
print(display.next_page())
print(display.next_page())