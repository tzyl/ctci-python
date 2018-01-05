import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.stack import StackArray


class Tower(StackArray):
    def push(self, x):
        if not self.stack_empty():
            if x >= self.peek():
                raise Exception("Can't place larger disk on smaller disk!")
        super(Tower, self).push(x)


def towers_of_hanoi(N):
    """Moves the tower of increasing height N...1 on stack1 to stack 3."""
    # Initialize problem.
    tower1 = Tower(N)
    tower2 = Tower(N)
    tower3 = Tower(N)
    for i in xrange(N, 0, -1):
        tower1.push(i)

    print tower1.data
    print tower2.data
    print tower3.data

    def move(n, start, finish, temp):
        """Moves an increasing sequence of n blocks from start stack to finish
        stack using the temp stack as buffer storage.
        """
        if n == 1:
            finish.push(start.pop())
        else:
            move(n - 1, start, temp, finish)
            finish.push(start.pop())
            move(n - 1, temp, finish, start)

    move(N, tower1, tower3, tower2)

    print tower1.data
    print tower2.data
    print tower3.data

if __name__ == "__main__":
    towers_of_hanoi(12)
