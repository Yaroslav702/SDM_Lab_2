class ArrayBasedList:
    def __init__(self):
        self._data = []

    def length(self):
        return len(self._data)

    def append(self, element):
        self._validate_elem_to_append(element)
        self._data.append(element)

    def insert(self, element, index):
        self._validate_elem_to_append(element)
        self._validate_index(index)
        self._data.insert(index, element)

    def delete(self, index):
        self._validate_index(index)
        return self._data.pop(index)

    def delete_all(self, element):
        if not isinstance(element, str) or len(element) != 1:
            return

        self._data = [item for item in self._data if item != element]

    def get(self, index):
        self._validate_index(index)
        return self._data[index]

    def clone(self):
        new_list = ArrayBasedList()
        new_list._data = self._data.copy()
        return new_list

    def reverse(self):
        self._data.reverse()

    def findFirst(self, element):
        if not isinstance(element, str) or len(element) != 1:
            return -1

        try:
            return self._data.index(element)
        except ValueError:
            return -1

    def find_last(self, element):
        if not isinstance(element, str) or len(element) != 1:
            return -1

        for i in range(len(self._data) - 1, -1, -1):
            if self._data[i] == element:
                return i
        return -1

    def clear(self):
        self._data.clear()

    def extend(self, elements):
        self._validate_type_to_extend(elements)
        self._data.extend(elements._data)

    def to_list(self):
        return self._data.copy()

    def _validate_elem_to_append(self, element: str) -> None:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character")

    def _validate_type_to_extend(self, elements) -> None:
        if not isinstance(elements, ArrayBasedList):
            raise TypeError("Elements must be a ArrayBasedList")

    def _validate_index(self, index: int) -> None:
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of range")
