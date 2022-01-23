class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#class Linked List
class LinkedList:
  def __init__(self):
    self.head = None

  #Add new element at the end of the list
  def push_back(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      temp = self.head
      while(temp.next != None):
        temp = temp.next
      temp.next = newNode

  #display the content of the list
  def PrintList(self,head):
    temp = head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

  def node_swap(self,head):
      if head is None or head.next is None:
          return head
      
      nextNode = head.next
      head.next = self.node_swap(head.next.next)
      nextNode.next = head
      return nextNode

  def node_swap2(self,head):
      tempNode = Node(0)
      tempNode.next= head

      prevNode = tempNode
      while prevNode.next is not None and prevNode.next.next is not None:
          firstNode = prevNode.next
          secondNode = prevNode.next.next

          firstNode.next = secondNode.next
          secondNode.next = firstNode
          prevNode.next = secondNode

          prevNode = firstNode

      return tempNode.next 

          
# test the code                  
MyList = LinkedList()

#Add three elements at the end of the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.push_back(40)
MyList.push_back(50)
MyList.push_back(60)
MyList.PrintList(MyList.head)
MyList.PrintList(MyList.node_swap2(MyList.head))
