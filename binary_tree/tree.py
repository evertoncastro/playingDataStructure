from node import Node


class Tree(object):
    __root = None

    def add_value(self, _val):
        if type(_val) != int:
            raise TypeError('The val parameter should be an integer')
        node = Node(_val)
        if not self.__root:
            self.__root = node
        else:
            self.__root.add_node(node)

    def traverse_in_order(self):
        print 'Start traverse in order'
        self.__root.visit_in_order()
        print 'End traverse in order'

    def traverse_pre_order(self):
        print 'Start traverse pre order'
        self.__root.visit_pre_order()
        print 'End traverse pre order'

    def traverse_post_order(self):
        print 'Start traverse post order'
        self.__root.visit_post_order()
        print 'End traverse post order'

    def leaf_nodes(self):
        return self.__root.recursive_leafs()

    def internal_nodes(self):
        return self.__root.recursive_internals()

    def search(self, value):
        return self.__root.recursive_search(value)

    def degree(self, value):
        return self.__root.recursive_degree(value)

    def level(self):
        return self.__root.recursive_level()


