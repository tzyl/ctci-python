import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.binarysearchtree import BinarySearchTree, Node


def is_binary_search_tree_min_max(binary_tree):
    """Method by passing min and max ranges."""
    min_, max_ = -float("inf"), float("inf")
    return check_min_max(binary_tree.root, min_, max_)


def check_min_max(root, min_, max_):
    if root is None:
        return True
    if (not min_ < root.key < max_ or
        not check_min_max(root.left, min_, root.key) or
            not check_min_max(root.right, root.key, max_)):
        return False
    return True


def is_binary_search_tree(binary_tree):
    """Saves space by only keeping track of last seen."""
    def check_subtree(root):
        if root is None:
            return True
        if not check_subtree(root.left):
            return False
        if last_seen["value"] > root.key:
            return False
        last_seen["value"] = root.key
        if not check_subtree(root.right):
            return False
        return True
    last_seen = {"value": -float("inf")}
    return check_subtree(binary_tree.root)


def is_binary_search_tree2(binary_tree):
    """Returns True if the given binary tree is in fact a
    binary search tree.
    """
    in_order_nodes = []
    in_order_traversal(in_order_nodes, binary_tree.root)
    for i in xrange(len(in_order_nodes) - 1):
        if in_order_nodes[i].key > in_order_nodes[i + 1].key:
            return False
    return True
    # return any(in_order_nodes[i].key > in_order_nodes[i + 1].key for i in xrange(len(in_order_nodes) - 1))


def in_order_traversal(node_list, root):
    if root is not None:
        in_order_traversal(node_list, root.left)
        node_list.append(root)
        in_order_traversal(node_list, root.right)

if __name__ == "__main__":
    bst = BinarySearchTree()
    for i in xrange(10):
        bst.insert(Node(i))
    bst.root.left = Node(999)
    print is_binary_search_tree_min_max(bst)
