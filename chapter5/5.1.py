def substitute(N, M, i, j):
    """Inserts M into N such that M starts at bit j and ends at bit i in N."""
    clear_mask = ~((1 << j - i + 1) - 1) << i
    return N & clear_mask | M << i


def get_bit(num, i):
    """Gets the ith bit (zero-indexed)."""
    return 1 if num & 1 << i else 0


def set_bit(num, i):
    """Sets the ith bit to 1."""
    return num | (1 << i)


def clear_bit(num, i):
    """Clears the ith bit (zero-indexed)."""
    return num & ~(1 << i)


def clear_bits_significant_through(num, i):
    """Clears all bits from the most signifciant through to and including the
    ith bit.
    """
    mask = ((1 << i) - 1)
    return num & mask


def clear_bits_upto(num, i):
    """Clears all bits up to the ith bit."""
    mask = ~((1 << (i + 1)) - 1)
    return num & mask


def update_bit(num, i, v):
    """Updates bit i with value v."""
    clear_mask = ~(1 << i)
    return num & clear_mask | v << i

if __name__ == "__main__":
    print get_bit(0b1011, 1)
    print bin(set_bit(0b1011, 2))
    print bin(clear_bit(0b1011, 1))
    print bin(clear_bits_significant_through(0b1111111111, 3))
    print bin(clear_bits_upto(0b1111111111, 3))
    print bin(update_bit(0b1111011111, 5, 1))
    print bin(substitute(0b10000000000, 0b10011, 2, 6))
