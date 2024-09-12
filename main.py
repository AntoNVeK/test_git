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
        if index < 0 or index > self.count_elements:
            raise IndexError("Linked List out of range")
        if self.size_node != calculate_optimal_node_size(self.count_elements - 1):

            current = self.head

            i = 0

            arr = []
            while current:
                for j in current.elements:
                    if i != index:
                        arr.append(j)
                    i += 1
                current = current.next
            if arr:
                self.create_linked_list(arr)
            else:
                self.head = None

        else:

            i = 0

            penultimate_node = None

            flag = 1

            current = self.head

            while current:

                for j in range(len(current.elements)):

                    if i == index and flag:
                        flag = 0

                        if j == len(current.elements) - 1 and current.next:
                            current.elements[j] = current.next.elements[0]



                        elif j == len(current.elements) - 1:
                            current.elements = current.elements[:-1]

                        else:
                            current.elements[j] = current.elements[j + 1]

                    elif flag == 0:
                        if j == len(current.elements) - 1 and current.next:
                            current.elements[j] = current.next.elements[0]

                        elif j == len(current.elements) - 1:
                            current.elements = current.elements[:-1]

                        else:
                            current.elements[j] = current.elements[j + 1]

                    i += 1
                if current and current.next and current.next.next == None:
                    penultimate_node = current
                current = current.next

            if penultimate_node and penultimate_node.next and len(penultimate_node.next.elements) == 0:
                penultimate_node.next = None

            self.count_elements -= 1
            # self.print_linked_list()

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

        if self.size_node != calculate_optimal_node_size(self.count_elements + 1):
            current = self.head
            arr = []

            while current:
                arr += current.elements
                current = current.next

            arr.insert(index, element)

            self.create_linked_list(arr)
        else:
            i = 0

            current = self.head

            flag = 1
            last_node = None
            previous = None

            while current:

                for j in range(len(current.elements)):
                    if i == index and flag:
                        flag = 0
                        previous = current.elements[j]
                        current.elements[j] = element

                    elif flag == 0:
                        el = current.elements[j]
                        current.elements[j] = previous
                        previous = el
                    i += 1

                if current != None and current.next == None:
                    last_node = current
                current = current.next

            if not previous:
                previous = element

            if last_node and len(last_node.elements) < self.size_node:
                last_node.elements.append(previous)

            elif last_node:
                new_node = Node()
                new_node.elements.append(previous)
                last_node.next = new_node

            self.count_elements += 1
        # self.print_linked_list()

    def search_element(self, index) -> int:

        if index < 0 or index >= self.count_elements:
            raise IndexError("Linked List out of range")

        i = 0

        current = self.head

        while current:
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


linked_list = LinkedList()
linked_list.create_linked_list([100, 200, 300])

print(linked_list.search_element(2))
