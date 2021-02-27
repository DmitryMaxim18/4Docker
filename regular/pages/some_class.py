from regular.some_module import print_arg


class A:
    some_data = print_arg('Print me')
    arg1 = 'arg1'

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name} Dima"

    def print_hello(self):
        print('Hello')


print(A.some_data)