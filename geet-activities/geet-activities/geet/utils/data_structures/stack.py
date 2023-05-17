'''
[Data Structure] Stack implementation.
'''


class ModifiedFilesStack:

    '''
    Stack object.

    Attributes:
        items (list): list to store the stack elements

    Methods:
        __init__(self): initializes an empty stack
        push(self, item): adds an item to the top of the stack
        pop(self): removes and returns the top item from the stack
        is_empty(self): checks if the stack is empty
        size(self): returns the number of items in the stack
    '''

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

