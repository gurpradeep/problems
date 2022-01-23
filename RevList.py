from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse(sublist_start,sublist_end):
    prevNode, currNode = None, sublist_start
    while currNode !=sublist_end:
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
    return prevNode

def reverse_sub_list(head,p,q):
    
    sublist_start,sublist_end=0,0
    prev,curr,next = None,head,None
    prev_list=None
    index=0
    while curr is not None:
        index+=1
        if index==p:
            prev_list=prev
            sublist_start=curr
        if index== q:
            sublist_end=curr
            next_list = curr.next
            break
        prev=curr
        curr = curr.next

    rev_head = reverse(sublist_start,sublist_end.next)
    prev_list.next = rev_head
    sublist_start.next=next_list 
    return head

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head,2,4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()