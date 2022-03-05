""" Definición de las Listas simplemente enlazadas """


class List:
    """List methods"""

    first = None

    def insert(self, node):
        """inserta node in last position"""
        elem = self.first

        if not elem:
            self.first = node
        else:
            while elem.next:
                elem = elem.next
            elem.next = node

    def insert_in_first_position(self, node):
        """insert node in first position"""
        if not self.first:
            self.first = node
        else:
            elem = self.first
            self.first = node
            node.next = elem

    def iterate(self):
        """print elements of the list"""
        elem = self.first

        while elem:
            print(elem.data)
            elem = elem.next
