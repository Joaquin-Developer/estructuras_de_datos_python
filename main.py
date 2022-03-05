"""Modulo para probar todo"""

from List import List
from Node import Node


def init_list():
    """cargamos e imprimimos la lista"""
    my_list = List()

    for i in range(1, 5):
        my_list.insert(Node(i, None))

    my_list.insert_in_first_position(Node(0, None))

    my_list.iterate()


if __name__ == "__main__":
    init_list()
