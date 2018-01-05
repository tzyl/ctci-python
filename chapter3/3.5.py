import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.stack import Stack


class MyQueue(object):
    """Queue implemented using two stacks.
    Items are enqueued onto stack1.
    Items are dequeued from stack2. If stack2 is empty then all items in stack1
    are popped off and pushed onto stack 2 to maintain FIFO order.
    """
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, x):
        self.stack1.push(x)

    def dequeue(self):
        if self.stack2.stack_empty():
            while not self.stack1.stack_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

if __name__ == "__main__":
    queue = MyQueue()
    for i in xrange(5):
        queue.enqueue(i)
    queue.stack1.traverse()
    queue.stack2.traverse()
    print queue.dequeue()
    queue.stack1.traverse()
    queue.stack2.traverse()
    for i in xrange(10):
        queue.enqueue(i)
    queue.stack1.traverse()
    queue.stack2.traverse()
