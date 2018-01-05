import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.linkedlist import LinkedList


def find_sum(binary_tree, sum_):
    path = [None] * (calculate_height(binary_tree) + 1)
    find_sum_helper(binary_tree.root, sum_, path, 0)


def find_sum_helper(node, sum_, path, level):
    if node is None:
        return
    # Insert node into current path.
    path[level] = node.value
    t = 0
    for i in xrange(level, -1, -1):
        t += path[i]
        if t == sum_:
            print "Path found:"
            for j in xrange(i, level + 1):
                print path[j]
    # Searches nodes beneath this one.
    find_sum_helper(node.left, sum_, path, level + 1)
    find_sum_helper(node.right, sum_, path, level + 1)


def calculate_height(binary_tree):
    def _calculate_heights(node):
        if node is None:
            return -1
        return 1 + max(_calculate_heights(node.left), _calculate_heights(node.right))
    if binary_tree.root is None:
        return None
    return _calculate_heights(binary_tree.root)


def print_all_paths(binary_tree, value):
    """Prints all paths which sum to a given value."""
    paths = []
    _get_all_paths(paths, binary_tree.root, value)
    for i, path in enumerate(paths):
        print "Path %s" % i
        for node in path:
            print node.key, node.value


def _get_all_paths(paths, root, value):
    paths.extend(all_paths_from(root, value))
    if root is not None:
        _get_all_paths(paths, root.left, value)
        _get_all_paths(paths, root.right, value)


def all_paths_from(root, value):
    if root is None:
        return []

    left_paths = all_paths_from(root.left, value - root.value)
    for path in left_paths:
        path.insert(Node(root.key, root.value))
    right_paths = all_paths_from(root.right, value - root.value)
    for path in right_paths:
        path.insert(Node(root.key, root.value))

    if root.value == value:
        path = LinkedList()
        path.insert(Node(root.key, root.value))
        return left_paths + right_paths + [path]

    return left_paths + right_paths


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print node
            self.inorder_traversal(node.right)


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

if __name__ == "__main__":
    binary_tree = BinaryTree()
    binary_tree.root = Node(0, 1)
    binary_tree.root.left = Node(1, 2)
    binary_tree.root.left.left = Node(2, 3)
    binary_tree.root.right = Node(3, 4)
    binary_tree.root.right.left = Node(4, 1)
    binary_tree.root.right.left.left = Node(5, 1)
    binary_tree.root.right.right = Node(6, 5)
    binary_tree.root.right.right.left = Node(7, 1)
    binary_tree.root.right.right.left.left = Node(8, 1)
    binary_tree.root.right.right.left.left.left = Node(9, -1)
    print_all_paths(binary_tree, 6)
    find_sum(binary_tree, 6)
