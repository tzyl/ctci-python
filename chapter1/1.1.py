def all_unique(s):
    # Returns true if all the characters in the string s are unique.
    return len(set(s)) == len(s)


def all_unique2(s):
    # Solution using list to track characters seen.
    if len(s) > 128:
        return False
    seen_char = [False] * 128
    for c in s:
        value = ord(c)
        if seen_char[value]:
            return False
        seen_char[value] = True
    return True


def all_unique3(s):
    # Solution using bit vector.
    if len(s) > 128:
        return False
    checker = 0
    for c in s:
        value = ord(c) - ord("a")
        if checker & (1 << value) > 0:
            return False
        checker |= (1 << value)
    return True

print all_unique3("abcd")
print all_unique3("aabcd")
