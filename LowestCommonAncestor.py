class TreeNode(object): 
     
     def __init__(self, val):
        self.val = val
        self.children = []

     def lowest_common_ancestor(root, a,b):
        def findNode(root, givenNode):
            if root is givenNode:
                return givenNode
            else:
                return None


            for child in root.children:
                findNode(child,givenNode )
            
         
                
        a_node = findNode(root,a)
        b_node = findNode(child,b)

        if a_node == b_node:
            return
def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    printer()

root = TreeNode(1)
root.children.append(TreeNode(3))
root.children.append(TreeNode(4)) 
root.children[0].children.append(TreeNode(5)) 
root.children[0].children[0].children.append(TreeNode(10)) 
root.children[0].children.append(TreeNode(6)) 
root.children[0].children[1].children.append(TreeNode(11))
root.children[0].children[1].children.append(TreeNode(12))
root.children[0].children[1].children.append(TreeNode(13)) 
root.children[2].children.append(TreeNode(7))
root.children[2].children.append(TreeNode(8))
root.children[2].children.append(TreeNode(9))

a = root.children[0].children[1].children[2]
b = root.children[0].children[0].children[0]
LCA = lowest_common_ancestor(root, a, b)
print("\"", LCA, "\"", "is the lowest common ancestor of the nodes", "\"", a.val, "\"", "and", "\"", b.val, "\"")