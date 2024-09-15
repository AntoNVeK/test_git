import main
import LinkedList

import time

for j in (10, 10000, 100000):
    extended_linked_list = main.ExpandedLinkedList()
    start = time.time()
    for i in range(j):
        extended_linked_list.insert(i, extended_linked_list.count_elements)

    print(f"Expanded_Linked_List insert end time for {j} elements: {time.time() - start}")

    start = time.time()
    for i in range(j):
        extended_linked_list.pop(extended_linked_list.count_elements - 1)

    print(f"Expanded_Linked_List pop end time for {j} elements: {time.time() - start}")

    linked_list = LinkedList.LinkedList()

    start = time.time()
    for i in range(j):
        linked_list.insert(i, index=linked_list.length)

    print(f"Linked_List insert end time for {j} elements: {time.time() - start}")

    start = time.time()
    for i in range(j):
        linked_list.pop(linked_list.length - 1)

    print(f"Linked_List pop end time for {j} elements: {time.time() - start}")

    arr = []

    start = time.time()
    for i in range(j):
        arr.insert(len(arr), i)

    print(f"Array insert end time for {j} elements: {time.time() - start}")

    start = time.time()
    for i in range(j):
        arr.pop(len(arr) - 1)

    print(f"Array pop end time for {j} elements: {time.time() - start}")

for j in (10, 10000, 100000):
    arr = [i for i in range(j)]
    extended_linked_list = main.ExpandedLinkedList()
    extended_linked_list.create_linked_list(arr)

    linked_list = LinkedList.LinkedList()
    linked_list.create(arr)

    Array = [i for i in range(j)]

    start = time.time()
    extended_linked_list.find(j // 2)
    print(f"Expanded_Linked_List find center time for {j} elements: {time.time() - start}")

    start = time.time()
    linked_list.find(j // 2)
    print(f"Linked_List find center time for {j} elements: {time.time() - start}")

    start = time.time()
    Array.index(j // 2)
    print(f"Array find center time for {j} elements: {time.time() - start}")
