from set import Set, HashTable
import unittest

class SetTest(unittest.TestCase):
    def test_init(self):
        s = Set()
        assert s.size() == 0
    
    def test_init_with_list(self):
        s = Set([1, 2, 3])
        assert s.size() == 3
        assert s.contains(1) == True
        assert s.contains(2) == True
        assert s.contains(3) == True
        assert s.contains(4) == False
    
    def test_size(self):
        s = Set()
        assert s.size() == 0
        s.add('A')
        assert s.size() == 1
        s.add('B')
        assert s.size() == 2
        s.add('C')
        assert s.size() == 3

    def test_union(self):
        set_A = Set([1, 2, 3])
        set_B = Set([3, 4, 5])
        set_C = set_A.union(set_B)
        assert set_C.items() == [1, 2, 3, 4, 5]
    
    def test_union_same(self):
        set_A = Set([1, 2, 3])
        set_B = Set([1, 2, 3])
        set_C = set_A.union(set_B)
        assert set_C.items() == [1, 2, 3]
    
    def test_intersection(self):
        set_A = Set([1, 2, 3])
        set_B = Set([3, 4, 5])
        set_C = set_A.intersection(set_B)
        assert set_C.items() == [3]
    
    def test_intersection_empty(self):
        set_A = Set([1, 2, 3])
        set_B = Set([4, 5])
        set_C = set_A.intersection(set_B)
        assert set_C.items() == []
    
    def test_difference(self):
        set_A = Set([1, 2, 3])
        set_B = Set([3, 4, 5])
        set_C = set_A.difference(set_B)
        assert set_C.items() == [1, 2, 4, 5]
    
    def test_difference_empty(self):
        set_A = Set([1, 2, 3])
        set_B = Set([1, 2, 3])
        set_C = set_A.difference(set_B)
        assert set_C.items() == []
    
    def test_is_subset(self):
        set_A = Set([1, 2, 3])
        set_B = Set([2, 3])
        assert set_A.is_subset(set_B) == True
    
    def test_is_subset_false(self):
        set_A = Set([1, 2, 3])
        set_B = Set([2, 3, 5])
        assert set_A.is_subset(set_B) == False


if __name__ == '__main__':
    unittest.main()
