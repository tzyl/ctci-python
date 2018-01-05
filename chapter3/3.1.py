class TripleStack(object):
    def __init__(self):
        self.stack_size = 100
        self.stack_pointers = [-1, -1, -1]
        self.stack = [None] * 3 * self.stack_size

    def top_of_stack(self, stack_number):
        return stack_number*self.stack_size + self.stack_pointers[stack_number]

    def push(self, stack_number, x):
        if self.stack_pointers[stack_number] + 1 > self.stack_size:
            raise Exception("Stack overflow")
        self.stack_pointers[stack_number] += 1
        self.stack[self.top_of_stack(stack_number)] = x

    def pop(self, stack_number):
        if self.stack_pointers[stack_number] == -1:
            raise Exception("Stack underflow")
        self.stack_pointers[stack_number] -= 1
        return self.stack[self.top_of_stack(stack_number) + 1]

    def peek(self, stack_number):
        if self.stack_pointers[stack_number] == -1:
            raise Exception("Stack underflow")
        return self.stack[self.top_of_stack(stack_number)]

    def is_empty(self, stack_number):
        return self.stack_pointers[stack_number] == -1
