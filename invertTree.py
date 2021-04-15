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
        
        
def invert_tree(root,level,rightorleft):
    level = level + 1
    if root:
        str1 = str(root.value) + " Level: "+ str(level)  
        str3=""
        if rightorleft ==0:
          str3 = str1 + "--LeftNode"  
        
        if rightorleft ==1:
          str3 = str1 + "--RightNode"

        print("Current root value",str3,end='\n')
        root.left,root.right = invert_tree(root.right,level,1),invert_tree(root.left,level,0)
        return root
    else:
        str4=""
        str2 = " Level: "+ str(level) 
        if rightorleft ==0:
          str4 = str2 + "--LeftNode"  
        
        if rightorleft ==1:
          str4 = str2 + "--RightNode"
 
        print("Leaf node",str4,end='\n')
        




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print_tree(root)
print("",end='\n')
print("****Inverse****")
print_tree(invert_tree(root,0,-1))
