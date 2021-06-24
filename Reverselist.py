class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 
    
    def print_list(head): 
        while head is not None: 
            print("===============")
            print ("-->", head.data) 
            head = head.next 
    
    def reverse_list_recursive(head): 
        if head is None or head.next is None: 
            return head 
        p = head.next 
        head.next = None 
        revrest = Node.reverse_list_recursive(p) 
        p.next = head  
        return revrest 

    def rev_list_recursive(head): 
        if head is None or head.next is None:
            return head

        p = head.next
        head.next = None
        rev_head = Node.rev_list_recursive(p)
        p.next = head
        return rev_head
        

    def rev_list_iterative(head): 
        
        current = head
        prev=None
        next = None
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev



node1 = Node(1)    
node2 = Node(2)    
node3 = Node(3)    
node4 = Node(4)    
node5 = Node(5)    

node1.next = node2 
node2.next = node3 
node3.next = node4 
node4.next = node5 
head = node1 
Node.print_list(head) 
head = node1 
#head = Node.rev_list_recursive(head) 
head = Node.rev_list_iterative(head) 
Node.print_list(head)

