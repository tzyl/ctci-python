def decimal_to_binary(num):
    """Given a real number between 0 and 1 gives the binary representation
    or prints "ERROR" if the number cannot be represented accurately in
    binary with at most 32 characters.
    """
    bits = []
    i = 1
    while num and i <= 32:
        if num >= (1.0 / 2) ** i:
            bits.append(1)
            num -= (1.0 / 2) ** i
        else:
            bits.append(0)
        i += 1
    if num:
        return "ERROR"
    return "0." + "".join(str(bit) for bit in bits)


def decimal_to_binary2(num):
    """Uses multiplcation rather than division."""
    bits = []
    i = 1
    while num and i <= 32:
        num *= 2
        if num >= 1:
            bits.append(1)
            num -= 1
        else:
            bits.append(0)
        i += 1
    if num:
        return "ERROR"
    return "0." + "".join(str(bit) for bit in bits)

if __name__ == "__main__":
    print decimal_to_binary(0.625)
    print decimal_to_binary2(0.625)
