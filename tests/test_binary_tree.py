import unittest
from binary_tree.tree import Tree
from binary_tree.node import Node


class TestTree(unittest.TestCase):

    def setUp(self):
        # Do some stuff
        pass

    def test_search_node(self):
        tree = Tree()
        for val in [7, 3, 6, 9, 11, 5, 2, 8]:
            tree.add_value(val)
        result = tree.search(9)
        expected_node = Node(9)
        expected_node.add_node(Node(8))
        expected_node.add_node(Node(11))

        self.assertEqual(result, expected_node)

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

    def test_node_degree(self):
        tree = Tree()
        for val in [7, 3, 6, 9, 11, 5, 2, 8]:
            tree.add_value(val)
        result = tree.degree(6)
        self.assertEqual(result, 1)

    def test_tree_level(self):
        tree = Tree()
        for val in [7, 3, 6, 9, 11, 5, 2, 8]:
            tree.add_value(val)
        result = tree.level()
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
