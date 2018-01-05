# Given a boolean expression consisting of the symbols 0,1, &, |, and A, and a
# desired boolean result value result, implement a function to count the number
# of ways of parenthesizing the expression such that it evaluates to result.
# EXAMPLE
# Expression: 1A01011
# Desired result: false (0)
# Output: 2 ways. 1A( (010) 11) and 1A(91 (011)).


def memoize(fn):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return wrapper


@memoize
def catalan(n):
    """Returns the nth Catalan number.
    (2n!)/((n+1)!n!)
    """
    numerator, denominator = 1, 1
    for i in xrange(n):
        numerator *= 2 * n - i
        denominator *= i + 2
    return numerator / denominator


# Avoid building new strings by passing indices for start and end.
# Use Catalan number to avoid many calulations.
# Built in cache so we can specify key more precisely.
def number_of_ways(expr, desired, p=0, q=None, cache={}):
    if q is None:
        q = len(expr)
    if q == p + 1:
        num = int(expr[p])
        correct = (num and desired) or (not num and not desired)
        return 1 if correct else 0
    key = p, q
    if key not in cache:
        total = 0
        for i in xrange(p, q - 1, 2):
            if expr[i + 1] == "&":
                total += (number_of_ways(expr, True, p, i + 1, cache) *
                          number_of_ways(expr, True, i + 2, q, cache))
            elif expr[i + 1] == "|":
                total_ways = catalan((i - p) / 2) * catalan((q - i - 3) / 2)
                total += (total_ways -
                          number_of_ways(expr, False, p, i + 1, cache) *
                          number_of_ways(expr, False, i + 2, q, cache))
            elif expr[i + 1] == "^":
                total += (number_of_ways(expr, True, p, i + 1, cache) *
                          number_of_ways(expr, False, i + 2, q, cache))
                total += (number_of_ways(expr, False, p, i + 1, cache) *
                          number_of_ways(expr, True, i + 2, q, cache))
        cache[key] = total
    return cache[key] if desired else catalan((q - p - 1) / 2) - cache[key]


# Fast method using dynamic programming. O(n^2)
@memoize
def number_of_ways2(expr, desired):
    if len(expr) == 1:
        correct = (int(expr) and desired) or (not int(expr) and not desired)
        return 1 if correct else 0
    total = 0
    for i in xrange(0, len(expr) - 1, 2):
        a = number_of_ways2(expr[:i + 1], True)
        b = number_of_ways2(expr[:i + 1], False)
        c = number_of_ways2(expr[i + 2:], True)
        d = number_of_ways2(expr[i + 2:], False)
        if expr[i + 1] == "&":
            if desired:
                total += a * c
            else:
                total += a * d + b * c + b * d
        elif expr[i + 1] == "|":
            if desired:
                total += a * d + a * c + b * c
            else:
                total += b * d
        elif expr[i + 1] == "^":
            if desired:
                total += a * d + b * c
            else:
                total += a * c + b * d
    return total


# OLD. This method has duplicate counts.
def initial_thoughts(expr, desired):
    if len(expr) == 3:
        result = evaluate(expr)
        correct = (result and desired) or (not result and not desired)
        if correct:
            print expr
        return 1 if correct else 0
    total = 0
    for i in xrange(0, len(expr) - 1, 2):
        new_expr = list(expr)
        new_expr[i:i + 3] = [str(evaluate(expr[i:i + 3]))]
        total += initial_thoughts(new_expr, desired)
    return total


def evaluate(expr):
    a = int(expr[0])
    b = int(expr[2])
    if expr[1] == "|":
        return a | b
    elif expr[1] == "&":
        return a & b
    elif expr[1] == "^":
        return a ^ b
    return None

if __name__ == '__main__':
    # import timeit
    # print timeit.timeit('number_of_ways("1^0|0|1&1^0|0|1&1^0|0|1&1|0|1&1^0|0|1&1^0&1|0|1&1^0|0|1&1|0|1&1^0|0|1", False)', setup="from __main__ import number_of_ways")
    # print
    # timeit.timeit('number_of_ways2("1^0|0|1&1^0|0|1&1^0|0|1&1|0|1&1^0|0|1&1^0&1|0|1&1^0|0|1&1|0|1&1^0|0|1",
    # False)', setup="from __main__ import number_of_ways2")
    import time
    start = time.time()
    print number_of_ways("1^0|0|1&1^0|0|1&1^0|0|1&1|0|1&1^0|0|1&1^0&1|0|1&1^0|0|1&1|0|1&1^0|0|1", False)
    print time.time() - start
    start = time.time()
    print number_of_ways2("1^0|0|1&1^0|0|1&1^0|0|1&1|0|1&1^0|0|1&1^0&1|0|1&1^0|0|1&1|0|1&1^0|0|1", False)
    print time.time() - start
    # print number_of_ways("1|1|1|1|1|1|1|1", True)
    # print number_of_ways("1&1", True)
