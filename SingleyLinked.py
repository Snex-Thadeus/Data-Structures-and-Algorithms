# Traversing a Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):  # Traversing a Node
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data) # Creates a new Node
        if self.head is None:  # Checks is the Linked list is empty
            self.head = new_node # The new created node
        else:
            n = self.head # The link of the first reference
            while n.ref is not None: # Not pointing to the last node
                n = n.ref
            n.ref = new_node # We change the reference of the last node to the new node added

    def add_after(self, data, x): # Adding after a given node
        n = self.head
        while n is not None: # To traverse the entire LL
            if x == n.data: # It means we got the x node
                break
            n = n.ref #Assign a new value to n
        if n is None:
            print("node is not present in LL")
        else:
            new_node = Node(data) # Create the node with data using Class Node
            new_node.ref = n.ref
            n.ref = new_node # New node is the reference of n

    def add_before(self, data, x): # Adding  before given/first node
        if self.head is None: # Check whether LL is empty
            print("Linked List is empty!")
            return
        if self.head.data == x: # Checking if we are adding before the first node/at the beginning
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None: # Looping till the last node where n.ref=None
            if n.ref.data == x: # Checking for previous node of x
                break
            n = n.ref # Move to the next node
        if n.ref is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref # Changing the reference of the new node
            n.ref = new_node # Changing the reference of n to new node

    def insert_empty(self, data): # Adding elements to an empty LL
        if self.head is None: # If it's empty
            new_node = Node(data)
            self.head = new_node # Storing the reference of the new node in the head
        else:
            print("Linked List is not empty!")

    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty can't delete!")
        else:
            self.head = self.head.ref #Point head to the refernce of the second node

    def delete_end(self):
        if self.head is None:
            print("Linked List is empty can't delete!")
        elif self.head.ref is None: # When we have only one node
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None: # Searching 2nd last node
                n = n.ref #Incremenent the ref togo to the next value
            n.ref = None # Assigning the 2nd last node ref to none so as to delete the last node

    def delete_by_value(self, x):
        if self.head is None:
            print("Linked List is empty, can't delete!")
            return
        if x==self.head.data:
            self.head = self.head.ref #Delete first node
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present in the LL")
        else:
            n.ref = n.ref.ref




LL1 = LinkedList()
# LL1.add_begin(10)
LL1.add_end(100)
LL1.add_before(500, 100) # x=100
LL1.add_begin(20)
# LL1.delete_end()
LL1.delete_by_value(10)
# LL1.delete_begin()
# LL1.insert_empty(70)
LL1.print_LL()