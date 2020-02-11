from deque import LinkedDeque
import unittest

class DequeTest(unittest.TestCase):
    def test_init(self):
        dq = LinkedDeque()
        assert dq.front() is None
        assert dq.length() == 0
        assert dq.is_empty() is True
    
    def test_init_with_list(self):
        dq = LinkedDeque(['A', 'B', 'C'])
        assert dq.front() == 'A'
        assert dq.length() == 3
        assert dq.is_empty() is False
    
    def test_length(self):
        dq = LinkedDeque()
        assert dq.length() == 0
        dq.push_back('A')
        assert dq.length() == 1
        dq.push_back('B')
        assert dq.length() == 2
        dq.pop_front()
        assert dq.length() == 1
        dq.pop_front()
        assert dq.length() == 0
    
    def test_push_front(self):
        dq = LinkedDeque()
        dq.push_front('A')
        assert dq.length() == 1
        assert dq.front() == 'A'
        dq.push_front('B')
        assert dq.length() == 2
        assert dq.front() == 'B'
        dq.push_front('C')
        assert dq.length() == 3
        assert dq.front() == 'C'
        assert dq.is_empty() == False
        # should look like C -> B -> A
    
    def test_push_back(self):
        dq = LinkedDeque()
        dq.push_back('A')
        assert dq.length() == 1
        assert dq.front() == 'A'
        dq.push_back('B')
        assert dq.length() == 2
        assert dq.front() == 'A'
        dq.push_back('C')
        assert dq.length() == 3
        assert dq.front() == 'A'
        assert dq.is_empty() == False
        # should look like A -> B -> C 
    
    def test_pop_front(self):
        dq = LinkedDeque(['A', 'B', 'C'])
        assert dq.length() == 3
        assert dq.front() == 'A'
        dq.pop_front()
        assert dq.length() == 2
        assert dq.front() == 'B'
        dq.pop_front()
        assert dq.length() == 1
        assert dq.front() == 'C'
        assert dq.is_empty() == False
        dq.pop_front()
        assert dq.length() == 0
        assert dq.front() == None
        assert dq.is_empty() == True

    def test_pop_back(self):
        dq = LinkedDeque(['A', 'B', 'C'])
        assert dq.length() == 3
        assert dq.front() == 'A'
        dq.pop_back()
        assert dq.length() == 2
        assert dq.front() == 'A'
        dq.pop_back()
        assert dq.length() == 1
        assert dq.front() == 'A'
        assert dq.is_empty() == False
        dq.pop_back()
        assert dq.length() == 0
        assert dq.front() == None
        assert dq.is_empty() == True


if __name__ == '__main__':
    unittest.main()
