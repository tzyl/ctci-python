import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.linkedlist import LinkedList, Node


def find_loop_start(linked_list):
    """Given a corrupt circular linked list returns the start of the loop."""
    slow = linked_list.head
    fast = linked_list.head
    i = 0
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        i += 1
        if fast == slow:
            # There exists a loop. Find out where it starts.
            # The head and this intersection position are k places away from
            # the start of the loop.
            head = linked_list.head
            while head is not slow:
                head = head.next
                slow = slow.next
            return head
    # No loop.
    return None


def find_loop_start2(linked_list):
    """Given a corrupt circular linked list returns the start of the loop.
    Probably not allowed to use Python set.
    """
    seen = set()
    current = linked_list.head
    while current is not None:
        if current in seen:
            return current
        seen.add(current)
        current = current.next
    return None

linked_list = LinkedList()
for i in xrange(10):
    linked_list.insert(Node(i))
# Set up a loop.
x = linked_list.search(0)
y = linked_list.search(5)
x.next = y
y.prev = x

print find_loop_start(linked_list).key
