class BST:
    def __init__(self, key): #Self-Object itself/instance of a class
        self.key = key
        self.lchild = None
        self.rchild = None

    # def update(node, key, value):
    #     target = find(node, key)
    #     if target is not None:
    #         target.value = value
    #
    # def list_all(node):
    #     if node is None:
    #         return []
    #     return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

    def insert(self, data): #O(log n)
        if self.key is None: #Empty node
            self.key = data
            return
        if self.key == data: #Ignoring duplicates
            return
        if self.key > data:
            if self.lchild: #If leftchild is present
                self.lchild.insert(data) #Recursion
            else: #If no leftchild
                self.lchild = BST(data) #Creating new node
        else:
            if self.rchild:  # If rightchild is  present
                self.rchild.insert(data)  # Recursion
            else:  # If no rightchild
                self.rchild = BST(data)  # Creating new node

    def search(self, data): #Same time complexity as insert
        if self.key == data:
            print("Node is found!")
            return
        if data < self.key: #Left subtree
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present")

    def preorder(self): #Traversing Root node --->Left subtree --->right subtree
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self): #Traversing Left subtree --->Root node --->right subtree
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self): #Traversing Left subtree --->right subtree --->Root node
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")

    def delete(self, data, curr): #curr = root.key
        if self.key is None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data, curr)
            else:
                print("Given Node is Not Present")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data, curr)
            else:
                print("Given Node is Not Present")
        else: #data==self.key
            if self.lchild is None:
                temp = self.rchild #If lchild is none, return rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild #If rchild is none, return lchild
                if data == curr: #If deleting the root node that contains 2 child node
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None #Self=root
                return temp
            node = self.rchild
            while node.lchild: #Finding the smallest node in the right subtree
                node = node.lchild #Smallest node in the right subtree
            self.key = node.key
            self.rchild = self.rchild.delete(node.key, curr)
        return self

    def min_node(self):
        current = self #self=root
        while current.lchild:
            current = current.lchild
        print("Node with smallest key is:", current.key)

    def mmax_node(self):
        current = self #self=root
        while current.rchild:
            current = current.rchild
        print("Node with largest key is:", current.key)



def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)


root = BST(11)
list1 = [10, 4, 30, 7, 4, 8, 20, 70]
for i in list1:
    root.insert(i)

print(count(root))

# root.search(4)
print("Preorder")
root.preorder()
print()
print("Inorder")
# root.inorder()
print()
print("PostOrder")
# root.postorder()
if count(root) > 1: #If root node is the leaf node
    root.delete(11, root.key)
else:
    print("Can't perform deletion operation")
print("After Deleting")
root.preorder()

root.min_node()
root.mmax_node()


def delete(self, val):
    if val < self.data:
        if self.left:
            self.left = self.left.delete(val)
    elif val > self.data:
        if self.right:
            self.right = self.right.delete(val)
    else:
        if self.left is None and self.right is None:
            return None
        elif self.left is None:
            return self.right
        elif self.right is None:
            return self.right

        max_val = self.left.find_max()
        self.data = max_val
        self.left = self.left.delete(max_val)

        min_val = self.right.find_min()
        self.data = min_val
        self.right = self.right.delete(min_val)

    return self



# Complexity of the various operations in a balanced BST:
#
# Insert - O(log N) + O(N) = O(N)
# Find - O(log N)
# Update - O(log N)
# List all - O(N)