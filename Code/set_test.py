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

    def test_add(self):
        s = Set()
        assert s.items() == []
        s.add('A')
        assert s.items() == ['A']
        s.add('B')
        assert sorted(s.items()) == ['A', 'B']
        s.add('C')
        assert sorted(s.items()) == ['A', 'B', 'C']
        s.add('A')
        assert sorted(s.items()) == ['A', 'B', 'C']

    def test_remove(self):
        s = Set([1, 2, 3, 4, 5])
        s.remove(4)
        assert s.items() == [1, 2, 3, 5]
        s.remove(2)
        assert s.items() == [1, 3, 5]
        with self.assertRaises(KeyError):
            s.remove(2)  # Key no longer exists
        with self.assertRaises(KeyError):
            s.remove(6)  # Key does not exist

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
        # assert set_C.items() == [1, 2, 4, 5]
        assert set_C.items() == [1, 2]
    
    def test_difference_empty(self):
        set_A = Set([1, 2, 3])
        set_B = Set([1, 2, 3])
        set_C = set_A.difference(set_B)
        assert set_C.items() == []
    
    def test_is_subset(self):
        set_A = Set([1, 2])
        set_B = Set([1, 2, 3])
        assert set_A.is_subset(set_B) == True

    def test_is_subset_false_1(self):
        set_A = Set([1, 2, 3])
        set_B = Set([2, 3])
        assert set_A.is_subset(set_B) == False
    
    def test_is_subset_false(self):
        set_A = Set([1, 2, 3])
        set_B = Set([2, 3, 5])
        assert set_A.is_subset(set_B) == False
    
    def test_is_subset_of_setA(self):
        set_A = Set(['A'])
        set_B = Set(['A', 'B'])
        assert set_A.is_subset(set_B) == True # is set_A a subset of set_B
    
    def test_is_subset_empty_true(self):
        set_A = Set([1, 2, 3])
        set_B = Set()
        assert set_A.is_subset(set_B) == False


if __name__ == '__main__':
    unittest.main()
