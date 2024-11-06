import main
import LinkedList

import time

for j in (10, 10000, 100000):
    extended_linked_list = main.ExpandedLinkedList()
    extended_linked_list.create_linked_list(range(j))

    start = time.time()
    extended_linked_list.insert(10, extended_linked_list.count_elements // 2)
    print(f"Expanded_Linked_List create time for {j} elements: {time.time() - start}")

    linked_list = LinkedList.LinkedList()
    linked_list.create(range(j))

    start = time.time()
    linked_list.insert(10, linked_list.length // 2)
    print(f"Linked_List create time for {j} elements: {time.time() - start}")

    arr = [i for i in range(j)]
    start = time.time()
    arr.insert(len(arr) // 2, 10)

    print(f"Array create time for {j} elements: {time.time() - start}")
    print("____________________________________________________________________")
