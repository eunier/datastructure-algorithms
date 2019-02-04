"""
# Linked List Reversal - SOLUTION

## Problem

Write a function to reverse a Linked List in place. The function will take in the head of the list as input and return
the new head of the list.
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


# solution here
def reverser(head):
    current = head
    previous = None

    while current:
        next_node = current.next_node
        current.next_node = previous
        previous = current
        current = next_node

    return previous


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)

# Set up order a,b,c,d with values 1,2,3,4
a.next_node = b
b.next_node = c

print(str(a.value) + " - " + str(a.next_node.value))
print(str(b.value) + " - " + str(b.next_node.value))

reverser(a)
print()
print(str(b.value) + " - " + str(b.next_node.value))
print(str(c.value) + " - " + str(c.next_node.value))



