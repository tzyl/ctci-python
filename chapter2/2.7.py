import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.linkedlist import LinkedList, Node


def check_palindrome(linked_list):
    stack = []
    slow = linked_list.head
    fast = linked_list.head
    while fast is not None and fast.next is not None:
        stack.append(slow.key)
        slow = slow.next
        fast = fast.next.next
    if fast is not None:
        # odd length need to move along one more.
        slow = slow.next
    while slow is not None:
        if slow.key != stack.pop():
            return False
        slow = slow.next
    return True


def check_palindrome_recursive(linked_list):
    length = size(linked_list)
    def _check_palindrome(head, length):
        if length == 0:
            return head, True
        elif length == 1:
            return head.next, True
        to_check, valid = _check_palindrome(head.next, length - 2)
        if not valid or head.key != to_check.key:
            return None, False
        return to_check.next, True
    return _check_palindrome(linked_list.head, length)[1]


def size(linked_list):
    size = 0
    x = linked_list.head
    while x is not None:
        size += 1
        x = x.next
    return size


def check_palindrome2(linked_list):
    """Relies on doubly linked list."""
    x = linked_list.head
    while x.next is not None:
        x = x.next
    y = linked_list.head
    while y is not None:
        if x.key != y.key:
            return False
        x = x.prev
        y = y.next
    return True

a = LinkedList()
for i in xrange(9):
    a.insert(Node(i))
for i in reversed(xrange(9)):
    a.insert(Node(i))
a.traverse()
print check_palindrome_recursive(a)
