import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.linkedlist import LinkedList, Node


def get_from_end(linked_list, k):
    """Returns the kth to last element from linked_list."""
    x = linked_list.head
    y = linked_list.head
    for _ in xrange(k):
        if y is None:
            print "Not enough elements to get %sth from last!" % k
        y = y.next
    while y is not None:
        x = x.next
        y = y.next
    return x


def get_from_end_recursive(linked_list, k):
    def _get_from_end_recursive(current, k):
        if current is None:
            return None, 0
        node, i = _get_from_end_recursive(current.next, k)
        i += 1
        if i == k:
            return current, i
            print current.key
        return node, i
    return _get_from_end_recursive(linked_list.head, k)[0]

linked_list = LinkedList()
for i in xrange(10):
    linked_list.insert(Node(i))
for i in xrange(1, 11):
    print get_from_end(linked_list, i).key
    print get_from_end_recursive(linked_list, i).key
