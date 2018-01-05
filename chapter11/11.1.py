# You are given two sorted arrays, A and B, where A has a large enough buffer
# at the end to hold B. Write a method to merge B into A in sorted order.


def merge(A, B):
    # Work from the end and move elements into their correct place. O(n)
    i, j = len(A) - 1, len(B) - 1
    while A[i] is None:
        i -= 1
    for k in reversed(xrange(len(A))):
        if i < 0 or A[i] <= B[j]:
            A[k] = B[j]
            j -= 1
        elif j < 0 or A[i] > B[j]:
            A[k] = A[i]
            i -= 1

if __name__ == '__main__':
    A = range(10, 15) + [None] * 5
    B = range(5)
    merge(A, B)
    print A
