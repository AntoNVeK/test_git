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


class ExpandedLinkedList:
    def __init__(self, elements=[], size_node=16, count_elements=0):
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

        if index == 0:
            if len(self.head.elements) > 2 or (len(self.head.elements) > 1 and (
                    not self.head.next or len(self.head.next.elements) == self.size_node)):
                self.head.elements.pop(0)
            elif self.head.next and len(self.head.elements) > 1 and len(self.head.next.elements) < self.size_node:
                self.head.next.elements.insert(0, self.head.elements[1])
                self.head = self.head.next
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
            elif len(penultimate.elements) < self.size_node and len(current.elements) - 1 == 1:
                penultimate.elements.append(current.elements[0])
                penultimate.next = None
            else:
                current.elements = current.elements[:-1]

        else:
            i = 0
            current = self.head
            previous = None

            while current:
                if i + len(current.elements) <= index:
                    i += len(current.elements)
                    previous = current
                    current = current.next
                    continue

                if len(current.elements) > 2:
                    current.elements.pop(index - i)
                    break
                # 1 2
                elif previous and len(previous.elements) < self.size_node and len(current.elements) == 2:
                    current.elements.pop(index - i)
                    previous.elements.append(current.elements[0])
                    previous.next = current.next
                    break
                elif current.next and len(current.next.elements) < self.size_node and len(current.elements) == 2:
                    current.elements.pop(index - i)
                    current.next.elements.insert(0, current.elements[0])
                    if previous:
                        previous.next = current.next
                    else:
                        self.head = self.head.next
                    break
                elif (not previous and not current.next) or (previous and len(previous.elements) == self.size_node) or (current.next and len(current.next.elements) == self.size_node):
                    current.elements.pop(index - i)
                    break
                else:
                    previous.next = current.next
                    break

    def find(self, el):
        index = 0

        current = self.head

        while current:
            if el in current.elements:
                return index + current.elements.index(el)
            index += len(current.elements)

            current = current.next
        return -1

    def insert(self, element, index):
        if index < 0 or index > self.count_elements:
            raise IndexError("Linked List out of range")

        self.count_elements += 1

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

                if len(current.elements) + 1 <= self.size_node:
                    current.elements.insert(index - i, element)
                    break

                else:

                    current.elements.insert(index - i, element)
                    right_elements = current.elements[len(current.elements) // 2:]
                    current.elements = current.elements[:len(current.elements) // 2]

                    next_node = current.next

                    new_node = Node()
                    new_node.elements = right_elements

                    current.next = new_node
                    new_node.next = next_node
                    break

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
    linked_list = ExpandedLinkedList()
    linked_list.create_linked_list(arr1)

    for i in arr2:
        index = linked_list.find(i)
        print(f"index: {index}")
        if index != -1:
            linked_list.pop(index)
        print("______________")


if __name__ == '__main__':
    linked_list = ExpandedLinkedList(range(27))


    linked_list.print_linked_list()
