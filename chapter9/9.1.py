def stair_permutations(n):
    """Returns the number of different ways a child can hop up a staircase
    with n steps by hopping 1,2 or 3 steps at a time."""
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    return (stair_permutations(n - 1) +
            stair_permutations(n - 2) +
            stair_permutations(n - 3))


def stair_permutations2(n):
    """Iterative solution."""
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    a, b, c = 1, 1, 2
    for _ in xrange(n - 2):
        a, b, c = b, c, a + b + c
    return c

if __name__ == '__main__':
    for i in xrange(20):
        print stair_permutations(i), stair_permutations2(i)
