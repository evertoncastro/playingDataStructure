
class Node(object):
    """
    Class to create a Tree of Nodes based on hierarchy structure.
    The most part of the methods implement a recursive way to navigate over the hierarchy od nodes
    """
    __value = None
    __left = None
    __right = None

    def __init__(self, value):
        self.__value = value

    def __eq__(self, other):
        """
        Used in order to compare two nodes looking for the values inside them in place of memory pointer
        :param The value to be compared with self:
        :return a Boolean value:
        """
        return self.__dict__ == other.__dict__

    @property
    def value(self):
        return self.__value

    # @property
    # def left(self):
    #     return self.__left
    #
    # @left.setter
    # def left(self, node):
    #     if not isinstance(node, Node):
    #         raise ValueError('Value provided is not of Node Class')
    #     self.__left = node
    #
    # @property
    # def right(self):
    #     return self.__right
    #
    # @right.setter
    # def right(self, node):
    #     if not isinstance(node, Node):
    #         raise ValueError('Value provided is not of Node Class')
    #     self.__right = node

    def add_node(self, n):
        if n.value < self.value:
            if not self.__left:
                self.__left = n
            else:
                self.__left.add_node(n)
        elif n.value > self.value:
            if not self.__right:
                self.__right = n
            else:
                self.__right.add_node(n)

    def visit_in_order(self):
        if self.__left:
            self.__left.visit_in_order()
        print str(self.__value)
        if self.__right:
            self.__right.visit_in_order()

    def visit_pre_order(self):
        print str(self.value)
        if self.__left:
            self.__left.visit_pre_order()
        if self.__right:
            self.__right.visit_pre_order()

    def visit_post_order(self):
        if self.__left:
            self.__left.visit_post_order()
        if self.__right:
            self.__right.visit_post_order()
        print str(self.value)

    def recursive_search(self, value):
        if self.value == value:
            return self
        elif value < self.value and self.__left is not None:
            return self.__left.recursive_search(value)
        elif value > self.value and self.__right is not None:
            return self.__right.recursive_search(value)

    def recursive_degree(self, value):
        node = self.recursive_search(value)
        if not node:
            return None
        total = 0
        if node.__left:
            total += 1
        if node.__right:
            total += 1
        return total

    def recursive_leafs(self, _list=None):
        if not _list:
            _list = []
        if not self.__left and not self.__right:
            _list.append(self.__value)
            return _list
        if self.__left is not None:
            _list = self.__left.recursive_leafs(_list)
        if self.__right is not None:
            _list = self.__right.recursive_leafs(_list)
        return _list

    def recursive_internals(self, _list=None):
        if not _list:
            _list = []
        if self.__left or self.__right:
            if self.__left is not None:
                _list = self.__left.recursive_internals(_list)
            _list.append(self.__value)
            if self.__right is not None:
                _list = self.__right.recursive_internals(_list)
        return _list

    def recursive_level(self, _l=0):
        if not self.__left and not self.__right:
            return _l
        l_left, l_right = 0, 0
        if self.__left is not None:
            l_left = self.__left.recursive_level(_l+1)
        if self.__right is not None:
            l_right = self.__right.recursive_level(_l+1)

        return max(l_left, l_right)

    def recursive_height(self, _h=0):
        if not self.__left and not self.__right:
            return _h
        h_left, h_right = 0, 0
        if self.__left is not None:
            h_left = self.__left.recursive_height(_h+1)
        if self.__right is not None:
            h_right = self.__right.recursive_height(_h+1)

        return max(h_left, h_right)

