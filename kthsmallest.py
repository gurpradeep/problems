class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.leftNodes=1

def insertBST(root,node):
    if root is None:
        return None
    else:
        if root.data > node.data:
            root.leftNodes+=1
            if root.left==None:
                root.left=node
            else:
                insertBST(root.left,node)
        else:
            if root.right is None:
                root.right = node
            else:
                insertBST(root.right,node)
count =0
def kth_smallest_in_BST(root,k):

    global count
    if root is None:
        return root
    
    left = kth_smallest_in_BST(root.left,k)

    if left:
        return left
    count+=1
    if(count==k):
        return root
        
    return kth_smallest_in_BST(root.right,k)


node1,node2, node3, node4,node5, node6 = BSTNode(6),BSTNode(3),BSTNode(8),BSTNode(1),BSTNode(4),BSTNode(7)

node1.left,node1.right = node2,node3
node2.left,node2.right = node4,node5
node3.left=node6
result = kth_smallest_in_BST(node1,5)
print(result.data)

