def swap_odd_even_bits(x):
    """Clever solution using masks to single out even and odd."""
    even = x & 0xAAAAAAAA
    odd = x & 0x55555555
    return bin(even >> 1 | odd << 1)


def swap_odd_even_bits2(x):
    """Swaps the odd and even bits in an integer x
    i.e bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped etc.
    """
    y = x
    i = 0
    while y:
        if y & 1 != y >> 1 & 1:
            x = swap_bits(x, i, i + 1)
        y >>= 2
        i += 2
    return bin(x)


def swap_bits(x, i, j):
    ith = 1 if x & (1 << i) else 0
    jth = 1 if x & (1 << j) else 0
    if ith == 1 and jth == 0:
        x &= ~(1 << i)
        x |= 1 << j
    elif ith == 0 and jth == 1:
        x &= ~(1 << j)
        x |= 1 << i
    return x

if __name__ == '__main__':
    print swap_odd_even_bits(0b101011101010)
    print swap_odd_even_bits2(0b101011101010)
