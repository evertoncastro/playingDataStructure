from tree import Tree

if __name__ == '__main__':
    tree = Tree()
    tree.add_value(8)
    tree.add_value(16)
    tree.add_value(5)
    tree.add_value(7)
    tree.add_value(7)
    tree.add_value(4)
    tree.add_value(1)
    tree.add_value(2)
    tree.traverse_in_order()
    tree.traverse_pre_order()
    tree.traverse_post_order()
    tree.search(16)
