import unittest
from binary_tree.tree import Tree


class TestTree(unittest.TestCase):

    def setUp(self):
        # Do some stuff
        pass

    def test_leaf_nodes(self):
        tree = Tree()
        for val in [7, 3, 6, 9, 11, 5, 2, 8]:
            tree.add_value(val)
        result = tree.leaf_nodes()
        self.assertEqual(result, [2, 5, 8, 11])

    def test_internal_nodes(self):
        tree = Tree()
        for val in [7, 3, 6, 9, 11, 5, 2, 8]:
            tree.add_value(val)
        result = tree.internal_nodes()
        self.assertEqual(result, [3, 6, 7, 9])

if __name__ == '__main__':
    unittest.main()