"""
Jakub Korsak
"""


class Road(list):
    """
    A subclass of list, that accepts indices larger that its length.
    It follows periodic boundary conditions.
    Example
        road = Road([0, 2, 42])
        road[0]
        > 0
        road[5]
        > 42
    """

    def __getitem__(self, item):
        return super().__getitem__(self.pbc(item))

    def __setitem__(self, index, item):
        super().__setitem__(self.pbc(index), str(item))

    def pbc(self, index):
        """
        Implement periodic boundary conditions
        :param index: the List's index
        :return: The index modulo length of Road object
        """
        length = super().__len__()
        if index >= length:
            index %= length
        return index
