#!/usr/bin/env python

class Parent:

    def __init__(self, **kwargs):
        if 'name' in kwargs:
            self.__name = kwargs.pop('name')
        else:
            self.__name = "parent"
        if 'lastname' in kwargs:
            self.__lastname = kwargs.pop('lastname')
        else:
            self.__lastname = "bastard"
        self.__children = list()
        self.__kids = list()
        super().__init__(**kwargs)

    def print_name(self):
        print(self.__name, self.get_lastname())

    def get_lastname(self):
        return self.__lastname

    def add_child(self, child):
        assert(isinstance(child, Child)), "Must be instance of Child"
        self.__children.append(child)

    def list_kids(self):
        for child in self.__children:
            child.print_fullname()

    def add_kids_by_name(self, *names):
        for kid in names:
            self.__kids.append(str(kid))

    def construct_kids_by_name(self):
        for kid_names in self.__kids:
            child = Child(name=kid_names, lastname=self.get_lastname())
            self.add_child(child)

class Child(Parent):

    def __init__(self, name, **kwargs):
        self.__name = name
        super().__init__(**kwargs)

    def print_name(self):
        print(self.__name)

    def print_fullname(self):
        print(self.__name, self.get_lastname())


def main():
    print("###")
    p = Parent(name="john", lastname="smith")
    p.print_name()

    c = Child(name="tommy")
    c.print_name()

    print("###")
    p.add_child(c)
    p.list_kids()

    print("###")
    p.add_kids_by_name("jackie", "alice", "bobby")
    p.construct_kids_by_name()
    p.list_kids()


main()
