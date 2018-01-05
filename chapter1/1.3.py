from collections import Counter


def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_count = Counter(s1)
    s2_count = Counter(s2)
    for c in s1_count:
        if s1_count[c] != s2_count[c]:
            return False
    return True


def is_permutation2(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)


def is_permutation3(s1, s2):
    if len(s1) != len(s2):
        return False
    counts = [0] * 256
    for c in s1:
        counts[ord(c)] += 1
    for c in s2:
        counts[ord(c)] -= 1
        if counts[ord(c)] < 0:
            return False
    return True

print is_permutation3("aaaaabb", "abaabaa")
print is_permutation3("aaaaabb A", "Aaba abaa")
