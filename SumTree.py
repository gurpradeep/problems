from collections import deque

class TreeNode(object):
   def __init__(self, value=0, left=None, right=None ):
       self.value = value
       self.left = left
       self.right = right

def print_tree(root):

    q = deque()
    q.append(root)
    while q:
        curr=q.popleft()
        print(curr.value, end=' ')
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
        
        
def sum_tree(root):
    val_array=[]
    def sum_tree_helper(root,sum_value,val_array):
        if root is None:
            return

        sum_value=sum_value+(root.value)
        if root.left is None and root.right is None:
            val_array.append(sum_value)
            return

        sum_tree_helper(root.left,sum_value,val_array) 
        sum_tree_helper(root.right,sum_value,val_array)
        
    sum_tree_helper(root,0,val_array)
    return val_array

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

root.left.left = TreeNode(4)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(10)

val_array=[]
print(sum_tree(root))
