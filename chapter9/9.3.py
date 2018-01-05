def has_magic_index(A):
    """Magic index if A[i] = i for some i in a sorted array of distinct
    integers A. Brute force O(n) solution.
    """
    for i, x in enumerate(A):
        if i == x:
            return True
        elif i < x:
            return False
    return False


def has_magic_index2(A):
    """O(lg(n)) solution using binary search."""
    return binary_search(A, 0, len(A))


def binary_search(A, p, q):
    """Uses binary search to look for a magic index in A[p:q]."""
    if p == q:
        return False
    i = (p + q) / 2
    print p, q, i
    if A[i] == i:
        return True
    elif A[i] > i:
        return binary_search(A, p, i)
    else:
        return binary_search(A, i + 1, q)


def has_magic_index_non_distinct(A):
    """Solution in the case that the sorted integers are not distinct."""
    return binary_search_non_distinct(A, 0, len(A))


def binary_search_non_distinct(A, p, q):
    if p >= q:
        return False
    i = (p + q) / 2
    if A[i] == i:
        return True
    elif A[i] > i:
        return binary_search_non_distinct(A, p, i) or binary_search_non_distinct(A, A[i], q)
    else:
        return binary_search_non_distinct(A, i + 1, q) or binary_search_non_distinct(A, p, A[i] + 1)


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = [-5, -4, 1, 3, 6]
    print has_magic_index(A), has_magic_index2(A)
    print has_magic_index(B), has_magic_index2(B)
    C = range(-1, 1000) + [1001]
    print has_magic_index_non_distinct(C)
