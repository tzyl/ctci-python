class MinStack(object):
    def __init__(self):
        self.stack_size = 100
        self.stack = [None] * self.stack_size
        self.top = -1
        self.minimums = [None] * self.stack_size

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.stack_size - 1

    def push(self, x):
        if self.is_full():
            raise Exception("Stack overflow")
        new_min = min(self.min(), x) if self.min() is not None else x
        self.top += 1
        self.stack[self.top] = x
        self.minimums[self.top] = new_min

    def pop(self):
        if self.is_empty():
            raise Exception("Stack underflow")
        self.top -= 1
        return self.stack[self.top + 1]

    def min(self):
        if self.is_empty():
            return None
        return self.minimums[self.top]

if __name__ == "__main__":
    min_stack = MinStack()
    print min_stack.min()
    for i in reversed(xrange(10)):
        min_stack.push(i)
        print min_stack.min()
    for i in reversed(xrange(10)):
        min_stack.pop()
        print min_stack.min()
