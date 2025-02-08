from typing import override

from Component import Component


class Composite(Component):

    def __init__(self, name):
        super().__init__(name)
        self.children = []

    @override
    def add_child(self, child):
        self.children.append(child)

    @override
    def remove_child(self, child):
        self.children.remove(child)

    @override
    def get_children(self):
        print('again composite?')
        return self.children

    @override
    def draw(self, space = ''):
        print(space + self.name)
        #for child in self.children:
        #    child.draw(space + ' ' * 4)




