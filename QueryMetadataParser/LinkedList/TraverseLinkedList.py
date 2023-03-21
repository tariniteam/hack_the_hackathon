class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # print method for the linked list
    def traverse_linked_list(self):
        element_list = []
        current = self.head
        while (current):
            #print(current.data)
            element_list.append(current.data)
            current = current.next
        return element_list

    def get_first_node_of_linked_list (self):
        if self.head is None:
            return None
        else:
            data = self.head.data
            if self.head is self.tail:
                self.tail = None
            self.head = self.head.next
            return data


    def get_last_node_of_linked_list (self):
        current = self.head
        print ("Head" , self.head)
        while (current ):
            last_node = current.data
            if (current.next is None):
                last_node = current.data
                #print("last node = ", last_node)
            current = current.next
        return last_node

if __name__ == "__main__":

 objLinkedList = LinkedList()
 objLinkedList.insert(3)
 objLinkedList.insert(4)
 objLinkedList.insert(5)
 element_list = objLinkedList.traverse_linked_list()
 print (element_list)
 last_node = objLinkedList.get_last_node_of_linked_list()
 print("last node = ", last_node)
 first_node = objLinkedList.get_first_node_of_linked_list()
 print("first node = ", first_node)