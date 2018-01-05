# Given an M x N matrix in which each row and each column is sorted in
# ascending order, write a method to find an element.


def find_element(A, x):
    # O(m + n) by eliminating one row or column at a time.
    m, n = len(A), len(A[0])
    # Start at top right.
    i, j = 0, n - 1
    while i >= 0 and j >= 0:
        if A[i][j] == x:
            return i, j
        elif A[i][j] > x:
            # The start of this column is too large so the whole column must be too
            # large.
            j -= 1
        else:
            # The end of this row is too small so the whole row must be too small.
            i += 1
    return None


def find_element2(A, x):
    # O(log(m)log(n)) by binary searching for candidate rows then binary
    # searching each of these rows for x.
    if A[0][0] > x:
        return None
    p, r = 0, len(A) - 1
    while p < r:
        # Round up two element state space to avoid loop.
        q = (p + r + 1) / 2
        if A[q][0] > x:
            r = q - 1
        else:
            p = q
    for i in xrange(p + 1):
        p, r = 0, len(A[i]) - 1
        while p <= r:
            q = (p + r) / 2
            if A[i][q] == x:
                return i, q
            elif A[i][q] > x:
                r = q - 1
            else:
                p = q + 1
    return None

if __name__ == '__main__':
    A = [[0, 1, 1],
         [1, 1, 3],
         [2, 4, 5]]
    print find_element(A, 2)
