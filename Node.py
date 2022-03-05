# pylint: disable=too-few-public-methods
"""Implementación de los  nodos"""


class Node:
    """Representación de nodo"""

    data = None
    next = None

    def __init__(self, data: int, next):
        self.data = data
        self.next = next
