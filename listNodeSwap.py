class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next=None


class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

def nodeSwap2(head):
    if head is None or head.next is None:
        return head

    nextNode = head.next
    head.next = nodeSwap(head.next.next)
    nextNode.next = head
    return nextNode

def nodeSwap(head):

    tempNode = Node(-1)
    tempNode.next=head
    prevNode=tempNode
    while prevNode.next is not None or prevNode.next.next is not None:

        firstNode = prevNode.next
        secondNode = prevNode.next.next

        firstNode = secondNode.next
        secondNode.next = firstNode
        prevNode.next=secondNode

        prevNode = firstNode

    return tempNode.next         

if __name__ == '__main__':
    llist = LinkedList()
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)
    fourth=Node(4)
    five=Node(5)
    
    llist.head.next=second
    second.next=third
    third.next=fourth
    fourth.next=five

    llist.head = nodeSwap(llist.head)
    llist.printList()
    