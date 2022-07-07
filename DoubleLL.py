class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None #Next reference
        self.pref = None #Previous reference

class doublyLL:
    def __init__(self):
        self.head = None

# Forward Traversing:
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,  "--->", end=" ")
                n = n.nref

# Backward Traversing
    def print_LL_reverse(self):
        print()
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n.nref is not None: #Reach to the last node
                n = n.nref
            while n is not None: #Reversing until you reach the first node
                print(n.data, "--->", end=" ")
                n = n.pref

    def insert_empty(self, data): #Inserting when the LL is empty
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")

    def add_begin(self, data):
        new_node = Node(data) #Creates a new node
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head #Change new node nref
            self.head.pref = new_node #Change first node ref
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head # n is the first node
            while n.nref is not None: #Reach to the last node
                n = n.nref #Go to the next node
            n.nref = new_node #Change the nref of last node to the new node
            new_node.pref = n

# 1st way:
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.nref
        if n is None:
            print("Given Node is not presnt in Linked List!")
        elif n.nref is None:
            new_node = Node(data)
            n.nref = new_node
            new_node.pref = n
        else:
            new_node = Node(data)
            n.nref.pref = new_node
            new_node.nref = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is Empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            self.head.pref = new_node
            new_node.nref = self.head
            self.head = new_node
            return
        n = self.head
        while n.nref is not None:
            if x == n.nref.data:
                break
            n = n.nref
        if n.nref is None:
            print("Given Node is not presnt in Linked List!")
        else:
            new_node = Node(data)
            new_node.pref = n
            new_node.nref = n.nref
            n.nref.pref = new_node
            n.nref = new_node


# 2nd way:
    def add_afterr(self, data, x):
        if self.head is None:
            print("LL is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref # Move to the next node
            if n is None:
                print("Given Node is not present in DLL")
            else: # We found x
                new_node = Node(data) # Create node using node class
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None: #Checking if we are inserting after the last node
                    n.nref.pref = new_node
                n.nref = new_node


    def add_beforer(self, data, x):
        if self.head is None:
            print("LL is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present in DLL")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None: # Checking if we are inserting new node before the first node
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

    def delete_begin(self):
        if self.head is None: #Check if DLL is empty
            print("DLL is empty can't delte !")
            return
        if self.head.nref is None: #Check if DLL contains only one node
            self.head = None
            print("DLL is empty after deleting the node!")
        else: #DLL contains more than 1 node
            self.head = self.head.nref #Point head to the next node
            self.head.pref = None #Pref of the first node now becomes none

    def delete_end(self):
        if self.head is None:
            print("DLL is empty can't delte !")
            return
        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting the node!")
        else: #DLL contains more than one node
            n = self.head #First node
            while n.nref is not None: #Not the last node
                n = n.nref #Go to the next node
            n.pref.nref = None #Change the nref of the 2nd last node to none so as to delete the last node

    def delete_by_value(self, x):
        if self.head is None:
            print("DLL is empty can't delte !")
            return
        if self.head.nref is None: #If DLL contains only one node
            if x == self.head.data:
                self.head = None
            else:
                print("x is not present in DLL")
            return
        if self.head.data == x: #Deleting the first node if Contains more than one node
            self.head = self.head.nref #Point head to the next node
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None: #Deleting the middle node
            if x == n.data:
                break
            n = n.nref #Move to the next node
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x: #Deleting the last node
                n.pref.nref = None
            else:
                print("x is not present in dll!")

dl1 = doublyLL()
# dl1.insert_empty(10)
dl1.add_begin(20)
# dl1.delete_begin()
# dl1.delete_end()
dl1.add_afterr(50, 20)
dl1.add_beforer(70, 20)
dl1.add_end(100)
dl1.print_LL()
dl1.print_LL_reverse()