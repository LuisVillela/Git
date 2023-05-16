'''
[Data Structure] Linked List implementation.
'''


class Node:
    '''
    Node object.

    Attributes:
        hash (str): commit's hash
        message (str): commit's message
        author (str): user's name
        email (str): user's email
        next (Node): pointer to next node in list

    ⬇ Your code starts here:
    '''
    def __init__(self, hash, message, author, email):
        self.hash = hash
        self.message = message
        self.author = author
        self.email = email
        self.next = None
    '''
    ⬆ Your code ends here.
    '''

class LinkedList:
    '''
    Linked List object.

    Attributes:
        start (Node): pointer to first node in list

    Methods:
        __init__(self)
        __iter__(self)
        traverse(self)
        insert_first(self, node)
        insert_last(self, node)
        remove(key)
        reverse(self)

    ⬇ Your code starts here:
    '''
    def __init__(self):
        self.start = None

    def __iter__(self):
        node = self.start
        while node:
            yield node
            node = node.next

    def traverse(self):
        if not self.start:
            print("Linked List is empty.")
            return
        node = self.start
        while node:
            print(f"Commit Hash: {node.hash}")
            print(f"Message: {node.message}")
            print(f"Author: {node.author}")
            print(f"Email: {node.email}")
            print()
            node = node.next

    def insert_first(self, node):
        if not self.start:
            self.start = node
        else:
            node.next = self.start
            self.start = node

    def insert_last(self, node):
        if not self.start:
            self.start = node
        else:
            current = self.start
            while current.next:
                current = current.next
            current.next = node

    def remove(self, key):
        if not self.start:
            print("The Linked List is empty.")
            return

        if self.start.hash == key:
            self.start = self.start.next
            return

        current = self.start
        prev = None
        while current:
            if current.hash == key:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print(f"Commit with hash {key} was not found.")

    def reverse(self):
        prev = None
        current = self.start
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.start = prev
    '''
    ⬆ Your code ends here.
    '''
