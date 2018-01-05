# A circus is designing a tower routine consisting of people standing atop
# one another's shoulders. For practical and aesthetic reasons, each
# person must be both shorter and lighter than the person below him or
# her. Given the heights and weights of each person in the circus, write a
# method to compute the largest possible number of people in such a tower.

# EXAMPLE:
# Input (ht,wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
# Output:The longest tower is length 6 and includes from top to bottom:
# (56, 90) (60,95) (65,100) (68,110) (70,150) (75,190)


# O(n^2).
def max_people(people):
    # First sort on height then find longest increasing subsequence based
    # on weights.
    people.sort(key=lambda x: x[0])
    # DP to get longest increasing subsequence. A[i] will represent the longest
    # increasing subsequence ending at people[i].
    best = 0
    A = [1] * len(people)
    for i in xrange(len(people)):
        for j in xrange(i):
            if A[i] >= A[j] and 1 + A[j] > A[i]:
                A[i] = 1 + A[j]
        best = max(best, A[i])
    return best


# Recursive solution finding optimal subtowers like problem 9.10.
def max_people2(people):
    best = []
    for i in xrange(len(people)):
        best = max(best, max_people_from(people, i), key=len)
    return best


def max_people_from(people, i):
    tower = [people[i]]
    for j in xrange(len(people)):
        if j != i and is_possible(people[i], people[j]):
            tower = max(tower, [people[i]] + max_people_from(people, j), key=len)
    return tower


def is_possible(p1, p2):
    return p2[0] < p1[0] and p2[1] < p1[1]


if __name__ == '__main__':
    print max_people([(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)])
