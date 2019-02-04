"""
# Linked List Nth to Last Node - SOLUTION

## Problem Statement
Write a function that takes a head node and an integer value **n** and then returns the nth to last node in the linked
list. For example, given:
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


# solution
def nth_to_last_node(n, head):

    left_pointer = head
    right_pointer = head

    for i in range(n - 1):
        if not right_pointer.next_node:
            raise LookupError("Error: n is larger than the linked list")

        right_pointer = right_pointer.next_node

    while right_pointer.next_node:
        left_pointer = left_pointer.next_node
        right_pointer = right_pointer.next_node

    return left_pointer


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

# This would return the node d with a value of 4, because its the 2nd to last node.
print(nth_to_last_node(6, a).value)

