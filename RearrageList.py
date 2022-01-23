class Node(object):
    def __init__(self,data) -> None:
        self.data=data
        self.next = None
    
    def printList(self):
        temp = self
        while (temp):
            print(str(temp.data) + "-->",end="")
            temp = temp.next


def reorder(head):

    midNode = findmid(head)
    midHead = reverseMidtoEnd(midNode)
    newHead = insertL(head,midHead)
    return newHead

def findmid(head):
    slow,fast=head,head
    while(fast.next is not None and fast.next.next is not None):
        slow = slow.next
        fast=fast.next.next
    return slow    

def reverseMidtoEnd(head):
    p1,p2 = None,head

    while (p2 is not None):
        p3 = p2.next
        p2.next=p1
        p1=p2
        p2=p3
    return p1


def insertL(head,midhead):
    origHead = head

    while (head is not None and midhead is not None):
        temp = head.next
        head.next = midhead
        head = temp

        temp = midhead.next
        midhead.next = head
        midhead = temp
    
    return origHead 

    
  
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    printNode = reorder(head)
    printNode.printList()


main()