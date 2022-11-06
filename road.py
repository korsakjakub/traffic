class Road(list):
    def __getitem__(self, item):
        return super().__getitem__(self.pbc(item))

    def __setitem__(self, index, item):
        super().__setitem__(self.pbc(index), str(item))

    def pbc(self, index):
        length = super().__len__()
        if index >= length:
            index %= length
        return index
