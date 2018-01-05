import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.linkedlist import LinkedListWithTail, Node


# def add_lists(list1, list2, reverse=True):
#     list3 = LinkedListWithTail()
#     def add(node1, node2, carry):
#         if node1 is None and node2 is None and carry == 0:
#             return None

#         value = carry
#         if node1 is not None:
#             value += node1.key
#         if node2 is not None:
#             value += node2.key

#         if not reverse and value >= 10:
#             list3.insert_tail(Node(value - (value % 10)))
#             value %= 10
#         list3.insert_tail(Node(value % 10))

#         if node1 is not None or node2 is not None:
#             add(node1.next if node1 is not None else None,
#                 node2.next if node2 is not None else None,
#                 1 if value > 10 else 0)
#     add(list1.head, list2.head, 0)
#     return list3


def add2(list1, list2):
    """Given two linked lists list1 and list2 where each node contains a single
    digit of a number stored in reverse order so the 1's digit is at the head,
    return the sum of the two numbers in a linked list in the same way.
    """
    i = 0
    x = 0
    current = list1.head
    while current is not None:
        x += current.key * (10 ** i)
        current = current.next
        i += 1
    i = 0
    y = 0
    current = list2.head
    while current is not None:
        y += current.key * (10 ** i)
        current = current.next
        i += 1
    z = x + y
    print x, y, z
    list3 = LinkedListWithTail()
    while z:
        list3.insert_tail(Node(z % 10))
        z /= 10
    return list3


def add3(list1, list2):
    """Same but for it the digits are stored in forward order."""
    digits = []
    current = list1.head
    while current is not None:
        digits.append(current.key)
        current = current.next
    x = reduce(lambda x, y: x*10 + y, digits)
    digits = []
    current = list2.head
    while current is not None:
        digits.append(current.key)
        current = current.next
    y = reduce(lambda x, y: x*10 + y, digits)
    z = x + y
    print x, y, z
    list3 = LinkedListWithTail()
    while z:
        list3.insert(Node(z % 10))
        z /= 10
    return list3

a, b = LinkedListWithTail(), LinkedListWithTail()
m, n = 132, 459
while m:
    a.insert(Node(m % 10))
    m /= 10
while n:
    b.insert(Node(n % 10))
    n /= 10

a.traverse()
b.traverse()
c = add2(a, b)
c.traverse()
c = add3(a, b)
c.traverse()
