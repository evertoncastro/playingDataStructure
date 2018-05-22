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

    def traverse(self):
        self.__root.visit()

    def search(self, value):
        self.__root.search(value)
