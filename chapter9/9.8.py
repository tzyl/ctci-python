def number_of_ways(n):
    """Returns the number of ways of representing n using the coins
    1, 5, 10, 25."""
    return number_of_ways_helper([1, 5, 10, 25], n)


def number_of_ways_helper(coins, n):
    if len(coins) == 1:
        return 1
    coin = coins[-1]
    total = 0
    i = 0
    while n - i*coin >= 0:
        total += number_of_ways_helper(coins[:-1], n - i*coin)
        i += 1
    return total

if __name__ == '__main__':
    for i in xrange(27):
        print number_of_ways(i)
