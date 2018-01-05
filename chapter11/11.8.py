# Should use a balanced tree to ensure O(log(n)) insert and rank.
class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, x):
        y = self.root
        z = None
        while y is not None:
            y.size += 1
            z = y
            if x.key < y.key:
                y = y.left
            else:
                y = y.right
        x.parent = z
        if z is None:
            self.root = x
        elif x.key < z.key:
            z.left = x
        else:
            z.right = x

    # def search(self, k):
    #     x = self.root
    #     while x is not None and x.key != k:
    #         if x.key < k:
    #             x = x.left
    #         else:
    #             x = x.right
    #     return x

    def rank(self, k):
        """Returns the number of nodes with key <= k."""
        x = self.root
        left_count = 0
        while x is not None:
            if x.key <= k:
                left_count += 1 + x.left.size if x.left is not None else 1
                x = x.right
            else:
                x = x.left
        return left_count


class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1
