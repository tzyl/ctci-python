def number_of_paths(X, Y):
    """Returns the number of paths to move from (0, 0) to (X, Y) in an X by Y
    grid if can only move right or down."""
    if X == 0 or Y == 0:
        return 1
    return number_of_paths(X - 1, Y) + number_of_paths(X, Y - 1)


def number_of_paths2(X, Y):
    """Solution using mathematical analysis that the number of paths is
    (X + Y - 2) choose (min(X, Y) - 1)."""
    if X == 0 or Y == 0:
        return 1
    numerator = X + Y
    denominator = 1
    for i in xrange(1, min(X, Y)):
        numerator *= X + Y - i
        denominator *= 1 + i
    return numerator / denominator


def memoize(fn):
    cache = {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = fn(*args, **kwargs)
        return cache[key]
    return wrapper


@memoize
def find_a_path(X, Y, blocked):
    """Finds a path from (0, 0) to (X, Y) with blocked positions."""
    if (X, Y) in blocked:
        return None
    if X == 0 and Y == 0:
        return [(X, Y)]
    if X != 0:
        right_path = find_a_path(X - 1, Y, blocked)
        if right_path is not None:
            right_path.append((X, Y))
            return right_path
    if Y != 0:
        down_path = find_a_path(X, Y - 1, blocked)
        if down_path is not None:
            down_path.append((X, Y))
            return down_path
    return None

if __name__ == '__main__':
    for i in xrange(1, 10):
        for j in xrange(1, 10):
            print number_of_paths(i, j), number_of_paths2(i, j)
    print find_a_path(100, 100, [(9, 10), (0, 1), (1, 2)])[::-1]
