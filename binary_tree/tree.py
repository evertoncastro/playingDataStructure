from node import Node


class Tree(object):
    __root = None

    def add_value(self, val):
        if type(val) != int:
            raise TypeError('The val parameter should be an integer')
        node = Node(val)
        if not self.__root:
            self.__root = node
        else:
            self.__root.add_node(node)

    def traverse_in_order(self):
        print 'Start traverse in order'
        self.__root.visit_in_order()
        print 'End traverse in order'

    def search(self, value):
        self.__root.search(value)
