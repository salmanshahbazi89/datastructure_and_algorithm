from src.complexity.time_complexity import time_it
import time


@time_it
def linear_search(numbers_list, item_to_search):
    for idx, element in enumerate(numbers_list):
        if element == item_to_search:
            return idx
    return -1


@time_it
def binary_search(numbers_list, item_to_search):
    left_idx = 0
    right_idx = len(numbers_list) - 1

    while left_idx <= right_idx:
        mid_idx = (right_idx + left_idx) // 2

        if numbers_list[mid_idx] == item_to_search:
            return mid_idx

        if numbers_list[mid_idx] < item_to_search:
            left_idx = mid_idx + 1

        if numbers_list[mid_idx] > item_to_search:
            right_idx = mid_idx - 1

    return -1


def binary_search_recursive(numbers_list, item_to_search, left_idx, right_idx):
    mid_idx = (right_idx + left_idx) // 2

    if mid_idx < 0 or mid_idx > len(numbers_list):
        return -1

    if numbers_list[mid_idx] == item_to_search:
        return mid_idx

    if numbers_list[mid_idx] < item_to_search:
        return binary_search_recursive(numbers_list, item_to_search, mid_idx + 1, right_idx)

    if numbers_list[mid_idx] > item_to_search:
        return binary_search_recursive(numbers_list, item_to_search, left_idx, mid_idx - 1)


if __name__ == '__main__':
    numbers_list = [i for i in range(750000000)]
    item_to_search = 745000000

    index_linear = linear_search(numbers_list, item_to_search)
    index_binary = binary_search(numbers_list, item_to_search)
    start = time.time()
    index_binary_recursive = binary_search_recursive(numbers_list, item_to_search, 0, len(numbers_list) - 1)
    end = time.time()
    print(f"item was found in {index_linear} by linear search")
    print(f"item was found in {index_binary} by binary search")

    print(f"item was found in {index_binary_recursive} by recursive binary search")
    print("index_binary_recursive" + " took " + str((end - start) * 1000) + " mil seconds")
