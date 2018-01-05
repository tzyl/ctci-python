# Given a sorted array of n integers that has been rotated an unknown
# number of times, write code to find an element in the array. You may
# assume that the array was originally sorted in increasing order.


# If all elemnts are not distinct we need to do extra searches.
def find_element(A, x):
    stack = []
    stack.append((0, len(A) - 1))
    while stack:
        p, r = stack.pop()
        q = (p + r) / 2
        # print p, q, r
        if x == A[q]:
            return q
        elif A[p] < A[q]:
            # A[p:q] is in sorted order.
            if A[p] <= x <= A[q-1]:
                # Continue search in A[p:q]
                stack.append((p, q - 1))
            else:
                # Continue search in A[q+1:r+1]
                stack.append((q + 1, r))
        elif A[p] > A[q]:
            # A[q+1:r+1] is in sorted order.
            if A[q+1] <= x <= A[r]:
                # Continue search in A[q+1:r+1]
                stack.append((q + 1, r))
            else:
                # Continue search in A[p:q]
                stack.append((p, q - 1))
        elif A[p] == A[q] and p != q:
            # Can't deduce anything here, search both sides.
            if q != p:
                stack.append((p, q - 1))
            if q != r:
                stack.append((q + 1, r))
    return -1


# This works if all elements are distinct.
def find_element2(A, x):
    p = 0
    r = len(A) - 1
    while p != r:
        q = (p + r) / 2
        if x == A[q]:
            return q
        elif A[p] < A[q]:
            # A[p:q] is in sorted order.
            if A[p] <= x <= A[q-1]:
                # Continue search in A[p:q]
                r = q - 1
            else:
                # Continue search in A[q+1:r]
                p = q + 1
        else:
            # A[q+1:r+1] is in sorted order.
            if A[q+1] <= x <= A[r]:
                # Continue search in A[q+1:r+1]
                p = q + 1
            else:
                # Continue search in A[p:q]
                r = q - 1
    return -1

if __name__ == '__main__':
    print find_element(range(10), 4)
    test1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
    print find_element(test1, 3)
    test2 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    print find_element(test2, 5)
