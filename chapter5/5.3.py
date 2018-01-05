def get_larger_arithmetic(n):
    c = n
    c0 = 0
    c1 = 0
    while c & 1 == 0 and c != 0:
        c0 += 1
        c >>= 1
    while c & 1 == 1:
        c1 += 1
        c >>= 1
    if c0 + c1 == 32 or c0 + c1 == 0:
        return "ERROR. No larget number with the same number of 1 bits exists."
    return bin(n + (1 << c0) + (1 << (c1 - 1)) - 1)


def get_smaller_arithmetic(n):
    c = n
    c1 = 0
    c0 = 0
    while c & 1 == 1:
        c1 += 1
        c >>= 1
    while c & 1 == 0 and c != 0:
        c0 += 1
        c >>= 1
    if c1 + c0 == 32 or c0 + c1 == 0:
        return "ERROR. No smaller number with the same number of 1 bits exists."
    return bin(n - (1 << c1) - (1 << (c0 - 1)) + 1)


def get_larger_same_1s(n):
    """Given positive integer n, prints the next largesst and next smallest
    number that have the same number of 1 bits in binary representation.
    """
    # Find the first 1 bit with a 0 bit to the left of it.
    m = n
    i = 0
    while not (get_bit(m, 0) == 1 and get_bit(m, 1) == 0) and i < 32:
        m >>= 1
        i += 1
    if i == 32:
        return "ERROR. No larger number with the same number of 1 bits exists."
    # Move this 1 bit one place to the left and move all other 1s on
    # the right as far right as possible to minimize the number.
    larger = n | (1 << (i + 1))
    count = sum(get_bit(larger, j) for j in xrange(i))
    clear_mask = ~((1 << (i + 1)) - 1)
    set_mask = (1 << count) - 1
    larger &= clear_mask
    larger |= set_mask
    return bin(larger)


def get_smaller_same_1s(n):
    # Find the first 0 bit which has a 1 bit to the left of it.
    m = n
    i = 0
    while not (get_bit(m, 0) == 0 and get_bit(m, 1) == 1) and i < 32:
        m >>= 1
        i += 1
    if i == 32:
        return "ERROR. No smaller number with the same number of 1 bits exists."
    # Move the 1 bit one place to the right and all other 1s to the right as far
    # left as possible.
    smaller = n
    count = sum(get_bit(n, j) for j in xrange(i))
    clear_mask = ~((1 << (i + 2)) - 1)
    set_mask = ((1 << (count + 1)) - 1) << (i - count)
    smaller &= clear_mask
    smaller |= set_mask
    return bin(smaller)


def get_bit(num, i):
    """Gets the ith bit (zero-indexed)."""
    return 1 if num & 1 << i else 0

if __name__ == "__main__":
    print get_larger_same_1s(0b11101100)
    print get_larger_arithmetic(0b11101100)
    print get_smaller_same_1s(0b111100011)
    print get_smaller_arithmetic(0b111100011)
