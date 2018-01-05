import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.linkedlist import LinkedList, Node


def delete(x):
    """Deletes node x from singly linked list given only access to x.
    Note: Will not work if x is the last node in list. Maybe mark the node
    as dummy to deal with this case. This method still has side effects if
    there are external pointers to nodes as this does not actually delete the
    node but tries to mimic it.
    """
    if x is None or x.next is None:
        return False
    x.key, x.next = x.next.key, x.next.next
    return True

linked_list = LinkedList()
for i in xrange(10):
    linked_list.insert(Node(i))
linked_list.traverse()
print delete(linked_list.search(5))
linked_list.traverse()
