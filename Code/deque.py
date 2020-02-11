from linkedlist import LinkedList
from queue import LinkedQueue

class LinkedDeque(LinkedQueue):
    def __init__(self, iterable=None):
        super().__init__(iterable)
    
    def push_front(self, item):
        """
        Time complexity O(1) -- adding an element to the beginning of the list, calling prepend method from LinkedList class which has is O(1)
        """
        self.list.prepend(item)

    def push_back(self, item):
        """
        Time complexity O(1) -- adding an element to the end of the list, calling enqueue method from Queue class that calls the append method from LinkedList class which has is O(1)
        """
        super().enqueue(item)

    def pop_front(self):
        """
        Time complexity O(1) -- removing element from the beginning of the list, calling dequeue method from Queue class that calls the delete method from LinkedList class which deletes the head
        """
        super().dequeue()

    def pop_back(self):
        """
        Time complexity O(1) -- removing element from the end of the list, calling dequeue method from Queue class that calls the delete method from LinkedList class which deletes the tail
        """
        if self.is_empty():
            raise ValueError()
        else:
            self.list.delete(self.list.get_at_index(self.length() - 1))
