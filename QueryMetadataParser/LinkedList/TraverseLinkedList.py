class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class LinkedList:
   def __init__(self):
      self.head_node = None

   def traverse_linked_list(self):
      printval = self.head_node
      print (printval)
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
         print (printval)


if __name__ == "__main__":
 list1 = LinkedList()
 list1.head_node = Node("Mon")
 e2 = Node("Tue")
 e3 = Node("Wed")
 print (e2)
 # Link first Node to second node
 list1.head_node.nextval = e2
 print (list1)
 # Link second Node to third node
 e2.nextval = e3

 objLinkedList = LinkedList()
 objLinkedList.traverse_linked_list()