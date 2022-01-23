from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if root is None: 
      return root

    right = invert_tree(root.right);
    left = invert_tree(root.left);
    root.left = right;
    root.right = left;
    return root;

def print_tree(root):
    q = deque()
    q.append(root)
    while q:
        curr=q.popleft()
        print(curr.val, end=' ')
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

# Driver Code
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print_tree(invert_tree(root))