def to_convert(A, B):
    """Clears the least significant bit rather than continuously shifting."""
    different = 0
    C = A ^ B
    while C:
        different += 1
        C = C & C - 1
    return different


def to_convert2(A, B):
    """Using XOR."""
    different = 0
    C = A ^ B
    while C:
        if C & 1:
            different += 1
        C >>= 1
    return different


def to_convert3(A, B):
    """Returns the number of bits required to convert
    integer A into integer B.
    """
    different = 0
    while A or B:
        if A & 1 != B & 1:
            different += 1
        A >>= 1
        B >>= 1
    return different

if __name__ == '__main__':
    print to_convert(31, 14)
