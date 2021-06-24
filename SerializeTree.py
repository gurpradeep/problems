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



class Translator:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        def pre_order(root):
            if root:
                res.append(str(root.val) + ",")
                pre_order(root.leftChild)
                pre_order(root.rightChild)
            
        res = []
        pre_order(root)
        return "".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        lst = data.split(",")
        lst.pop()
        root = None
        for n in lst:
            if not root:
                root = Node(n)
            else:
                root.insert(n)
        return root

## Driver code
names = ["Jeanette", "Elia", "Albert", "Latasha", "Elvira", "Kandice", "Maggie"]
bst = BinarySearchTree()
for name in names:
    bst.insert(name)

print("Original BST:")
#printTree(bst.root)

trans = Translator()
string = trans.serialize(bst.root)
print("\nSerialized: " + string)

deserialized = trans.deserialize(string)
print("\nDeserialized:")
#printTree(deserialized)