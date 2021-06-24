class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def longest_route(root):
    if not root: 
        return 0
    print("longest:",root.val)
    def height(node): 
        if node is None:
            print("height:Null")
        else:
            print("height:",node.val)

        if node is None: 
            return 0 ;  
        else : 
            # Compute the height of each subtree 
            lh = height(node.left) 
            rh = height(node.right) 

            # Use the larger one 
            return max(lh, rh) + 1
    
    l_height = height(root.left)
    r_height = height(root.right)
    l_path = longest_route(root.left)
    r_path = longest_route(root.right)
    
    res = max(l_height + r_height + 1, max(l_path, r_path))

    return res

# Driver code

root = TreeNode("a")
root.left = TreeNode("b")
root.right = TreeNode("c")
root.left.left = TreeNode("d")
root.right.left = TreeNode("e")
root.right.right = TreeNode("f")

print("The longest route will pass through", longest_route(root), "checkpoints")