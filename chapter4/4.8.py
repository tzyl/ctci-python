import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.queue import Queue
from datastructures.binarysearchtree import BinarySearchTree, Node


def is_subtree(t1, t2):
    """Returns True if t2 (binary tree with hundreds of nodes) is a subtree of
    t1 (binary tree with millions of nodes).
    """
    if t2.root is None:
        # Empty tree always a subtree.
        return True
    elif t1.root is None:
        return False
    return subtree(t1.root, t2.root)


def subtree(r1, r2):
    q = Queue()
    q.enqueue(r1)
    while not q.queue_empty():
        x = q.dequeue()
        if x.key == r2.key and same_tree(x, r2):
            return True
        if x.left is not None:
            q.enqueue(x.left)
        if x.right is not None:
            q.enqueue(x.right)
    return False


def subtree_recursive(r1, r2):
    if r1 is None:
        return False
    if r1.key == r2.key:
        if same_tree(r1, r2):
            return True
    return subtree_recursive(r1.left, r2) or subtree_recursive(r1.right, r2)


def same_tree(r1, r2):
    if r1 is None and r2 is None:
        return True
    elif r1 is None or r2 is None:
        return False
    elif r1.key != r2.key:
        return False
    else:
        return same_tree(r1.left, r2.left) and same_tree(r1.right, r2.right)


def is_subtree2(t1, t2):
    if t2.root is None:
        return True
    x = t1.search(t2.root.key)
    if x is None:
        return False
    return same_tree2(x, t2.root)


def same_tree2(root1, root2):
    q = Queue()
    q.enqueue(root1)
    q.enqueue(root2)
    while not q.queue_empty():
        x, y = q.dequeue(), q.dequeue()
        if x.key != y.key:
            return False
        if x.left is not None and y.left is not None:
            q.enqueue(x.left)
            q.enqueue(y.left)
        elif x.left is not y.left:
            return False
        if x.right is not None and y.right is not None:
            q.enqueue(x.right)
            q.enqueue(y.right)
        elif x.right is not y.right:
            return False
    return True

if __name__ == "__main__":
    t1 = BinarySearchTree()
    t2 = BinarySearchTree()
    for i in xrange(1000):
        t1.insert(Node(i))
    print "DONE"
    for i in xrange(900, 1000):
        t2.insert(Node(i))
    print is_subtree(t1, t2)
