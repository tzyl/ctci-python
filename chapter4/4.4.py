import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.linkedlist import LinkedList


def get_each_depth(binary_tree):
    linked_lists = []
    current = LinkedList()
    current.insert(binary_tree.root)
    while not current.empty():
        linked_lists.append(current)
        children = LinkedList()
        for node in current:
            if node.left is not None:
                children.insert(node.left)
            if node.right is not None:
                children.insert(node.right)
        current = children
    return linked_lists


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print node
            self.inorder_traversal(node.right)


class Node(object):
    def __init__(self):
        self.left = None
        self.right = None

if __name__ == "__main__":
    binary_tree = BinaryTree()
    x = Node()
    binary_tree.root = x
    x = Node()
    binary_tree.root.left = x
    x = Node()
    binary_tree.root.left.left = x
    x = Node()
    binary_tree.root.left.left.left = x
    x = Node()
    binary_tree.root.right = x
    for depth, linked_list in enumerate(get_each_depth(binary_tree)):
        print depth
        for node in linked_list:
            print node
