import math


def calculate_optimal_node_size(num_elements):
    element_size = 4
    cache_line_size = 64
    total_memory = num_elements * element_size
    num_cache_lines = math.ceil(total_memory / cache_line_size) + 1
    return num_cache_lines


class Node:

    def __init__(self, next=None):
        self.elements = []
        self.next = next


class LinkedList:
    def __init__(self, size_node=0, count_elements=0, elements=[]):
        self.head = None
        self.size_node = size_node
        self.count_elements = count_elements
        if elements:
            self.create_linked_list(elements)

    def create_linked_list(self, elements):
        if not elements:
            return None
        self.count_elements = len(elements)
        self.size_node = calculate_optimal_node_size(self.count_elements)

        self.head = Node()
        current = self.head

        i = 0
        while i < len(elements):
            for j in range(self.size_node):
                if i < len(elements):
                    current.elements.append(elements[i])
                    i += 1
                else:
                    break
            if i < len(elements):
                current.next = Node()
                current = current.next

    def print_linked_list(self):
        node_number = 0
        current = self.head
        while current:
            print(f"Node {node_number}:", end=" ")
            print(" ".join(map(str, current.elements)))
            current = current.next
            node_number += 1

    def pop(self, index):
        if index < 0 or index >= self.count_elements:
            raise IndexError("Linked List out of range")
        self.count_elements -= 1
        flag = 0
        size = calculate_optimal_node_size(self.count_elements)
        if self.size_node != size:
            self.size_node = size
            flag = 1

        if index == 0:
            if len(self.head.elements) > 1:
                self.head.elements.pop(0)
            elif self.head.next:
                self.head = self.head.next
            else:
                self.head = None

        elif index == self.count_elements:
            current = self.head
            penultimate = None
            while current.next:

                if current and current.next and not current.next.next:
                    penultimate = current

                current = current.next

            if len(current.elements) - 1 == 0:
                penultimate.next = None
            else:
                current.elements = current.elements[:-1]

        else:
            i = 0
            current = self.head
            previous = None

            while current:
                if i + len(current.elements) < index:
                    i += len(current.elements)
                    previous = current
                    current = current.next
                    continue
                for j in range(len(current.elements)):
                    if i == index:
                        if len(current.elements) - 1 > 0:
                            current.elements.pop(j)
                        else:
                            previous.next = current.next

                    i += 1

                previous = current
                current = current.next
        if flag:
            self.balance()

    def balance(self):
        current = self.head

        while current:
            if len(current.elements) > self.size_node:
                new_node = Node()
                new_node.elements = current.elements[len(current.elements) // 2:]
                new_node.next = current.next
                current.elements = current.elements[:len(current.elements) // 2]
                current.next = new_node

            current = current.next

    def search(self, el):
        index = 0

        current = self.head

        while current:
            for i in range(len(current.elements)):
                if current.elements[i] == el:
                    return index
                index += 1

            current = current.next
        return -1

    def insert(self, element, index):
        if index < 0 or index > self.count_elements:
            raise IndexError("Linked List out of range")

        self.count_elements += 1
        self.size_node = calculate_optimal_node_size(self.count_elements)
        if index == 0:
            if self.head and len(self.head.elements) < self.size_node:
                self.head.elements.insert(0, element)


            elif self.head == None:
                self.head = Node()
                self.head.elements.append(element)

            else:
                new_node = Node()
                new_node.elements = self.head.elements[:len(self.head.elements) // 2]
                new_node.elements.insert(0, element)

                self.head.elements = self.head.elements[len(self.head.elements) // 2:]
                current = self.head
                new_node.next = current
                self.head = new_node


        elif index == self.count_elements - 1:
            current = self.head

            while current.next:
                current = current.next

            if len(current.elements) < self.size_node:
                current.elements.append(element)

            else:
                new_node = Node()
                new_node.elements = current.elements[(len(current.elements) // 2 + 1):]
                new_node.elements.append(element)

                current.elements = current.elements[:(len(current.elements) // 2 + 1)]
                current.next = new_node

        else:
            i = 0

            current = self.head

            while current:
                if i + len(current.elements) < index:
                    i += len(current.elements)
                    current = current.next
                    continue

                for j in range(len(current.elements)):
                    if i == index:

                        if len(current.elements) + 1 <= self.size_node:
                            current.elements.insert(j, element)

                        else:

                            current.elements.insert(j, element)
                            right_elements = current.elements[len(current.elements) // 2:]
                            current.elements = current.elements[:len(current.elements) // 2]

                            next_node = current.next

                            new_node = Node()
                            new_node.elements = right_elements

                            current.next = new_node
                            new_node.next = next_node

                    i += 1

                current = current.next

    def search_element(self, index) -> int:

        if index < 0 or index >= self.count_elements:
            raise IndexError("Linked List out of range")

        i = 0

        current = self.head

        while current:
            if i + len(current.elements) < index:
                i += len(current.elements)
                current = current.next
                continue
            for j in range(len(current.elements)):

                if i == index:
                    return current.elements[j]
                i += 1

            current = current.next


def check(arr1, arr2, n_array=[]):
    linked_list = LinkedList()
    linked_list.create_linked_list(arr1)

    for i in arr2:
        index = linked_list.search(i)
        print(f"index: {index}")
        if index != -1:
            linked_list.pop(index)
        print("______________")


