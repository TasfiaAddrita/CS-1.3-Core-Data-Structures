from linkedlist import Node, LinkedList

class BinaryNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None

class DoublyLinkedList(LinkedList):
    def __init__(self, iterable=None):
        super().__init__(iterable) # uses append method from DoublyLinkedList, not LinkedList, Polymorphism

    def __str__(self):
        """Return a formatted string representation of this doubly linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' <-> '.join(items))

    def append(self, item):
        new_node = BinaryNode(item)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

        # if not empty, call ...

    def prepend(self, item):
        new_node = BinaryNode(item)
        if self.is_empty():
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def find(self, quality):
        pass

    def delete(self, index):
        pass
    def get_at_index(self, index);
        if index < self.length() // 2:
            super().get_at_index(index)