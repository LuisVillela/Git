'''
[Module] Init command utils.
'''
import os
import utils.data_structures.linked_list as linked_list


def write_file(name: str, lines: list) -> None:

    with open(name, 'w') as writer:
        writer.write('\n'.join(lines))


def get_init_files() -> dict:

    initial_files = {
        '.geet/.geetignore': [".DS_Store\n"],
        '.geet/.hashdict.json': ["{\"README.md\": \"1ea4b01b49eae1fd044238ae5423222eac5495ce\"}\n"],
        'README.md': ["### Geet", "Fresh geet repository.\n"]
    }

    return initial_files


def file_exists(path: str, name: str) -> bool:

    return os.path.exists(path + name)


def create_branch(path: str) -> object:

    '''
    TODO no. 1: Linked List branch

    => We'll use a Linked List to represent the master branch. Each commit will be a node in the LL.

        - In geet/utils/data_structures/linked_list.py you'll find the boilerplate for a linked list class. Based on those docstrings, implement a linked list.

        - Once your data structure is ready, create an empty instance and make it the return of this method.

    ⬇ Your code starts here:
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
        '''
    def __init__(self, hash, message, author, email):
            self.hash = hash
            self.message = message
            self.author = author
            self.email = email
            self.next = None



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
                print("Linked List is empty.")
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

            print(f"Commit with hash {key} not found.")
        
            def reverse(self):
                prev = None
                current = self.start
                while current:
                    next_node = current.next
                    current.next = prev
                    prev = current
                    current = next_node
                self.start = prev

# Crear una instancia vacía de la lista enlazada y devolverla
linked_list_instance = LinkedList()
return linked_list_instance


'''
⬆ Your code ends here.
'''
