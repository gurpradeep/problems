class Node:
    def __init__(self,data):
        self.data = data
        self.next_element = None




class LinkedList:

    def __init__(self):
        self.head_node=None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    def insert_at_head(self,data):
        temp_node = Node(data)
        if self.is_empty():
            self.head_node = temp_node
            return self.head_node

        temp_node.next_element= self.head_node
        self.head_node=temp_node


    def insert_at_tail(self,data):
        new_node = Node(data)

        temp = self.head_node

        if is_empty():
            self.head_node=new_node

        while temp.next_element is not None:
            temp = temp.next_element
        temp.next_element = new_node
        return

    def length(self):
        length=0
        temp = self.head_node
        while temp.next_element is not None:
            length+=1
            temp = temp.next_element
        
        return length
        

