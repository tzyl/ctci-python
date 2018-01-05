import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.stack import Stack


def sort_stack(stack, temp_stack):
    """Sorts a stack in ascending order (biggest item on top) using an
    additional stack for storage. First moves all items to the temporary stack
    then moves them back one by one into their correct position.
    """
    while not stack.stack_empty():
        temp_stack.push(stack.pop())
    while not temp_stack.stack_empty():
        to_insert = temp_stack.pop()
        insert(to_insert, stack, temp_stack)


def insert(to_insert, stack, temp_stack):
    position = 0
    while not stack.stack_empty():
        if stack.peek() < to_insert:
            # Found correct position
            break
        temp_stack.push(stack.pop())
        position += 1
    stack.push(to_insert)
    for _ in xrange(position):
        stack.push(temp_stack.pop())


def sort_stack_recursive(stack, temp_stack):
    if stack.stack_empty():
        return
    temp_stack.push(stack.pop())
    sort_stack_recursive(stack, temp_stack)
    to_insert = temp_stack.pop()
    insert(to_insert, stack, temp_stack)

stack = Stack()
temp_stack = Stack()
for i in xrange(10, 0, -1):
    stack.push(i)
stack.traverse()
sort_stack(stack, temp_stack)
stack.traverse()
