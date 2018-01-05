def check_binary_tree_balanced(binary_tree):
    calculate_heights(binary_tree)
    return check_subtree_balanced(binary_tree.root)


def check_subtree_balanced(root):
    if root is None:
        return True
    return (check_node_balanced(root) and
            check_subtree_balanced(root.left) and
            check_subtree_balanced(root.right))


def check_node_balanced(node):
    if node.left is None or node.right is None:
        return True
    return abs(node.left.height - node.right.height) <= 1


def calculate_heights(binary_tree):
    def _calculate_heights(node):
        if node is None:
            return - 1
        node.height = 1 + max(_calculate_heights(node.left), _calculate_heights(node.right))
        return node.height
    _calculate_heights(binary_tree.root)


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
    bt = BinaryTree()
    x = Node()
    bt.root = x
    x = Node()
    bt.root.left = x
    x = Node()
    bt.root.left.left = x
    x = Node()
    bt.root.left.left.left = x
    y = Node()
    bt.root.right = x
    print check_binary_tree_balanced(bt)
    print bt.root.height
