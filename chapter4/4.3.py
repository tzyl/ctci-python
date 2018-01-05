import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.binarysearchtree import BinarySearchTree, Node


def min_height_binary_search_tree(sorted_integers):
    bst = BinarySearchTree()
    root = insert_middle(bst, sorted_integers, 0, len(sorted_integers))
    bst.insert(root)
    return bst


def insert_middle(bst, sorted_integers, p, q):
    if p == q:
        return None
    middle = (p + q) / 2
    node = Node(sorted_integers[middle])
    node.left = insert_middle(bst, sorted_integers, p, middle)
    node.right = insert_middle(bst, sorted_integers, middle + 1, q)
    return node


def calculate_heights(binary_tree):
    def _calculate_heights(node):
        if node is None:
            return - 1
        node.height = 1 + max(_calculate_heights(node.left), _calculate_heights(node.right))
        return node.height
    _calculate_heights(binary_tree.root)
    if binary_tree.root is not None:
        binary_tree.height = binary_tree.root.height

if __name__ == "__main__":
    bst = min_height_binary_search_tree(xrange(15))
    calculate_heights(bst)
    print bst.height
