def subsets(A):
    """Returns all subests of a list as a list of lists."""
    return subsets_helper(A, 0, len(A))


def subsets_helper(A, p, q):
    if p == q:
        return [[]]
    subsets = subsets_helper(A, p + 1, q)
    subsets.extend([subset + [A[p]] for subset in subsets])
    return subsets


def subsets2(A):
    """Solution using binary representations."""
    subsets = []
    for i in xrange(1 << len(A)):
        subsets.append(subset_from_int(A, i))
    return subsets


def subset_from_int(A, x):
    subset = []
    i = 0
    while x:
        if 1 & x:
            subset.append(A[i])
        i += 1
        x >>= 1
    return subset

if __name__ == '__main__':
    print subsets(range(4))
    print subsets2(range(4))
