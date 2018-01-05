import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.stack import StackArray
from datastructures.linkedlist import LinkedList


class SetOfStacks(LinkedList):
    def __init__(self):
        super(SetOfStacks, self).__init__()
        self.stack_size = 4
        self.stack_count = 0

    def push(self, x):
        # Check if we need to create a new stack.
        if self.head is None or self.head.stack.stack_full():
            self.insert(StackNode(self.stack_count, self.stack_size))
            self.stack_count += 1
        self.head.stack.push(x)

    def pop(self):
        # Check if we need to remove a stack.
        if self.head.stack.stack_empty():
            self.delete(self.head)
            self.stack_count -= 1
        if self.head is None:
            raise Exception("Set of stacks underflow")
        return self.head.stack.pop()

    def pop_at(self, stack_index):
        # Discuss whether it is worth the added time complexity to maintain
        # stacks to be at full capacity if we implement pop_at.
        stack = self.search(stack_index)
        value = stack.stack.pop()
        self.fix_stack(stack)
        return value

    def fix_stack(self, stack):
        if stack.stack.stack_empty():
            self.delete(stack)
        elif stack.prev is not None:
            # Move items to fill up hole.
            temp = StackArray(self.stack_size)
            while not stack.prev.stack.stack_empty():
                temp.push(stack.prev.stack.pop())
            while not temp.stack_empty() and not stack.stack.stack_full():
                stack.stack.push(temp.pop())
            while not temp.stack_empty():
                stack.prev.stack.push(temp.pop())
            self.fix_stack(stack.prev)


class StackNode(object):
    def __init__(self, key, stack_size):
        self.key = key
        self.stack = StackArray(stack_size)
        self.next = None
        self.prev = None


def traverse_set_of_stacks(set_of_stacks):
    x = set_of_stacks.head
    while x is not None:
        print "Stack index: %s" % x.key
        print x.stack.data
        x = x.next

if __name__ == "__main__":
    set_of_stacks = SetOfStacks()
    for i in xrange(13):
        print "PUSHING"
        set_of_stacks.push(i)
    traverse_set_of_stacks(set_of_stacks)
    for _ in xrange(6):
        print "POPPING"
        print set_of_stacks.pop()
    traverse_set_of_stacks(set_of_stacks)
    print set_of_stacks.pop_at(0)
    traverse_set_of_stacks(set_of_stacks)
