import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.linkedlist import LinkedList, Node


# class LinkedList(object):
#     """Doubly linked list"""
#     def __init__(self):
#         self.head = None

#     def search(self, k):
#         x = self.head
#         while x is not None and x.key != k:
#             x = x.next
#         return x

#     def insert(self, x):
#         x.next = self.head
#         if self.head is not None:
#             self.head.prev = x
#         self.head = x
#         self.prev = None

#     def delete(self, x):
#         if x.prev is not None:
#             x.prev.next = x.next
#         else:
#             self.head = x.next
#         if x.next is not None:
#             x.next.prev = x.prev


# class Node(object):
#     def __init__(self, key):
#         self.key = key
#         self.next = None
#         self.prev = None


def remove_duplicates(linked_list):
    """Removes duplicates in a linked list by keeping track of seen keys.2"""
    seen = set()
    x = linked_list.head
    while x is not None:
        if x.key in seen:
            print "Deleting duplicate with key %s" % x.key
            linked_list.delete(x)
        else:
            seen.add(x.key)
        x = x.next


def remove_duplicates2(linked_list):
    """Removes duplicates in a linked list without using a temporary buffer."""
    x = linked_list.head
    while x is not None:
        y = x.next
        while y is not None:
            if y.key == x.key:
                print "Deleting duplicate with key %s" % y.key
                linked_list.delete(y)
            y = y.next
        x = x.next

linked_list = LinkedList()
for _ in xrange(5):
    linked_list.insert(Node(1))
for _ in xrange(5):
    linked_list.insert(Node(2))
linked_list.traverse()
remove_duplicates2(linked_list)
linked_list.traverse()
