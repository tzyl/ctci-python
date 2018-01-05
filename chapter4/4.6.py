import random
import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.binarysearchtree import BinarySearchTree, Node


if __name__ == "__main__":
    bst = BinarySearchTree()
    keys = range(100)
    random.shuffle(keys)
    for key in keys:
        bst.insert(Node(key))
    x = bst.search(50)
    print bst.successor(x).key
    print bst.predecessor(x).key
