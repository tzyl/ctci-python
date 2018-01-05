def find_missing_integer(A):
    """O(n) solution using more complex method."""
    n = len(A)
    bit_length = 0
    m = n
    while m:
        m >>= 1
        bit_length += 1
    ans = 0
    for i in xrange(bit_length):
        zeroes = [x for x in A if not x & 1 << i]
        ones = [x for x in A if x & 1 << i]
        if len(zeroes) <= len(ones):
            A = zeroes
        else:
            ans |= 1 << i
            A = ones
    return ans


def find_missing_integer2(A):
    """Given an array A containing all the integers from 0 to n except for one,
    returns the missing integer if only allowed to fetch the jth bit of A[i] in
    constant time.
    """
    n = len(A)
    seen = [False] * (n + 1)
    bit_length = 0
    m = n
    while m:
        m >>= 1
        bit_length += 1
    for num in A:
        x = 0
        for j in xrange(bit_length):
            x |= get_bit(num, j) << j
        seen[x] = True
    for x in xrange(n + 1):
        if not seen[x]:
            return x
    return None


def get_bit(num, i):
    return 1 if num & 1 << i else 0

if __name__ == '__main__':
    A = range(1000000)
    A.remove(33)
    print find_missing_integer(A)
    # print find_missing_integer2(A)
