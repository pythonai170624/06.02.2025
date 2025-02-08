from typing import override

from Component import Component


class Leaf(Component):

    def __init__(self, name):
        super().__init__(name)

    @override
    def add_child(self, child):
        pass

    @override
    def remove_child(self, child):
        pass

    @override
    def get_children(self):
        print('again leaf?')
        return []

    @override
    def draw(self, space):
        print(space + self.name)





