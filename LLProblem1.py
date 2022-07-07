# Write a function to delete a node in a singly-linked list. You will not be given access to the head
# of the list, instead you will be given access to the node to be deleted directly
# It is guqranteed that the node to be deleted is not a tail node in the list.
# The trick here is we can copy the data of the next node to the data field of the current node to be deleted. Then we can
# move one step forward. Now our next has become the current node and the current has become the previous node. Now we can
# easily delete the current node by conventional deletion methods.

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next