def permutations_generator(string):
    if len(string) <= 1:
        yield string
    else:
        for perm in permutations_generator(string[1:]):
            for i in xrange(len(string)):
                yield perm[:i] + string[0] + perm[i:]


def permutations(string):
    if len(string) <= 1:
        return string
    p = []
    for perm in permutations(string[1:]):
        for i in xrange(len(string)):
            p.append(perm[:i] + string[0] + perm[i:])
    return p

if __name__ == '__main__':
    print permutations("abc")
    print "\n".join(perm for perm in permutations_generator("abc"))
