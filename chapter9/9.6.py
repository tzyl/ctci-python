def print_valid_parentheses(n):
    """Prints all valid combinations of n-pairs of parentheses."""
    for seq in get_valid_parentheses2(n, 0, 0):
        print seq


# INITIAL SOLUTION WRONG.
def get_valid_parentheses(n):
    if n == 1:
        return set(["()"])
    p = set()
    for seq in get_valid_parentheses(n - 1):
        p.add("()" + seq)
        p.add(seq + "()")
        p.add("(" + seq + ")")
    return p


# Avoids duplicates. SLOW
def get_valid_parentheses2(n, i, j):
    if i == n and j == n:
        return [""]
    p = []
    if i < n:
        p.extend(["(" + s for s in get_valid_parentheses2(n, i + 1, j)])
    if j < i:
        p.extend([")" + s for s in get_valid_parentheses2(n, i, j + 1)])
    return p


# Better avoid duplicates. FASTER
def get_valid_parentheses3(n):
    p = []
    s = ""
    add_parentheses(p, n, n, s)
    return p


def add_parentheses(p, open_remaining, close_remaining, s):
    if open_remaining == close_remaining == 0:
        p.append(s)
    if open_remaining > 0:
        add_parentheses(p, open_remaining - 1, close_remaining, s + "(")
    if close_remaining > open_remaining:
        add_parentheses(p, open_remaining, close_remaining - 1, s + ")")

if __name__ == '__main__':
    # import time
    # print_valid_parentheses(3)
    # start = time.time()
    # get_valid_parentheses3(13)
    # print time.time() - start
    # start = time.time()
    # get_valid_parentheses2(13, 0, 0)
    # print time.time() - start
    for i in xrange(1, 10):
        print len(get_valid_parentheses3(i))
