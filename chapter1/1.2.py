def reverse(s):
    """Reverses string s"""
    if len(s) <= 1:
        return s
    return s[-1] + reverse(s[:-1])


def reverse2(s):
    chars = []
    for i in xrange(len(s) - 1, 0, -1):
        chars.append(s[i])
    return "".join(chars)


def reverse3(s):
    return "".join(s[i] for i in reversed(xrange(len(s))))


def reverse4(s):
    c_list = list(s)
    for i in xrange(len(s) / 2):
        c_list[i], c_list[len(s) - 1 - i] = c_list[len(s) - 1 - i], c_list[i]
    return "".join(c_list)

print reverse4("abcdefghij")
