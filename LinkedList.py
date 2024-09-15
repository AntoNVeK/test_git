class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def create(self, arr):
        if not arr:
            return

        # Создаем первый узел
        self.head = Node(arr[0])
        self.tail = self.head

        # Создаем остальные узлы и связываем их
        for value in arr[1:]:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def insert(self, el, index):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")

        new_node = Node(el)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:  # Если список был пуст, обновляем tail
                self.tail = new_node
        elif index == self.length:  # Вставка в конец
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.length += 1

    def pop(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        if index == 0:
            removed_element = self.head.data
            self.head = self.head.next
            if self.head is None:  # Если список стал пустым, обновляем tail
                self.tail = None
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            removed_element = current.next.data
            current.next = current.next.next
            if index == self.length - 1:  # Если удаляем последний элемент, обновляем tail
                self.tail = current

        self.length -= 1
        return removed_element

    def find(self, el):
        current = self.head
        index = 0
        while current:
            if current.data == el:
                return index
            current = current.next
            index += 1
        return -1  # Если элемент не найден

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)
