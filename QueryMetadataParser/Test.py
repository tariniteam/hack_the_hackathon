class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

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
        pass

    def get_last_node_of_linked_list (self):
        current = self.head
        print (self.head)
        while (current):
            last_node = current.data
            current = current.next
            print (current.next)
            #if current.next == 'NULL':
                #last_node = current.data
                #print ("last node", last_node)
        return last_node


# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
element_list = LL.traverse_linked_list()
print (element_list)
last_node = LL.get_last_node_of_linked_list()