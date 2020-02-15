from linkedlist import LinkedList

class DoublyLinkedList(LinkedList):
    def __init__(self, iterable=None):
        super().__init__(iterable)
        self.prev = None
    
    def __str__(self):
        """Return a formatted string representation of this doubly linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' <-> '.join(items))

    def append(self, item):
        pass

    def delete(self, index):
        pass
