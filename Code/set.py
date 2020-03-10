from hashtable import HashTable

class Set():
    def __init__(self, elements=None):
        "Initialize a new empty set structure, and add each element if a sequence is given"
        self.ht = HashTable(2 * len(elements) if elements is not None else 10)
        if elements is not None:
            for element in elements:
                self.add(element)

    def items(self):
        """
        Return a list of all entries (key-value pairs) in this hash table.
        """
        all_items = []
        for bucket in self.ht.buckets:
            for item in bucket.items():
                all_items.append(item[0])
        return all_items

    def size(self):
        """
        Property that tracks the number of elements in constant time
        """
        return self.ht.size

    def contains(self, element):
        """
        Return a boolean indicating whether element is in this set
        """
        return self.ht.contains(element)

    def add(self, element):
        """Add element to this set, if not present already"""
        return self.ht.set(element, None)

    def remove(self, element):
        """
        Remove element from this set, if present, or else raise KeyError
        """
        return self.ht.delete(element)

    def union(self, other_set):
        """
        Return a new set that is the union of this set and other_set
        """
        union = Set(self.items())
        for o_item in other_set.items():
            if self.contains(o_item) == False:
                union.add(o_item)
        return union

    def intersection(self, other_set):
        """Return a new set that is the intersection of this set and other_set"""
        intersect = Set()
        for o_item in other_set.items():
            if self.contains(o_item):
                intersect.add(o_item)
        return intersect

    def difference(self, other_set):
        """Return a new set that is the difference of this set and other_set"""
        diff = Set(self.items())
        for s_item in self.items():
            if other_set.contains(s_item) == False:
                diff.add(s_item)
            else:
                diff.remove(s_item)
        return diff

    def is_subset(self, other_set):
        """Return a boolean indicating whether other_set is a subset of this set"""
        for s_item in self.items():
            if not other_set.contains(s_item):
                return False
        return True


