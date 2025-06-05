class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def length(self):
        return self._length

    def append(self, element):
        self._validate_elem_to_append(element)

        new_node = Node(element)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self._length += 1

    def insert(self, element, index):
        self._validate_elem_to_append(element)
        self._validate_index(index)

        if index == self._length:
            self.append(element)
            return

        new_node = Node(element)

        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            current = self._get_node_at_index(index)
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node

        self._length += 1

    def delete(self, index):
        self._validate_index(index)

        node_to_delete = self._get_node_at_index(index)
        element = node_to_delete.data

        if node_to_delete.prev:
            node_to_delete.prev.next = node_to_delete.next
        else:
            self.head = node_to_delete.next

        if node_to_delete.next:
            node_to_delete.next.prev = node_to_delete.prev
        else:
            self.tail = node_to_delete.prev

        self._length -= 1
        return element

    def delete_all(self, element):
        if not isinstance(element, str) or len(element) != 1:
            return

        current = self.head
        while current:
            next_node = current.next
            if current.data == element:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self._length -= 1
            current = next_node

    def get(self, index):
        self._validate_index(index)
        return self._get_node_at_index(index).data

    def clone(self):
        new_list = DoublyLinkedList()
        current = self.head
        while current:
            new_list.append(current.data)
            current = current.next
        return new_list

    def reverse(self):
        if self._length <= 1:
            return

        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev

        self.head, self.tail = self.tail, self.head

    def find_first(self, element):
        if not isinstance(element, str) or len(element) != 1:
            return -1

        current = self.head
        index = 0
        while current:
            if current.data == element:
                return index
            current = current.next
            index += 1
        return -1

    def find_last(self, element):
        if not isinstance(element, str) or len(element) != 1:
            return -1

        current = self.tail
        index = self._length - 1
        while current:
            if current.data == element:
                return index
            current = current.prev
            index -= 1
        return -1

    def clear(self):
        self.head = None
        self.tail = None
        self._length = 0

    def extend(self, elements):
        self._validate_type_to_extend(elements)

        current = elements.head
        while current:
            self.append(current.data)
            current = current.next

    def _validate_elem_to_append(self, element: str) -> None:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character")

    def _validate_type_to_extend(self, elements) -> None:
        if not isinstance(elements, DoublyLinkedList):
            raise TypeError("Elements must be a DoublyLinkedList")

    def _validate_index(self, index: int) -> None:
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")

    def _get_node_at_index(self, index):
        if index < self._length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self._length - 1 - index):
                current = current.prev
        return current

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
