def find_common_ancestor(binary_tree, x, y):
    """Returns the first common ancestor of nodes x and y in a binary tree or
    None if there is not one.
    """
    result = _find_common_ancestor(binary_tree.root, x, y)
    if result.is_answer:
        return result.node
    return None


class Result(object):
    def __init__(self, node, is_answer):
        self.node = node
        self.is_answer = is_answer


def _find_common_ancestor(root, x, y):
    """Deals with the case if a node is not in the tree by passing a flag to
    represent if we have found the answer or not.
    """
    if root is None:
        return Result(None, False)
    if root is x and root is y:
        return Result(root, True)

    left = _find_common_ancestor(root.left, x, y)
    if left.is_answer:
        return left

    right = _find_common_ancestor(root.right, x, y)
    if right.is_answer:
        return right

    if left.node is not None and right.node is not None:
        return Result(root, True)
    elif root is x or root is y:
        is_answer = left.node is not None or right.node is not None
        return Result(root, is_answer)
    else:
        node = left.node if right.node is None else right.node
        return Result(node, False)


def _find_common_ancestor_bug(root, x, y):
    """Only traverses tree once. Does not deal with if one of the nodes is not
    in the tree at all.
    """
    if root is None:
        return root

    if root is x and root is y:
        return root

    left = _find_common_ancestor_bug(root.left, x, y)
    if left is not None and left is not x and left is not y:
        return left

    right = _find_common_ancestor_bug(root.right, x, y)
    if right is not None and right is not x and right is not y:
        return right

    if left is not None and right is not None:
        return root
    elif root is x or root is y:
        return root
    else:
        return right if left is None else left


def _find_common_ancestor_mine(root, x, y):
    """Only traverses tree once."""
    if root is None or root is x or root is y:
        return root
    left = _find_common_ancestor(root.left, x, y)
    right = _find_common_ancestor(root.right, x, y)
    if left is not None and right is not None:
        return root
    elif left is None:
        return right
    elif right is None:
        return left
    else:
        return None


def _find_common_ancestor_slow(root, x, y):
    if root is None or root is x or root is y:
        return root
    x_on_left = is_descendant(root.left, x)
    y_on_left = is_descendant(root.left, y)
    if x_on_left != y_on_left:
        return root
    direction = root.left if x_on_left else root.right
    return _find_common_ancestor_slow(direction, x, y)


def is_descendant(p, q):
    """Returns True if q is a descendant of p."""
    if p is None:
        return False
    elif p is q:
        return True
    else:
        return is_descendant(p.left, q) or is_descendant(p.right, q)


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print node
            self.inorder_traversal(node.right)


class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

if __name__ == "__main__":
    binary_tree = BinaryTree()
    x = Node(1)
    binary_tree.root = x
    x = Node(2)
    binary_tree.root.left = x
    x = Node(3)
    binary_tree.root.left.left = x
    w = Node(4)
    binary_tree.root.right = w
    y = Node(5)
    binary_tree.root.left.left.left = y
    z = Node(6)
    binary_tree.root.left.left.right = z
    print find_common_ancestor(binary_tree, y, z).key
    print find_common_ancestor(binary_tree, w, z).key
