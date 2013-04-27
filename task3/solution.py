from itertools import chain


class Person:
    def __init__(self, name, birth_year, gender, father=None, mother=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self._children = []
        self.parents = []
        self.set_parents(father, mother)

    def set_parents(self, father, mother):
        self.father = father
        self.mother = mother
        if father is not None:
            father.add_child(self)
        if mother is not None:
            mother.add_child(self)

    def add_child(self, child):
        self._children.append(child)
        child.parents.append(self)

    def children(self, gender=None):
        if gender is None:
            return self._children
        return [child for child in self._children if child.gender == gender]

    def get_siblings(self, gender=None):
        siblings = [parent.children(gender) for parent in self.parents]
        siblings = set(chain.from_iterable(siblings)) - {self}
        return list(siblings)

    def to_string(self):
        return self.name

    def get_brothers(self):
        return self.get_siblings('M')

    def get_sisters(self):
        return self.get_siblings('F')

    def is_direct_successor(self, successor):
        return self in successor.parents
