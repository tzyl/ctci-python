# Given a sorted array of strings which is interspersed with empty
# strings, write a method to find the location of a given string.


# Modified binary search to move middle to closest non-empty string.
# Worst case O(n).
def search_sparse(strings, s):
    p, r = 0, len(strings) - 1
    while p <= r:
        q = (p + r) / 2
        if not strings[q]:
            # Find closest non-empty string.
            left, right = q - 1, q + 1
            while True:
                if left < p and right > r:
                    # s does not exist in strings.
                    return -1
                elif strings[left]:
                    q = left
                    break
                elif strings[right]:
                    q = right
                    break
                left -= 1
                right += 1
        if strings[q] == s:
            return q
        elif strings[q] < s:
            # Continue search to the right.
            p = q + 1
        elif strings[q] > s:
            # Continue search to the left.
            r = q - 1
    return -1

if __name__ == '__main__':
    test = ["a", "", "", "", "b", ""]
    print search_sparse(test, "b")
    print search_sparse(test, "a")
    print search_sparse(test, "c")
    test2 = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    print search_sparse(test2, "at")
    print search_sparse(test2, "ball")
    print search_sparse(test2, "car")
    print search_sparse(test2, "dad")
    # Empty strings aren't searched for.
    print search_sparse(test2, "")
