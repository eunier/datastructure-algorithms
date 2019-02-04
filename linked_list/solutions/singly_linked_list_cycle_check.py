"""# Implement a Queue - Using Two Stacks

Given the Stack class below, implement a Queue class using **two** stacks! Note, this is a "classic" interview problem.
Use a Python list data structure as your Stack.
"""


class Node(object):
    def __init__(self, value):
        self.node = value
        self.next_node = None


def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker2 is not None and marker2.next_node is not None:
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        if marker2 == marker1:
            return True

    return False


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""


# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
# Cycle Here!
c.next_node = a


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.next_node = y
y.next_node = z

print(cycle_check(a))
print(cycle_check(b))
print(cycle_check(c))

print(cycle_check(x))
print(cycle_check(y))
print(cycle_check(z))
