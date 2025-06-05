import unittest
from doubly_linked_list import DoublyLinkedList
from array_based_list import ArrayBasedList


class TestListImplementations(unittest.TestCase):
    def setUp(self):
        self.doubly_list = DoublyLinkedList()
        self.array_list = ArrayBasedList()
        self.lists = [self.doubly_list, self.array_list]

    def test_empty_list_length(self):
        for lst in self.lists:
            self.assertEqual(lst.length(), 0)

    def test_append_single_element(self):
        for lst in self.lists:
            lst.append('f')
            self.assertEqual(lst.length(), 1)
            self.assertEqual(lst.get(0), 'f')

    def test_append_multiple_elements(self):
        for lst in self.lists:
            elements = ['2', 'b', '6', 'f']
            for element in elements:
                lst.append(element)

            self.assertEqual(lst.length(), 4)
            for i, element in enumerate(elements):
                self.assertEqual(lst.get(i), element)

    def test_append_invalid_element(self):
        for lst in self.lists:
            with self.assertRaises(ValueError):
                lst.append(123)

    def test_insert_at_middle(self):
        for lst in self.lists:
            lst.append('r')
            lst.append('v')
            lst.insert('b', 1)

            self.assertEqual(lst.length(), 3)
            self.assertEqual(lst.get(0), 'r')
            self.assertEqual(lst.get(1), 'b')
            self.assertEqual(lst.get(2), 'v')

    def test_delete_single_element(self):
        for lst in self.lists:
            lst.append('a')
            deleted = lst.delete(0)

            self.assertEqual(deleted, 'a')
            self.assertEqual(lst.length(), 0)

    def test_delete_from_beginning(self):
        for lst in self.lists:
            elements = ['a', 'b', 'c']
            for element in elements:
                lst.append(element)

            lst.delete(0)
            self.assertEqual(lst.length(), 2)
            self.assertEqual(lst.get(0), 'b')
            self.assertEqual(lst.get(1), 'c')

    def test_delete_invalid_index(self):
        for lst in self.lists:
            lst.append('a')

            with self.assertRaises(IndexError):
                lst.delete(-1)

    def test_delete_all_existing(self):
        for lst in self.lists:
            elements = ['a', 'b', 'a', 'c', 'a']
            for element in elements:
                lst.append(element)

            lst.delete_all('a')
            self.assertEqual(lst.length(), 2)

    def test_get_valid_index(self):
        for lst in self.lists:
            elements = ['a', 'b', 'c']
            for element in elements:
                lst.append(element)

            for i, element in enumerate(elements):
                self.assertEqual(lst.get(i), element)

    def test_get_invalid_index(self):
        for lst in self.lists:
            lst.append('1')

            with self.assertRaises(IndexError):
                lst.get(-1)

    def test_clone(self):
        for lst in self.lists:
            elements = ['a', 'b', 'c']
            for element in elements:
                lst.append(element)

            cloned = lst.clone()

            self.assertEqual(cloned.length(), lst.length())
            for i in range(lst.length()):
                self.assertEqual(cloned.get(i), lst.get(i))

    def test_reverse_multiple_elements(self):
        for lst in self.lists:
            elements = ['a', 'b', 'c', 'd']
            for element in elements:
                lst.append(element)

            lst.reverse()

            reversed_elements = ['d', 'c', 'b', 'a']
            for i, element in enumerate(reversed_elements):
                self.assertEqual(lst.get(i), element)

    def test_find_first_existing(self):
        for lst in self.lists:
            elements = ['a', 'b', 'a', 'c']
            for element in elements:
                lst.append(element)

            self.assertEqual(lst.find_first('a'), 0)
            self.assertEqual(lst.find_first('b'), 1)
            self.assertEqual(lst.find_first('c'), 3)

    def test_find_first_non_existing(self):
        for lst in self.lists:
            elements = ['a', 'b', 'c']
            for element in elements:
                lst.append(element)

            self.assertEqual(lst.find_first('d'), -1)

    def test_find_last_existing(self):
        for lst in self.lists:
            elements = ['a', 'b', 'a', 'c']
            for element in elements:
                lst.append(element)

            self.assertEqual(lst.find_last('a'), 2)
            self.assertEqual(lst.find_last('b'), 1)
            self.assertEqual(lst.find_last('c'), 3)

    def test_find_last_non_existing(self):
        for lst in self.lists:
            elements = ['a', 'b', 'c']
            for element in elements:
                lst.append(element)

            self.assertEqual(lst.find_last('d'), -1)


if __name__ == '__main__':
    unittest.main()
