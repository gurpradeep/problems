class TreeNode:
  def __init__(self, val):
    self.val = val
    self.next = None
    self.children = []

def traversing_dom_tree(root):
    
    if not root:
        return root
    
    def process_child(child_node, prev, leftmost):
        if child_node:
            
            # If we found atleast one node on the new level,
            # setup its next pointer
            if prev:
                prev.next = child_node
            else:    
                # It is the first node
                leftmost = child_node

            prev = child_node 
        return prev, leftmost
    
    leftmost = root
    
    # Traverse till last node
    while leftmost:
        
        # "prev" tracks the latest node on the "next" level
        # "curr" tracks the latest node on the current level

        prev, curr = None, leftmost
        
        leftmost = None
        
        # Iterate on the nodes of current level like a linked list

        while curr:
            
            print(curr.val)
            # Process all the children and update the prev
            # and leftmost pointers as necessary.
            for child in curr.children:
                prev, leftmost = process_child(child, prev, leftmost)
            
            curr = curr.next
            
    return root 




# Driver Code

root = TreeNode("body")
root.children.append(TreeNode("div"))
root.children.append(TreeNode("h1"))
root.children.append(TreeNode("div")) 
root.children[0].children.append(TreeNode("h2")) 
root.children[0].children[0].children.append(TreeNode("ul")) 
root.children[0].children.append(TreeNode("h3")) 
root.children[0].children[1].children.append(TreeNode("a"))
root.children[0].children[1].children.append(TreeNode("p"))
root.children[0].children[1].children.append(TreeNode("table")) 
root.children[2].children.append(TreeNode("p"))
root.children[2].children.append(TreeNode("a"))
root.children[2].children.append(TreeNode("p"))

res = traversing_dom_tree(root)