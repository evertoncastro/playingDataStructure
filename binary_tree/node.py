
class Node(object):
    __value = None
    __left = None
    __right = None

    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

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

    def search(self, value):
        if self.value == value:
            print 'Value found: %s' % str(value)
        elif value < self.value and self.__left is not None:
            self.__left.search(value)
        elif value > self.value and self.__right is not None:
            self.__right.search(value)
        else:
            print 'Not found value: %s' % str(value)

    def leafs(self, _list=None):
        if not _list:
            _list = []
        if not self.__left and not self.__right:
            _list.append(self.__value)
            return _list
        if self.__left is not None:
            _list = self.__left.leafs(_list)
        if self.__right is not None:
            _list = self.__right.leafs(_list)
        return _list

    def internals(self, _list=None):
        if not _list:
            _list = []
        if self.__left or self.__right:
            if self.__left is not None:
                _list = self.__left.internals(_list)
            _list.append(self.__value)
            if self.__right is not None:
                _list = self.__right.internals(_list)
        return _list

