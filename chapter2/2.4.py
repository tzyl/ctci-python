import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.linkedlist import LinkedList, Node


def partition(linked_list, x):
    """Partitions a linked list around a value x so that all nodes less than x
    come before all nodes greater than or equal to x.
    """
    current = linked_list.head
    while current is not None:
        next_ = current.next
        if current.key < x:
            linked_list.delete(current)
            linked_list.insert(current)
        current = next_

linked_list = LinkedList()
for i in xrange(10):
    linked_list.insert(Node(i))
linked_list.traverse()
partition(linked_list, 5)
linked_list.traverse()
